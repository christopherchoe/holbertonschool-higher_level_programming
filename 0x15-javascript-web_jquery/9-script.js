$(function () {
  let helloUrl = 'https://fourtonfish.com/hellosalut/?lang=' + $('html')[0].lang;
  $.ajax({
    url: helloUrl,
    success: function (greeting) {
      $('DIV#hello').text(greeting.hello);
    }
  });
});
