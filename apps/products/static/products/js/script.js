$(document).ready(function() {
  $('#search-product').click(function() {
    var productId = $('#product-id').val();
    $.ajax({
      url: `/${productId}/show`,
      method: 'GET',
      success: function(data) {
        console.log(data);
        $('#product').html(data[0].fields.name);
      },
      error: function(data) {
        console.log('there was an error');
        console.log(data);
        $('#product').html('PRODUCT NOT FOUND');
      }
    });
  });
});