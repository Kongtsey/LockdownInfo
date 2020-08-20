(function ($) {
  "use strict";

  var fullHeight = function () {
    $(".js-fullheight").css("height", $(window).height());
    $(window).resize(function () {
      $(".js-fullheight").css("height", $(window).height());
    });
  };
  fullHeight();

  $("#sidebarCollapse").on("click", function () {
    $("#sidebar").toggleClass("active");
  });

  if (window.matchMedia("(max-width: 767px)").matches) {
    // The viewport is less than 768 pixels wide
    alert("This is a tablet or desktop.");
    $(".level-titles").on("click", function () {
      $("#sidebar").toggleClass("active");
    });
  } else {
    // The viewport is at least 768 pixels wide
    alert("This is a tablet or desktop.");
  }
})(jQuery);
