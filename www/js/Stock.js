class Stock {
    constructor(title, ticker, suggestion, buy) {
        this.title = title;
        this.ticker = ticker;
        this.suggestion = suggestion;
        this.buy = buy;
    }

    createCard() {
        const card = document.createElement('div');
        card.classList.add('card');
        const cardLeft = document.createElement('div');
        cardLeft.classList.add('card-left');
        const cardTitle = document.createElement('h2');
        cardTitle.classList.add('card-title');
        cardTitle.innerText = this.title;
        const cardSubtitle = document.createElement('h5');
        cardSubtitle.classList.add('card-subtitle');
        cardSubtitle.innerText = this.ticker;
        const cardRight = document.createElement('div');
        cardRight.classList.add('card-right');
        const cardRightTitle = document.createElement('h3');
        cardRightTitle.classList.add('card-right-title');
        cardRightTitle.innerText = this.suggestion;
        const cardRightSubtitle = document.createElement('h5');
        cardRightSubtitle.classList.add('card-right-subtitle');
        cardRightSubtitle.innerText = this.buy;

        cardLeft.appendChild(cardTitle);
        cardLeft.appendChild(cardSubtitle);
        cardRight.appendChild(cardRightTitle);
        cardRight.appendChild(cardRightSubtitle);
        card.appendChild(cardLeft);
        card.appendChild(cardRight);

        return card;
    }

    addTo(element) {
        element.appendChild(this.createCard());
    }

    addToFeaturedIndex(index) {
        const featuredElement = document.getElementById('featured');
        if (index > 2) { //guard clause
            console.error('Error: Featured section is already full');
            return;
        }
        const card = this.createCard();
        const nthChild = featuredElement.children[index];
        console.log(nthChild)
        nthChild.replaceChild(card, nthChild.children[0]);
    }
}
