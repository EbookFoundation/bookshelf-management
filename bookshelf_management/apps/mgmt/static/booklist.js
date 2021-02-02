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

})(jQuery)