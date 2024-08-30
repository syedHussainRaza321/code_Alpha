const apiKey = 'YOUR_API_KEY'; // Replace with your Alpha Vantage API key

const addStockForm = document.getElementById('add-stock-form');
const stockList = document.getElementById('stock-list');

addStockForm.addEventListener('submit', (event) => {
    event.preventDefault();

    const stockSymbol = document.getElementById('stock-symbol').value;

    fetch(`https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol=${stockSymbol}&apikey=${apiKey}`)
        .then(response => response.json())
        .then(data => {
            const stockPrice = data['Global Quote']['05. price'];
            const listItem = document.createElement('li');
            listItem.textContent = `${stockSymbol} - ${stockPrice}`;
            stockList.appendChild(listItem);
        })
        .catch(error => console.error(error));
});