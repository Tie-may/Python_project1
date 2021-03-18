$(function () {
    var isSuccess = true;
    $("#submit").click(function (e) {
        if (!isSuccess) {
            e.preventDefault();
            alert('输入的用户名或密码有误')
        }
    });
    $("#btn_modify").click(function (e) {
        if (!isSuccess) {
            e.preventDefault();
            alert('输入的用户名或密码有误')
        }
    });
})