let timeout = null;

$('#aceita_publica').change(function () {
    if (this.checked) {
        $('#div-temas').addClass('hidden');
        $('#div-categoria').removeClass('hidden');
    } else {
        $('#div-temas').removeClass('hidden');
        $('#div-categoria').addClass('hidden');
    }

});

$('.element_for_read').on('mouseover', function(){
    element = this;
    timeout = setTimeout(function(){send_text(element);} , 1000);
})

$('.element_for_read').on('mouseout', function(){   
    clearTimeout(timeout);
})

function send_text(element){

    let viewElement = $(element).contents()
    let text = encodeURI(viewElement[0]['data'])

    if($('#sound-button').children().hasClass('glyphicon-volume-up')){
        $.ajax({
            url: "./../../readText/" ,
            async: true,
            type: "get",
            datatype: "html",
            data: { text: text },
            success: function(response){
                    console.log("requisição ocorreu com sucesso");
            },
            error: function(xhr, ajaxOptions, thrownError){
                // alert('Houve algum erro ao chamar a API de conversão de audio, gentileza tentar novamente.');
                console.log(xhr.status);
                console.logxhr(thrownError);
            }
        });
    }
}


$('#sound-button').on('click', function(){

    if ($(this).children().hasClass('glyphicon-volume-up')){
        $('.glyphicon-volume-up').removeClass('glyphicon-volume-up').addClass('glyphicon-volume-off');
    } else {
        $('.glyphicon-volume-off').removeClass('glyphicon-volume-off').addClass('glyphicon-volume-up');
    }
});

function checkAnswer(correctAnswer, ElementAnswer, CheckBox){

    let userAnswer = document.getElementById(ElementAnswer).value;
    console.log(userAnswer)
    console.log(correctAnswer)

    if (userAnswer == correctAnswer){
        document.getElementById(CheckBox).checked  = true;
    }
    else{
        document.getElementById(CheckBox).checked  = false;
    }

}