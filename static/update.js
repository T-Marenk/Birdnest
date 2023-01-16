$(document).ready(function() {
     
    const interval = setInterval(function() {
        
        req = $.ajax({
            url : '/update',
            type : 'POST'
        });

        req.done(function(data) {
            $('#violatorslist').html(data);
        });

    }, 1000);

});
