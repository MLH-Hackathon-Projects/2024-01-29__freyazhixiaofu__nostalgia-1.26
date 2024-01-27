document.addEventListener('DOMContentLoaded', function() {
    const urlParams = new URLSearchParams(window.location.search);
    const searchQuery = urlParams.get('q');

    fetch(`https://openaccess-api.clevelandart.org/api/artworks?has_image=1&q=${encodeURIComponent(searchQuery)}&limit=10`)
        .then(response => response.json())
        .then(data => {
            let resultsHTML = '';
            if (data.data && data.data.length > 0) {
                data.data.forEach(artwork => {
                    const tombstone = artwork.tombstone;
                    const image = artwork.images.web.url;
                    resultsHTML += `<div><img src="${image}" alt="${artwork.title}" style="max-width:100%;"><p>${tombstone}</p></div>`;
                });
            } else {
                resultsHTML = '<p>No results found</p>';
            }
            document.getElementById('results').innerHTML = resultsHTML;
        });
});
