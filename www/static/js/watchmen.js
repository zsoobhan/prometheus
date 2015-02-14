$('#footer-js').on('click', function() {
  ga('send', 'event', 'footer', 'click', 'source-code');
});

$('#contact-js').on('click', function() {
  ga('send', 'event', 'contact', 'click', $(this).data('target'));
});

$('.social-icon').on('click', function() {
  ga('send', 'event', 'social', 'click', $(this).data('target'));
});

$('#source-code-button-js').on('click', function() {
  ga('send', 'event', 'infrastructure', 'click', 'source-code');
});
