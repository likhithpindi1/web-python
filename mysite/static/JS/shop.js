
var when_click_basket = document.querySelector(".add-button");
var to_open_basket = document.querySelector(".back_black");
var to_close =document.querySelector(".to_close_basket");
var to_close_it = document.querySelector(".back_black")





when_click_basket.addEventListener("click", open_basket);
to_close.addEventListener("click", close_basket);
to_close_it.addEventListener("click",close_basket)
function open_basket()
{

    to_open_basket.classList.remove("to_hide")


}
function close_basket()
{

    to_open_basket.classList.add("to_hide")
}