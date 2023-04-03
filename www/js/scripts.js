const arrayOfStocks = (function() {
    var stocks = [];
  
    // Temporary add stock
    const apple = new Stock('Apple Inc.', 'AAPL', 'Strong Buy', '+10%');
    stocks.push(apple);
    const google = new Stock('Alphabet Inc.', 'GOOGL', 'Buy', '+10%');
    stocks.push(google);
    const microsoft = new Stock('Microsoft Corporation', 'MSFT', 'Strong Buy', '+10%');
    stocks.push(microsoft);
    const amazon = new Stock('Amazon.com Inc.', 'AMZN', 'Strong Buy', '+10%');
    stocks.push(amazon);
  
    return stocks;
  })();

window.addEventListener("DOMContentLoaded", (event) => {

    // Collapse responsive navbar when toggler is visible
    const navbarToggler = document.querySelector(".navbar-toggler");
    const navbarCollapse = document.querySelector(".navbar-collapse");

    navbarToggler.addEventListener("click", () => {
        navbarCollapse.classList.toggle("show");
    });

});
