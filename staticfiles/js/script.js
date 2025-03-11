let open_btn = document.getElementById("open_btn")
let side_bar = document.getElementById("sidebar")
let side = document.getElementById("side")
let close_btn = document.getElementById("close_btn")
let close_it = document.getElementById("close_it")
let filter = document.getElementById("filter")

const activePage = window.location.pathname;
// const navlinks = document.querySelectorAll('.nav1').forEach(link => {
//     if (link.href.includes(`${activePage}`)) {
//         // console.log(`${activePage}`);
//         link.classList.add('text-lime-300')
//     }
// });

console.log(activePage);
console.log("Here")

open_btn.addEventListener("click", function () {

    side_bar.classList.remove("hidden")

})

close_btn.addEventListener("click", function () {

    side_bar.classList.add("hidden")

})

close_it.addEventListener("click", function () {

    side.classList.add("hidden")

})

filter.addEventListener("click", function () {

    side.classList.remove("hidden")

})

