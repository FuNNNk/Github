// Initialize the map (Folium already does this, but we add click events)
document.addEventListener("DOMContentLoaded", () => {
  const map = L.map("map"); // Assuming Folium initializes this

  // Fetch GeoJSON and add click events
  fetch("/JournalsSite/static/romania_counties.json")
    .then((response) => response.json())
    .then((data) => {
      L.geoJSON(data, {
        onEachFeature: (feature, layer) => {
          const countyName = feature.properties.name;
          layer.on("click", () => {
            fetchPublications(countyName);
          });
        },
      }).addTo(map);
    });

  // Fetch publications from Flask API
  function fetchPublications(county) {
    fetch(`/api/publications/${county}`)
      .then((response) => response.json())
      .then((publications) => {
        if (publications.length > 0) {
          showPublicationsModal(county, publications);
        } else {
          alert(`No publications found for ${county}.`);
        }
      });
  }

  // Display publications in a modal
  function showPublicationsModal(county, publications) {
    const modal = document.createElement("div");
    modal.style.position = "fixed";
    modal.style.top = "20px";
    modal.style.right = "20px";
    modal.style.background = "white";
    modal.style.padding = "10px";
    modal.style.border = "1px solid black";
    modal.style.zIndex = "1000";
    modal.innerHTML = `
      <h3>Publications for ${county}</h3>
      <ul>
        ${publications.map(pub => `<li><a href="${pub}" target="_blank">${pub}</a></li>`).join("")}
      </ul>
    `;
    document.body.appendChild(modal);
  }
});