# utils.py
import math

def normalize_congestion(value, min_val=0, max_val=100):
    """
    Normalize congestion percentage (0-100) to 0-1 for heatmap weight.
    Clips to range.
    """
    try:
        v = float(value)
    except Exception:
        v = 0.0
    if v < min_val: v = min_val
    if v > max_val: v = max_val
    return (v - min_val) / (max_val - min_val)

def congestion_to_color(percent):
    """
    Returns a simple CSS color based on congestion percent:
    0-40 -> greenish, 40-70 -> yellow/orange, 70-100 -> red.
    """
    p = max(0, min(100, int(percent)))
    if p < 40:
        return "#2ecc71"  # green
    elif p < 70:
        return "#f1c40f"  # yellow
    else:
        return "#e74c3c"  # red

def radius_from_congestion(percent, min_r=6, max_r=30):
    """
    Scales circle radius by congestion percent.
    """
    p = max(0, min(100, float(percent)))
    return min_r + (max_r - min_r) * (p / 100.0)
