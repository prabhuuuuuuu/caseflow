let isScrolling;
let canScroll = true;

// Track active section during scrolling
document.addEventListener('scroll', () => {
    const sections = document.querySelectorAll('section');
    const navLinks = document.querySelectorAll('nav ul li a');

    let currentSection = '';

    sections.forEach(section => {
        const sectionTop = section.offsetTop;
        const sectionHeight = section.clientHeight;
        if (pageYOffset >= sectionTop - 50 && pageYOffset < sectionTop + sectionHeight - 50) {
            currentSection = section.getAttribute('id');
        }
    });

    navLinks.forEach(link => {
        link.classList.remove('active');
        if (link.getAttribute('href').includes(currentSection)) {
            link.classList.add('active');
        }
    });
});

// Handle navbar link clicks
document.querySelectorAll('nav a').forEach(link => {
    link.addEventListener('click', (e) => {
        const href = link.getAttribute('href');
        
        // If it's a page link (login/signup), let the default navigation happen
        if (href.includes('.html')) {
            return;
        }
        
        // For section links, handle smooth scrolling
        e.preventDefault();
        const targetSection = document.querySelector(href);
        if (targetSection) {
            targetSection.scrollIntoView({ behavior: 'smooth' });
        }
    });
});



//Law script.js
let slideIndex = 0;
const slides = document.querySelectorAll('.slide');
const totalSlides = slides.length;

function showSlides() {
    for (let i = 0; i < totalSlides; i++) {
        slides[i].style.display = 'none';
    }
    slideIndex++;
    if (slideIndex > totalSlides) { slideIndex = 1; }
    slides[slideIndex - 1].style.display = 'block';
    setTimeout(showSlides, 3000); // Change slide every 3 seconds
}

function moveSlide(n) {
    slideIndex += n;
    if (slideIndex > totalSlides) { slideIndex = 1; }
    if (slideIndex < 1) { slideIndex = totalSlides; }
    showSlides();
}

document.addEventListener('DOMContentLoaded', (event) => {
    showSlides();
});
