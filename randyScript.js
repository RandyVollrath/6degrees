function userArtist()
{
  var input = document.getElementById("artist").value;
  console.log('hit here');
  $.ajax(
  {
    url: "http://localhost:5000/",
    data: {artist:input},
    success: function(data) {
      $("#response").text(data);
    },
    error: function(data) {
      $("#response").text("no mutual songs in common");
    }
  })

}
