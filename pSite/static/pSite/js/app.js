$(document).ready(function() {

  $('.buy').on('click', function(event) {
    var id = event.currentTarget.dataset.id;
    var locStr = '/' + id + '/charge/';
    window.location = locStr;
  });
});


$(window).bind("load", function() {
   $('#content').show();
});
