// Select  DOM Items

// const addBtn = document.querySelector(".add-btn");
// const formBtn = document.querySelector(".form-btn");
//
// const todoText = document.querySelector(".to-do-text");
//
// // Set Initial State of Footer
// let showForm = true;
// let showAdd = true;
//
// addBtn.addEventListener('click', toggle1);
// formBtn.addEventListener('click', toggle2);
//
// function toggle1(){
//     if(showAdd){
//         addBtn.classList.remove('show');
//         addBtn.classList.add('hide');
//         todoText.classList.remove('hide');
//         todoText.classList.add('show');
//
//         // Set Form State
//         showForm = true;
//     }
// }
//
// function toggle2(){
//     if(showForm){
//         todoText.classList.remove('show');
//         todoText.classList.add('hide');
//         addBtn.classList.remove('hide');
//         addBtn.classList.add('show');
//
//         // Set Form State
//         showAdd = true;
//     }
// }

// ---------------
//----------------------------------------------------------------------------------------------------------------------
//
// const appWindow = document.querySelector(".myApp");
// const appTitle = document.querySelector(".app-title");
// const appParent = document.querySelector(".app-parent");
//
// let sticky = appTitle.offsetTop;
// let appOffset = appWindow.offsetTop;
//
// appWindow.onscroll = function() {stickerFunction()};
//
// function stickerFunction(){
//     // if(appOffset > sticky){
//         appTitle.classList.add("stick");
//         appParent.classList.add("stick-parent");
//     // }else{
//     //     appTitle.classList.remove("stick");
//
//     // console.log("Hey! I am scrolling.")
//     // console.log(sticky);
// }
setTimeout(function () {
    $('#message').fadeOut('slow');
}, 3000);
