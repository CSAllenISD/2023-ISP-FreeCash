const arrayOfStocks = (function () {
    var stocks = [];

    // Temporary add stock
    const apple = new Stock('Apple Inc.', 'AAPL', 'Buy', '+10%');
    apple.setFeatured(true);
    stocks.push(apple);
    const google = new Stock('Alphabet Inc.', 'GOOGL', 'Buy', '+10%');
    google.setFeatured(true);
    stocks.push(google);
    const microsoft = new Stock('Microsoft Corporation', 'MSFT', 'Strong Buy', '+10%');
    microsoft.setFeatured(true);
    stocks.push(microsoft);
    const amazon = new Stock('Amazon.com Inc.', 'AMZN', 'Strong Buy', '+10%');
    amazon.setTrending(true);
    stocks.push(amazon);

    return stocks;
})();

const arrayOfFeatured = arrayOfStocks.filter(stock => stock.isFeatured);
const arrayOfTrending = arrayOfStocks.filter(stock => stock.isTrending);
const arrayOfRisky = arrayOfStocks.filter(stock => stock.isRisky);

function chooseFeatured(int) {
    const lowestIndex = Math.min(arrayOfFeatured.length,int);
    const featuredStocks = arrayOfFeatured.sort(() => 0.5 - Math.random()).slice(0, lowestIndex);
    for (let i = 0; i < lowestIndex; i++) {
        featuredStocks[i].addToFeaturedIndex(i);
    }
}

function chooseTrending(int) {
    const lowestIndex = Math.min(arrayOfTrending.length,int);
    const trendingStocks = arrayOfTrending.sort(() => 0.5 - Math.random()).slice(0, lowestIndex);
    for (let i = 0; i < lowestIndex; i++) {
        trendingStocks[i].addToTrendingIndex(i);
    }
}

function chooseRisky(int) {
    const lowestIndex = Math.min(arrayOfRisky.length,int);
    const riskyStocks = arrayOfRisky.sort(() => 0.5 - Math.random()).slice(0, lowestIndex);
    for (let i = 0; i < lowestIndex; i++) {
        riskyStocks[i].addToRiskyIndex(i);
    }
}


window.addEventListener("DOMContentLoaded", (event) => {

    // Collapse responsive navbar when toggler is visible
    const navbarToggler = document.querySelector(".navbar-toggler");
    const navbarCollapse = document.querySelector(".navbar-collapse");

    navbarToggler.addEventListener("click", () => {
        navbarCollapse.classList.toggle("show");
    });

    // Add stocks to fsections
    chooseFeatured(3);
    chooseTrending(5);
    chooseRisky(5);

    console.log(arrayOfFeatured)
});
