// Assuming you have a backend API to fetch news data
const API_URL = "http://localhost:8000/api/v1/noticias"; // Replace with your actual API endpoint

// Fetch news articles from the API
function fetchNews() {
    fetch(API_URL)
        .then(response => response.json())
        .then(data => {
            // Handle successful response
            displayNews(data);
        })
        .catch(error => {
            // Handle API error or other exceptions
            console.error("Error fetching news:", error);
            // You might display an error message to the user here
        });
}

// Display news articles in the list
function displayNews(newsData) {
    const newsList = document.getElementById('news-items');
    newsList.innerHTML = ''; // Clear existing list items

    newsData.forEach(article => {
        const newsItem = document.createElement('li');
        const newsLink = document.createElement('a');
        const newsTitle = document.createElement('h3');
        const newsSummary = document.createElement('p');

        newsLink.href = article.url; // Replace with actual article URL property
        newsTitle.textContent = article.title;
        newsSummary.textContent = article.summary; // Assuming you have a summary property

        newsLink.appendChild(newsTitle);
        newsLink.appendChild(newsSummary);
        newsItem.appendChild(newsLink);
        newsList.appendChild(newsItem);
    });
}

// Search functionality (implementation depends on your chosen search method)
function handleSearch() {
    const searchInput = document.getElementById('search-input');
    const searchTerm = searchInput.value.toLowerCase();

    // Filter news data based on searchTerm
    const filteredNews = newsData.filter(article => {
        // Implement your filtering logic here
        // You might check title, summary, or other relevant fields
        return article.title.toLowerCase().includes(searchTerm) ||
               article.summary.toLowerCase().includes(searchTerm);
    });

    // Update the displayed news list
    displayNews(filteredNews);
}

// Event listener for search input and button
document.getElementById('search-input').addEventListener('input', handleSearch);
document.getElementById('search-btn').addEventListener('click', handleSearch);

// Add event listener to the button
document.getElementById('create-news-btn').addEventListener('click', function() {
    // Redirect to crearnoticia.html using JavaScript
    window.location.href = 'crearnoticia.html';
});

// Initial fetch and display of news on page load
fetchNews();