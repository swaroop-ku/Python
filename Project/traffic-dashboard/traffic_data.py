"""
Traffic data fetcher for MapmyIndia + fallback simulation.
"""

import requests
import hashlib
from datetime import datetime


# ---------------- SIMULATION ----------------
def _deterministic_simulated_congestion(lat, lon, t=None):
    if t is None:
        t = datetime.utcnow()

    hour = t.hour
    if 7 <= hour <= 10:  # morning rush
        peak = 1.0
    elif 17 <= hour <= 19:  # evening rush
        peak = 0.9
    else:
        peak = 0.45

    h = hashlib.sha1(f"{lat},{lon}".encode()).hexdigest()
    seed = int(h[:8], 16) % 100
    base = 40 + (seed % 30)
    simulated = base * (0.6 + peak * 0.8)
    simulated = max(20, min(95, simulated))
    return round(simulated, 1)


# ---------------- MAPMYINDIA FLOW ----------------
def try_mapmyindia_flow(lat, lon, api_key):
    endpoints = [
        f"https://apis.mapmyindia.com/advancedmaps/v1/{api_key}/traffic/flow?center={lat},{lon}",
        f"https://apis.mapmyindia.com/traffic/v1/flow?point={lat},{lon}&key={api_key}",
        f"https://atlas.mapmyindia.com/traffic/v1/flowSegment?point={lat},{lon}&key={api_key}",
    ]

    for ep in endpoints:
        try:
            resp = requests.get(ep, timeout=6)
            if resp.status_code != 200:
                continue
            j = resp.json()

            if isinstance(j, dict):
                # format 1
                if "flowSegmentData" in j:
                    fs = j["flowSegmentData"]
                    cs = fs.get("currentSpeed") or fs.get("current_travel_speed")
                    ffs = fs.get("freeFlowSpeed") or fs.get("free_flow_speed")
                    if cs and ffs:
                        congestion_pct = max(0, min(100, (1 - (float(cs) / float(ffs))) * 100))
                        return {"source": ep, "congestion": round(congestion_pct, 1)}

                # format 2
                if "flow" in j and isinstance(j["flow"], dict):
                    cs = j["flow"].get("currentSpeed") or j["flow"].get("speed")
                    ffs = j["flow"].get("freeFlowSpeed") or j["flow"].get("freeFlow")
                    if cs and ffs:
                        congestion_pct = max(0, min(100, (1 - (float(cs) / float(ffs))) * 100))
                        return {"source": ep, "congestion": round(congestion_pct, 1)}

                # fallback if congestion exists
                if "congestion" in j:
                    try:
                        return {"source": ep, "congestion": float(j["congestion"])}
                    except Exception:
                        pass
        except requests.exceptions.RequestException:
            continue
        except Exception:
            continue

    return None


# ---------------- MAIN FUNCTION ----------------
def get_congestion_for_cities(city_coords, api_key, prefer_mapmyindia=True):
    results = []

    for city, (lat, lon) in city_coords.items():
        data = None

        if prefer_mapmyindia:
            try:
                data = try_mapmyindia_flow(lat, lon, api_key)
            except Exception:
                data = None

        if data and "congestion" in data:
            congestion = float(data["congestion"])
            source = data.get("source", "mapmyindia_flow")
        else:
            congestion = _deterministic_simulated_congestion(lat, lon)
            source = "simulated_fallback"

        results.append({
            "city": city,
            "lat": lat,
            "lon": lon,
            "congestion": round(float(congestion), 1),
            "source": source
        })

    return results
