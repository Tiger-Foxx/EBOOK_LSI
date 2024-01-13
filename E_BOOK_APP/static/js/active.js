(function ($) {
  "use strict";
  $(document).on("ready", function () {
    $(".menu").slicknav({
      prependTo: ".mobile-nav",
      duration: 300,
      animateIn: "fadeIn",
      animateOut: "fadeOut",
      closeOnClick: true,
    });

    jQuery(window).on("scroll", function () {
      if ($(this).scrollTop() > 200) {
        $(".header").addClass("sticky");
      } else {
        $(".header").removeClass("sticky");
      }
    });

    $(".top-search a").on("click", function () {
      $(".search-top").toggleClass("active");
    });

    $(function () {
      $("#slider-range").slider({
        range: true,
        min: 0,
        max: 500,
        values: [120, 250],
        slide: function (event, ui) {
          $("#amount").val("$" + ui.values[0] + " - $" + ui.values[1]);
        },
      });
      $("#amount").val(
        "$" +
          $("#slider-range").slider("values", 0) +
          " - $" +
          $("#slider-range").slider("values", 1)
      );
    });

    $(".home-slider").owlCarousel({
      items: 1,
      autoplay: true,
      autoplayTimeout: 5000,
      smartSpeed: 400,
      animateIn: "fadeIn",
      animateOut: "fadeOut",
      autoplayHoverPause: true,
      loop: true,
      nav: true,
      merge: true,
      dots: false,
      navText: [
        '<i class="ti-angle-left"></i>',
        '<i class="ti-angle-right"></i>',
      ],
      responsive: {
        0: {
          items: 1,
        },
        300: {
          items: 1,
        },
        480: {
          items: 2,
        },
        768: {
          items: 3,
        },
        1170: {
          items: 4,
        },
      },
    });

    $(".popular-slider").owlCarousel({
      items: 1,
      autoplay: true,
      autoplayTimeout: 5000,
      smartSpeed: 400,
      animateIn: "fadeIn",
      animateOut: "fadeOut",
      autoplayHoverPause: true,
      loop: true,
      nav: true,
      merge: true,
      dots: false,
      navText: [
        '<i class="ti-angle-left"></i>',
        '<i class="ti-angle-right"></i>',
      ],
      responsive: {
        0: {
          items: 1,
        },
        300: {
          items: 1,
        },
        480: {
          items: 2,
        },
        768: {
          items: 3,
        },
        1170: {
          items: 4,
        },
      },
    });

    $(".quickview-slider-active").owlCarousel({
      items: 1,
      autoplay: true,
      autoplayTimeout: 5000,
      smartSpeed: 400,
      autoplayHoverPause: true,
      nav: true,
      loop: true,
      merge: true,
      dots: false,
      navText: [
        '<i class=" ti-arrow-left"></i>',
        '<i class=" ti-arrow-right"></i>',
      ],
    });

    $(".home-slider-4").owlCarousel({
      items: 1,
      autoplay: true,
      autoplayTimeout: 5000,
      smartSpeed: 400,
      autoplayHoverPause: true,
      nav: true,
      loop: true,
      merge: true,
      dots: false,
      navText: [
        '<i class=" ti-arrow-left"></i>',
        '<i class=" ti-arrow-right"></i>',
      ],
    });

    $("[data-countdown]").each(function () {
      var $this = $(this),
        finalDate = $(this).data("countdown");
      $this.countdown(finalDate, function (event) {
        $this.html(
          event.strftime(
            '<div class="cdown"><span class="days"><strong>%-D</strong><p>Days.</p></span></div><div class="cdown"><span class="hour"><strong> %-H</strong><p>Hours.</p></span></div> <div class="cdown"><span class="minutes"><strong>%M</strong> <p>MINUTES.</p></span></div><div class="cdown"><span class="second"><strong> %S</strong><p>SECONDS.</p></span></div>'
          )
        );
      });
    });

    (function ($) {
      "use strict";
      $(".flexslider-thumbnails").flexslider({
        animation: "slide",
        controlNav: "thumbnails",
      });
    })(jQuery);

    var CartPlusMinus = $(".cart-plus-minus");
    CartPlusMinus.prepend('<div class="dec qtybutton">-</div>');
    CartPlusMinus.append('<div class="inc qtybutton">+</div>');
    $(".qtybutton").on("click", function () {
      var $button = $(this);
      var oldValue = $button.parent().find("input").val();
      if ($button.text() === "+") {
        var newVal = parseFloat(oldValue) + 1;
      } else {
        if (oldValue > 0) {
          var newVal = parseFloat(oldValue) - 1;
        } else {
          newVal = 1;
        }
      }
      $button.parent().find("input").val(newVal);
    });

    $(".scroll").on("click", function (e) {
      var anchor = $(this);
      $("html, body")
        .stop()
        .animate(
          {
            scrollTop: $(anchor.attr("href")).offset().top - 0,
          },
          900
        );
      e.preventDefault();
    });

    $('input[type="checkbox"]').change(function () {
      if ($(this).is(":checked")) {
        $(this).parent("label").addClass("checked");
      } else {
        $(this).parent("label").removeClass("checked");
      }
    });

    $(".qty-box .quantity-right-plus").on("click", function () {
      var $qty = $(".qty-box .input-number");
      var currentVal = parseInt($qty.val(), 10);
      if (!isNaN(currentVal)) {
        $qty.val(currentVal + 1);
      }
    });
    $(".qty-box .quantity-left-minus").on("click", function () {
      var $qty = $(".qty-box .input-number");
      var currentVal = parseInt($qty.val(), 10);
      if (!isNaN(currentVal) && currentVal > 1) {
        $qty.val(currentVal - 1);
      }
    });

    $(".video-popup").magnificPopup({
      type: "iframe",
      removalDelay: 300,
      mainClass: "mfp-fade",
    });

    $.scrollUp({
      scrollText: '<span><i class="fa fa-angle-up"></i></span>',
      easingType: "easeInOutExpo",
      scrollSpeed: 900,
      animation: "fade",
    });
  });

  $("select").niceSelect();

  $(function () {
    $("#slider-range").slider({
      range: true,
      min: 0,
      max: 500,
      values: [0, 500],
      slide: function (event, ui) {
        $("#amount").val("$" + ui.values[0] + " - $" + ui.values[1]);
      },
    });
    $("#amount").val(
      "$" +
        $("#slider-range").slider("values", 0) +
        " - $" +
        $("#slider-range").slider("values", 1)
    );
  });

  $(".preloader").delay(2000).fadeOut("slow");
  setTimeout(function () {
    $("body").removeClass("no-scroll");
  }, 2000);
})(jQuery);
