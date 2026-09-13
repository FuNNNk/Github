from flask import Flask, render_template, send_from_directory, jsonify
import json

app = Flask(__name__)

# Load publications data
with open("data/publication.json", "r", encoding="utf-8") as f:
    publications_data = json.load(f)

# Serve the map page
@app.route("/")
def index():
    return render_template("romania_map.html")

# Serve the publications list page
@app.route("/publications/<county>")
def county_publications(county):
    publications = publications_data.get(county, [])
    return render_template("county_publications.html", county=county, publications=publications)

# Serve GeoJSON file
@app.route("/static/romania_counties.json")
def serve_geojson():
    return send_from_directory("static", "romania_counties.json")

if __name__ == "__main__":
    app.run(debug=True, port=5000)