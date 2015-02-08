$('#footer').on('click', function() {
  ga('send', 'event', 'footer', 'click', 'source-code');
});

$('#github-social').on('click', function() {
  ga('send', 'event', 'social', 'click', 'github');
});

$('#resume-social').on('click', function() {
  ga('send', 'event', 'footer', 'click', 'resume');
});

$('#twitter-social').on('click', function() {
  ga('send', 'event', 'footer', 'click', 'twitter');
});

$('#contact').on('click', function() {
  ga('send', 'event', 'contact', 'click', 'contactform');
});


$('#source-code').on('click', function() {
  ga('send', 'event', 'source-code', 'click', 'infrastructure');
});
