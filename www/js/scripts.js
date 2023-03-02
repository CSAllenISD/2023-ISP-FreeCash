window.addEventListener("DOMContentLoaded", (event) => {

    // Collapse responsive navbar when toggler is visible
    const navbarToggler = document.querySelector(".navbar-toggler");
    const navbarCollapse = document.querySelector(".navbar-collapse");

    navbarToggler.addEventListener("click", () => {
        navbarCollapse.classList.toggle("show");
    });

    // Add cards to the page TEMPORARY FOR COSMETIC PURPOSES
    let trending = document.getElementById("trending");
    let risky = document.getElementById("risky");
    addCardTo(createCard("Palo Alto Networks, Inc", "$PANW", "Buy", "+9.24%"),trending)
    addCardTo(createCard("Palo Alto Networks, Inc", "$PANW", "Buy", "+9.24%"),risky)

    // Change featured card
    
});

function createCard(title, subtitle, rightTitle, rightSubtitle) {
    const card = document.createElement('div');
    card.classList.add('card');
    const cardLeft = document.createElement('div');
    cardLeft.classList.add('card-left');
    const cardTitle = document.createElement('h2');
    cardTitle.classList.add('card-title');
    cardTitle.innerText = title;
    const cardSubtitle = document.createElement('h5');
    cardSubtitle.classList.add('card-subtitle');
    cardSubtitle.innerText = subtitle;
    const cardRight = document.createElement('div');
    cardRight.classList.add('card-right');
    const cardRightTitle = document.createElement('h3');
    cardRightTitle.classList.add('card-right-title');
    cardRightTitle.innerText = rightTitle;
    const cardRightSubtitle = document.createElement('h5');
    cardRightSubtitle.classList.add('card-right-subtitle');
    cardRightSubtitle.innerText = rightSubtitle;

    cardLeft.appendChild(cardTitle);
    cardLeft.appendChild(cardSubtitle);
    cardRight.appendChild(cardRightTitle);
    cardRight.appendChild(cardRightSubtitle);
    card.appendChild(cardLeft);
    card.appendChild(cardRight);

    return card;
}

function addCardTo(card, element) {
    element.appendChild(card);
}

function changeFeaturedCardTo(card, index) {
    const featuredElement = document.getElementById('featured');
    const nthChild = featuredElement.parentNode.children[index];
    featuredElement.parentNode.replaceChild(card, nthChild);
  }
