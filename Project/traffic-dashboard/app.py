import streamlit as st
import folium
from streamlit.components.v1 import html
import pandas as pd
from folium.plugins import HeatMap
from folium import CircleMarker
from traffic_data import get_congestion_for_cities
from utils import normalize_congestion, congestion_to_color, radius_from_congestion
import os
from datetime import datetime

# ---------------- CONFIG ----------------
API_KEY = os.getenv("MAPMYINDIA_KEY", "mtsynbfageotfudxcyvuubuzjmnrpmykkizz")

st.set_page_config(
    page_title="India Real-Time Traffic Dashboard",
    page_icon="🚦",
    layout="wide"
)

REFRESH_INTERVAL_SEC = 30

# ---------------- HEADER ----------------
st.title("🚦 India Real-Time Traffic Dashboard")
st.markdown(
    "Live traffic updates across major Indian cities. "
    "Tiles & overlays powered by MapmyIndia. If numeric data is unavailable, "
    "a deterministic simulated fallback is used."
)

# ---------------- SIDEBAR ----------------
with st.sidebar:
    st.header("🔍 Explore Traffic")
    city_list = [
        "Mumbai", "Delhi", "Bengaluru", "Chennai", "Pune",
        "Hyderabad", "Kolkata", "Ahmedabad", "Jaipur", "Lucknow"
    ]
    selected_city = st.selectbox("Jump to a city", city_list)

    st.markdown("---")
    st.write("MapmyIndia API Key Status:")
    if API_KEY and "your_key_here" not in API_KEY.lower():
        st.success("✅ API key detected")
    else:
        st.warning("⚠️ No valid MapmyIndia key — simulated data only")

    if st.button("🔄 Refresh Data"):
        st.cache_data.clear()
        st.rerun()

# ---------------- CITY COORDINATES ----------------
city_coords = {
    "Mumbai": (19.0760, 72.8777),
    "Delhi": (28.6139, 77.2090),
    "Bengaluru": (12.9716, 77.5946),
    "Chennai": (13.0827, 80.2707),
    "Pune": (18.5204, 73.8567),
    "Hyderabad": (17.3850, 78.4867),
    "Kolkata": (22.5726, 88.3639),
    "Ahmedabad": (23.0225, 72.5714),
    "Jaipur": (26.9124, 75.7873),
    "Lucknow": (26.8467, 80.9462)
}

# ---------------- DATA FETCH ----------------
@st.cache_data(ttl=REFRESH_INTERVAL_SEC)
def fetch_hotspots():
    return get_congestion_for_cities(city_coords, API_KEY, prefer_mapmyindia=True)

hotspots = fetch_hotspots()

# ---------------- MAP ----------------
lat, lon = city_coords[selected_city]
m = folium.Map(location=[lat, lon], zoom_start=11, tiles="cartodbpositron")

# MapmyIndia live traffic tiles
if API_KEY:
    folium.TileLayer(
        tiles=f"https://apis.mapmyindia.com/advancedmaps/v1/{API_KEY}/traffic/256/{{z}}/{{x}}/{{y}}.png",
        attr="MapmyIndia",
        name="MapmyIndia Live Traffic",
        overlay=True,
        control=True,
        max_zoom=18
    ).add_to(m)

# Add congestion data as circles + labels
heat_data = []
for spot in hotspots:
    city = spot["city"]
    clat = spot["lat"]
    clon = spot["lon"]
    congestion = float(spot["congestion"])

    heat_data.append([clat, clon, normalize_congestion(congestion)])

    CircleMarker(
        location=[clat, clon],
        radius=radius_from_congestion(congestion),
        color=congestion_to_color(congestion),
        fill=True,
        fill_opacity=0.6,
        popup=f"{city} — {congestion}% (source: {spot.get('source')})"
    ).add_to(m)

    folium.map.Marker(
        [clat, clon],
        icon=folium.DivIcon(
            html=f"""<div style="font-size:12px;color:#222">{city}: {congestion}%</div>"""
        )
    ).add_to(m)

# Add heatmap overlay
HeatMap(heat_data, radius=25, blur=18, min_opacity=0.4).add_to(m)
folium.LayerControl().add_to(m)

# Display map
m.save("map.html")
with open("map.html", "r", encoding="utf-8") as f:
    map_html = f.read()
st.components.v1.html(map_html, height=650, scrolling=True)

# ---------------- CHARTS + METRICS ----------------
st.markdown("---")
st.subheader("📊 Live Congestion Comparison")

df = pd.DataFrame(
    [{"City": s["city"], "Congestion (%)": s["congestion"], "Source": s["source"]} for s in hotspots]
)
df_sorted = df.sort_values("Congestion (%)", ascending=False)

col1, col2 = st.columns([2, 1])
with col1:
    st.bar_chart(df_sorted.set_index("City")["Congestion (%)"])

with col2:
    top = df_sorted.iloc[0]
    st.metric(label=f"Highest congestion: {top['City']}", value=f"{top['Congestion (%)']}%")
    selected_row = df[df["City"] == selected_city].iloc[0]
    st.metric(label=f"{selected_city} congestion", value=f"{selected_row['Congestion (%)']}%")
    st.markdown("**Details:**")
    st.dataframe(selected_row)

# ---------------- FOOTER ----------------
st.markdown("#### Sources & Raw Data")
st.dataframe(df.assign(Updated=str(datetime.utcnow())))

st.markdown("---")
st.caption(
    "Made with ❤️ using Python, Streamlit, Folium, and MapmyIndia APIs. "
    "If MapmyIndia endpoints are unavailable, deterministic simulated fallback is used."
)
st.caption("Tip: Set environment variable `MAPMYINDIA_KEY` to secure your API key.")
