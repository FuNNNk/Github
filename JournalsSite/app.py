from flask import Flask, send_from_directory, jsonify
import folium
import json
import os

app = Flask(__name__)

# Load publications data
with open("data/publication.json", "r",  encoding="utf-8") as f:
    publications_data = json.load(f)

# Load GeoJSON
romania_geojson = "static/romania_counties.json"

# Generate the standalone HTML map
def generate_map():
    m = folium.Map(location=[46.0, 25.0], zoom_start=7)
    folium.GeoJson(
        romania_geojson,
        name="Romania Counties",
        style_function=lambda x: {"fillColor": "blue", "color": "black", "fillOpacity": 0.5},
    ).add_to(m)
    return m

# Generate and save the map HTML
map_html = generate_map()._repr_html_()
with open("templates/map.html", "w", encoding="utf-8") as f:
    f.write(map_html)


@app.route("/")
def index():
    return send_from_directory("templates", "map.html")

@app.route("/static/romania_counties.json")
def serve_geojson():
    return send_from_directory("static", "romania_counties.json")

@app.route("/api/publications/<county>")
def get_publications(county):
    return jsonify(publications_data.get(county, []))

if __name__ == "__main__":
    os.makedirs("templates", exist_ok=True)
    app.run(debug=True)