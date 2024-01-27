document.addEventListener('DOMContentLoaded', function() {
    const urlParams = new URLSearchParams(window.location.search);
    const searchQuery = urlParams.get('q');

    fetch(`https://collectionapi.metmuseum.org/public/collection/v1/search?q=${encodeURIComponent(searchQuery)}&hasImages=true`)
        .then(response => response.json())
        .then(data => {
            let resultsHTML = '';
            if (data.objectIDs) {
                data.objectIDs.slice(0, 10).forEach(objectID => {
                    fetch(`https://collectionapi.metmuseum.org/public/collection/v1/objects/${objectID}`)
                        .then(response => response.json())
                        .then(objectData => {
                            resultsHTML += `<div><img src="${objectData.primaryImage}" alt="${objectData.title}"><p>${objectData.title}</p></div>`;
                            document.getElementById('results').innerHTML = resultsHTML;
                        });
                });
            } else {
                document.getElementById('results').innerHTML = '<p>No results found</p>';
            }
        });
});
