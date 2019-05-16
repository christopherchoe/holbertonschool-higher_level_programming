$(function () {
  $.ajax({
    url: 'https://swapi.co/api/people/5/?format=json',
    success: function (character) {
      $('#character').append(character.name);
    }
  });
});
