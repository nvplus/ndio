function clearcomments() {
    $('.ndio-comments').html("");
}

function vote_yes(yes, no) {
    var options = $(event.target).closest('.poll-options');

    options.html("<br>You voted Yes<br><br>Yes's: " + (yes + 1) + " | No's: " + no);
    options.css('margin-top', "14px");
}

function vote_no(yes, no) {
    var options = $(event.target).closest('.poll-options');

    options.html("<br>You voted No<br><br>Yes's: " + yes + " | No's: " + (no + 1));
    options.css('margin-top', "14px");
}

$(document).ready(function () {
    /* POLLING */

    /*
     * Depracated poll create function
     *
    $(".poll-create").click(function() {
        var poll = prompt("Enter your yes/no question: ");
        var html = ` 
        <div class="poll">
        <div class="poll-title">${poll} (1 day left)</div>
        <div class="poll-options">
            <img class="poll-option poll-yes clickable" src="../images/ndio-yes.png">
            <div class="poll-divider"></div>
            <img class="poll-option poll-no clickable" src="../images/ndio-no.png">
        </div>
        <div class="poll-footer">
            <div class="poll-open-comments clickable">
                <img class="poll-comment-image" src="../images/ndio-comment.png">
                View comments
            </div>
        </div>
        </div>`

        $('.ndio-home-container').prepend(html);
    });
    */

    $('.poll-open-comments').click(function() {
        $('.ndio-home-container').hide();
        clearcomments();

       var num = Math.floor((Math.random() * 10) + 1);

       for (var i = 0; i < num; i++) {
            var n = i+1;
            $('.ndio-comments').append("User " + n + ": Comment "+ n + "<br>");
        }

        $('.ndio-comments').show();
    });

    /* PAGE SWITCHING */
    $(".ndio-hf-button").click(function() {
        $('.selected').removeClass('selected');
        $(this).addClass("selected");
    });

    $('.ndio-home').click(function() {
        $('.ndio-comments').hide();
        $('.ndio-search-container').hide();
        $('.ndio-home-container').show();
        $('.ndio-profile-container').hide();
    }); 

    $('.ndio-search').click(function() {
        $('.ndio-comments').hide();
        $('.ndio-search-container').show();
        $('.ndio-home-container').hide();
        $('.ndio-profile-container').hide();
    }); 

    $('.ndio-profile').click(function() {
        $('.ndio-comments').hide();
        $('.ndio-search-container').hide();
        $('.ndio-home-container').hide();
        $('.ndio-profile-container').show();
    }); 
});