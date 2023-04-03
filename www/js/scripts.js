window.addEventListener("DOMContentLoaded", (event) => {

    // Collapse responsive navbar when toggler is visible
    const navbarToggler = document.querySelector(".navbar-toggler");
    const navbarCollapse = document.querySelector(".navbar-collapse");

    navbarToggler.addEventListener("click", () => {
        navbarCollapse.classList.toggle("show");
    });

});
