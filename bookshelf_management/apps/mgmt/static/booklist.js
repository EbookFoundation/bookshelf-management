(function ($) {

  let list

  try{
    list = JSON.parse(localStorage.getItem('booklist'))
  }catch (e){
    list = {}
  }


  $('.bookshelf-entry').each( function() {
    const bookId = $(this).attr('id').split('-')[1]

    if(list[bookId]){
      console.log(bookId)
      $(this).append('<div class="in-booklist"></div>')
    }
    else {
      $(this).append('<div class="out-booklist"></div>')
    }
  })

  const queryString = window.location.search;
  const urlParams = new URLSearchParams(queryString);

  if(urlParams.has('addId')){
    // console.log(urlParams.get('addId'))
    $('#id_bookid').val(urlParams.get('addId'))

  }

  if(urlParams.has('addTitle')){
    // console.log(urlParams.get('addId'))
    $('#add-title').html('Adding book: ' + urlParams.get('addTitle'))

  }

})(jQuery)