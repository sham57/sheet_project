const date = new Date();
document.querySelector('.year').innerHTML = date.getFullYear();
setTimeout(function(){
  $('#hide').fadeOut('slow');
},2000)
