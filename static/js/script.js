// Navbar shadow on scroll

window.addEventListener("scroll", function(){

let navbar = document.querySelector(".navbar");

if(window.scrollY > 20){
navbar.classList.add("shadow");
}else{
navbar.classList.remove("shadow");
}

});


// Simple alert for demo buttons

function showAlert(){

alert("Feature coming soon!");

}