

// main page's jQurey

$(document).ready(function(){
    $('div.hidden').fadeIn(1000).removeClass('hidden');

    $('.col-lg-3').hover(
        // trigger when mouse hover
        function(){
            $(this).animate({
                marginTop: "-=1%",
            },200);
        },

        // trigger when mouse out
        function(){
            $(this).animate({
                marginTop: "0%"
            },200);
        }
    );
});