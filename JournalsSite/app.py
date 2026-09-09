from flask import Flask, render_template, jsonify
import folium
import json

app = Flask(__name__)

# Load publications data
with open("data/publication.json", "r") as f:
    publications_data = json.load(f)

# Load GeoJSON
romania_geojson = "static/romania_counties.json"

@app.route("/")
def index():
    # Create a base map
    m = folium.Map(location=[46.0, 25.0], zoom_start=7)

    # Add GeoJSON with custom JS for click events
    folium.GeoJson(
        romania_geojson,
        name="Romania Counties",
        style_function=lambda x: {"fillColor": "blue", "color": "black"},
    ).add_to(m)

    # Save the map to an HTML template
    m.save("templates/map.html")
    return render_template("map.html")

@app.route("/api/publications/<county>")
def get_publications(county):
    return jsonify(publications_data.get(county, []))

if __name__ == "__main__":
    app.run(debug=True)