let message_timeout = document.getElementById("message-timer");

let add = document.getElementById("add-button")
let success = document.querySelector(".toast-success")
let closeBtn = document.getElementById("close-button")


add.addEventListener('click', function 
    () {
    success.classList.remove("hidden")
})

closeBtn.addEventListener('click', function 
    () {
    success.classList.add("hidden")
})


setTimeout(() => {

    message_timeout.style.display = "none";

}, 5000);