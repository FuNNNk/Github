// Load GeoJSON and add click events
fetch("romania_counties.geojson")
  .then((response) => response.json())
  .then((data) => {
    L.geoJSON(data, {
      onEachFeature: (feature, layer) => {
        layer.on("click", () => {
          const countyName = feature.properties.name;
          fetchPublications(countyName);
        });
      },
    }).addTo(map);
  });

// Fetch publications for a county
function fetchPublications(county) {
  // Replace with actual API or dataset
  const publications = {
    "București": ["Publication 1", "Publication 2"],
    "Cluj": ["Publication A", "Publication B"],
  };
  alert(`Publications for ${county}: ${publications[county].join(", ")}`);
}