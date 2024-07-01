// JavaScript for fetching and displaying movie data

// Example of fetching movie data and populating the table
document.addEventListener('DOMContentLoaded', function() {
    fetch('/api/movies') // Replace with your actual API endpoint
        .then(response => response.json())
        .then(data => {
            const tableBody = document.querySelector('#movie-table tbody');
            tableBody.innerHTML = ''; // Clear existing rows
            data.forEach(movie => {
                const row = document.createElement('tr');
                row.innerHTML = `
                    <td>${movie.title}</td>
                    <td>${movie.director}</td>
                    <td>${movie.year}</td>
                `;
                tableBody.appendChild(row);
            });
        })
        .catch(error => console.error('Error fetching movies:', error));
});
