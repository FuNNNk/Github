import folium
from folium.plugins import FastMarkerCluster

# Load GeoJSON for Romania's counties
romania_geojson = "romania_counties.json"

# Create a base map centered on Romania
m = folium.Map(location=[46.0, 25.0], zoom_start=7)

# Add county boundaries
folium.GeoJson(
    romania_geojson,
    name="Romania Counties",
    style_function=lambda x: {"fillColor": "blue", "color": "black"},
).add_to(m)

# Add click events (requires JavaScript)
# This is a placeholder; actual implementation requires custom JS.
m.save("romania_map.html")