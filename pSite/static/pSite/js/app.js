$(document).ready(function() {

  var quotes = $(".quote");
  var quoteIndex = -1;
  var baseURL = window.location.protocol + "//" + window.location.host + "/";

  function showNextQuote() {
    ++quoteIndex;

    quotes.eq(quoteIndex % quotes.length)
      .fadeIn(2000)
      .delay(10000)
      .fadeOut(2000, showNextQuote);
  }

  $(".logo").on('click', function() {
    window.location = baseURL;
  });

  $('#buy1').on('click', function() {
          window.location = '/1/charge/';
  });

  showNextQuote();
});
