/**
 * Created by Daniil Neverov on 23.05.17.
 */

$(document).ready(function(e) {

    $('.course').hover( function(){
        var background = $( this ).attr('data-background');
        $( this ).css( "background-image", "url("+background+")" ) ;
        $( this ).css( "color", "white" ) ;
        $(this).find('.calendar-icon').attr('src', '/wp-content/themes/sovarchivetechno/img/calendar.png');
        $(this).find('.time-icon').attr('src', '/wp-content/themes/sovarchivetechno/img/time.png');
        $(this).find('button').removeClass('btn-default').addClass('btn-info');

        if ($(this).closest('.program-block').find('.bullet-list').is(":hidden")){
            $(this).find('.arrow').attr('src', '/wp-content/themes/sovarchivetechno/img/arrow-down.png');
        } else{
            $(this).find('.arrow').attr('src', '/wp-content/themes/sovarchivetechno/img/arrow.png');
        }
    }, function(){
        $( this ).css( "background-image", "none" ) ;
        $( this ).css( "color", "black" ) ;
        $(this).find('.calendar-icon').attr('src', '/wp-content/themes/sovarchivetechno/img/calendar-dark.png');
        $(this).find('.time-icon').attr('src', '/wp-content/themes/sovarchivetechno/img/time-dark.png');
        $(this).find('button').removeClass('btn-info').addClass('btn-default');

        if ($(this).closest('.program-block').find('.bullet-list').is(":hidden")){
            $(this).find('.arrow').attr('src', '/wp-content/themes/sovarchivetechno/img/arrow-dark-down.png');
        } else{
            $(this).find('.arrow').attr('src', '/wp-content/themes/sovarchivetechno/img/arrow-dark.png');
        }
    } );

    $( ".course" ).click(function () {
        var list = $(this).closest('.program-block').find('.bullet-list');
        if (list.is( ":hidden" ) ) {
            list.slideDown( "slow" );
            $(this).find('.arrow').attr('src', '/wp-content/themes/sovarchivetechno/img/arrow.png');
        } else {
            list.hide();
            $(this).find('.arrow').attr('src', '/wp-content/themes/sovarchivetechno/img/arrow-down.png');
        }
    });

    $('#formCallForm').submit(function (event) {
        event.preventDefault;
        var data = $('#formCallForm').serialize();
        $.ajax({
            type: "POST",
            url: "form-submit.php",
            data: data,
            success: function(msg){
                console.log( msg );
            }
        });
        $('#formCall').modal('hide');
        return false;
    });

    $('#formCoursesForm').submit(function (event) {
        event.preventDefault;     
        var data = $('#formCoursesForm').serialize();
        $.ajax({
            type: "POST",
            url: "form-submit.php",
            data: data,
            success: function(msg){
                console.log( msg );
            }
        });
        $('#formCourses').modal('hide');
        return false;
    });

    $('#formProgramsForm').submit(function (event) {
        event.preventDefault;
        var data = $('#formProgramsForm').serialize();
        $.ajax({
            type: "POST",
            url: "form-submit.php",
            data: data,
            success: function(msg){
                console.log( msg );
            }
        });
        $('#formPrograms').modal('hide');
        return false;
    });
    
    $('#questionsForm').submit(function (event) {
        event.preventDefault;
        var data = $('#questionsForm').serialize();
        $.ajax({
            type: "POST",
            url: "form-submit.php",
            data: data,
            success: function(msg){
               $('#questionsForm').find("input, textarea").val("");
                console.log( msg );
            }
        });
        return false;
    });

    $('#formCall, #formCourses, #formPrograms').on('show.bs.modal', function (event) {
        var button = $(event.relatedTarget); // Button that triggered the modal
        var formName = button.data('name'); // Extract info from data-* attributes
        
        // If necessary, you could initiate an AJAX request here (and then do the updating in a callback).
        // Update the modal's content. We'll use jQuery here, but you could use a data binding library or other methods instead.
        var modal = $(this);
        modal.find('.modal-body input[name="formName"]').val(formName);
    });

    $('input, textarea').focusout(function() {
        if ($(this).val() !== ''){
            $(this).next('label').addClass('focused-label');
        } else {
            $(this).next('label').removeClass('focused-label');
        }
    });
    
    $('.new-block').click(function(){
        var href = $(this).find('a').attr('href');
        window.location = href;
    });
});
