var share = window.share || {};

share.facebookShareButton = {

    listenForEvent: function () {
        'use_strict';
        $("#fb-share-link-js").click(function (e){
            e.preventDefault();
            share.facebookShareButton.pushGAEvent($(this).data('target'));
            share.facebookShareButton.openShareWindow(); 
        });
    },


    pushGAEvent: function(slug){
        'use_strict';
        ga('send', 'event', 'blog', 'click', slug);
    },


    openShareWindow: function(){
        'use_strict';
        window.open('https://www.facebook.com/sharer/sharer.php?u='
                    + encodeURIComponent(document.URL)
                    + '&t='
                    + encodeURIComponent(document.URL));
        return false;
    }
        
}

share.facebookShareButton.listenForEvent();


