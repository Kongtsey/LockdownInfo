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
    $(".level-titles").on("click", function () {
      $("#sidebar").toggleClass("active");
    });
  }
})(jQuery);
