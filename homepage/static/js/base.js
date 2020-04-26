window.onload = function() {navActiveFunction();};


$(document).on("scroll", function(){
    if
  ($(document).scrollTop() > 50)
    {
      $("#sticky_top_block").addClass("shrink_small");
      $("#sticky_top_block").removeClass("shrink_big");

      $("#top_portrait").addClass("top_img_small");
      $("#top_portrait").removeClass("top_img_big");
    }
  else
    {
        $("#sticky_top_block").addClass("shrink_big");
        $("#sticky_top_block").removeClass("shrink_small");

        $("#top_portrait").addClass("top_img_big");
        $("#top_portrait").removeClass("top_img_small");
    }
});

function navActiveFunction() {
    // toggle active item in navbar
    current = window.location.href;
    current_site = current.split("/").reverse()[1];
    if (current_site != "index") {
    document.getElementById("nav_".concat(current_site)).classList.add("active");
    document.getElementById("nav_home").classList.remove("active");
    }
}