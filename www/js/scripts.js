const arrayOfStocks = (function () {
    var stocks = [];

    // Temporary add stock
    const apple = new Stock('Apple Inc.', 'AAPL', 'Buy', '+10%');
    apple.setFeatured = true;
    stocks.push(apple);
    const google = new Stock('Alphabet Inc.', 'GOOGL', 'Buy', '+10%');
    google.setFeatured = true;
    stocks.push(google);
    const microsoft = new Stock('Microsoft Corporation', 'MSFT', 'Strong Buy', '+10%');
    microsoft.setFeatured = true;
    stocks.push(microsoft);
    const amazon = new Stock('Amazon.com Inc.', 'AMZN', 'Strong Buy', '+10%');
    amazon.setTrending = true;
    stocks.push(amazon);

    return stocks;
})();

const arrayOfFeatured = arrayOfStocks.filter(stock => stock.isFeatured);
const arrayOfTrending = arrayOfStocks.filter(stock => stock.isTrending);
const arrayOfRisky = arrayOfStocks.filter(stock => stock.isRisky);

window.addEventListener("DOMContentLoaded", (event) => {

    // Collapse responsive navbar when toggler is visible
    const navbarToggler = document.querySelector(".navbar-toggler");
    const navbarCollapse = document.querySelector(".navbar-collapse");

    navbarToggler.addEventListener("click", () => {
        navbarCollapse.classList.toggle("show");
    });

    // Add stocks to featured section
    arrayOfStocks[0].addToFeaturedIndex(0);
    arrayOfStocks[1].addToFeaturedIndex(1);
    arrayOfStocks[2].addToFeaturedIndex(2);

    arrayOfStocks[0].addTo(document.getElementById('trending'));
    arrayOfStocks[0].addTo(document.getElementById('risky'));

});
