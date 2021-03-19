$(function () {
    var isSuccess; // 是否登陆成功（上一次）
    var isPrevent = true; // 是否阻止提交按钮默认行为

    $("#submit").on('click', function (e) {
        isSuccess = $('body').attr("data-flag");
        if (isSuccess === "False") {
            if (isPrevent) {
                e.preventDefault();
                $("#submit").addClass("disabled");
            }
            $('#error_psw01').html(
                "<svg class='icon' aria-hidden='true'>" +
                "<use xlink:href='#icon-chahao'></use>" +
                "</svg>" +
                "用户名密码输入错误"
            );
        }
    })
    $("#submit").triggerHandler("click");

    $('#btn_modify').click(function (e) {
        isSuccess = $('body').attr("data-flag");
        if (isSuccess === "False") {
            $('#error_psw01').html(
                "<svg class='icon' aria-hidden='true'>" +
                "<use xlink:href='#icon-chahao'></use>" +
                "</svg>" +
                "修改密码失败！"
            );
        }
    });

    $(".entering").focus(function () {
        isPrevent = false;
        $('#submit').removeClass('disabled');
    });
})