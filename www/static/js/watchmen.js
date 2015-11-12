$('#footer-js').on('click', function() {
  ga('send', 'event', 'footer', 'click', 'source-code');
});

$('#contact-js').on('click', function() {
  ga('send', 'event', 'contact', 'click', $(this).data('target'));
});

$('#resume-js').on('click', function() {
  ga('send', 'event', 'menu', 'click', $(this).data('target'));
});

$('.social-icon').on('click', function() {
  ga('send', 'event', 'social', 'click', $(this).data('target'));
});

$('.button').on('click', function() {
  ga('send', 'event', 'button', 'click', $(this).data('target'));
});
