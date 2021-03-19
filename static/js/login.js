$(function () {
    var isSuccess;
    var isPrevent = true;
    $('#submit').click(function (e) {
        isSuccess = $('body').attr("data-flag");
        if (isSuccess === "False") {
            if(isPrevent){
                e.preventDefault();
                $("#submit").addClass("disabled");
            }
            $('#error_psw01').html(
                "<svg class='icon' aria-hidden='true'>" +
                "<use xlink:href='#icon-chahao'></use>" +
                "</svg>" +
                "用户名或密码输入错误"
            );
        }
    });

    $('#btn_modify').click(function (e) {
        isSuccess = $('body').attr("data-flag");
        if (isSuccess === "False") {
            if(isPrevent){
                e.preventDefault();
                $("#btn_modify").addClass('disabled');
            }
            $('#error_psw02').html(
                "<svg class='icon' aria-hidden='true'>" +
                "<use xlink:href='#icon-chahao'></use>" +
                "</svg>" +
                "用户名或密码输入错误"
            );
        }
    });

    $(".entering").focus(function (){
        isPrevent = false;
        $('#submit').removeClass('disabled');
        $('#btn_modify').removeClass('disabled');
    });
})