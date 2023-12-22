$(document).ready(function() {
    $('#reg').click(function() {
        // Замініть URL на посилання, на яке ви хочете перейти
        var externalSiteUrl = "{% static 'pages/SignUp.html' %}";

        // Перенаправлення на інший сайт
        window.location.href = externalSiteUrl;
    });
});
