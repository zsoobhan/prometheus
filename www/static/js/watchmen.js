$('#footer-js').on('click', function() {
  gtag('event', 'click', {'event_category': 'footer', 'event_label': 'source-code'});
});

$('#contact-js').on('click', function() {
  gtag('event', 'click', {'event_category': 'contact', 'event_label': $(this).data('target')});
});

$('#resume-js').on('click', function() {
  gtag('event', 'click', {'event_category': 'page', 'event_label': $(this).data('target')});
});

$('#resume-landing-js').on('click', function() {
  gtag('event', 'click', {'event_category': 'page', 'event_label': $(this).data('target')});
});

$('#source-js').on('click', function() {
  gtag('event', 'click', {'event_category': 'menu', 'event_label': $(this).data('target')});
});

$('.social-icon').on('click', function() {
  gtag('event', 'click', {'event_category': 'social', 'event_label': $(this).data('target')});
});

$('.button').on('click', function() {
  gtag('event', 'click', {'event_category': 'button', 'event_label': $(this).data('target')});
});
