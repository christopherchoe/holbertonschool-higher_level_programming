$(function () {
  $.ajax({
    url: 'https://swapi.co/api/films/?format=json',
    success: function (movies) {
      $.each(movies.results, function (i, movie) {
        $('UL#list_movies').append('<li>' + movie.title + '</li>');
      });
    }
  });
});
