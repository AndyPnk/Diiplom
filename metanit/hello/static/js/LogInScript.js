// Function using jQuery to show/hide registration forms based on user type
function showRegistrationForm() {
    var userType = $("#userType").val();

    if (userType === "customer") {
        $("#customerRegistrationForm").show(speed='fast');
        $("#logisticianRegistrationForm").hide(speed='fast');  
    } else if (userType === "logistician") {
        $("#customerRegistrationForm").hide(speed='fast');
        $("#logisticianRegistrationForm").show(speed='fast');  
    }
}

// Function using jQuery to check password match
function checkPasswordMatch() {
    var password = $("#password").val();
    var confirmPassword = $("#confirmPassword").val();
    var message = $("#passwordMatchMessage");

    if (password === confirmPassword) {
        message.html("Паролі співпадають").css("color", "green");
    } else {
        message.html("Паролі не співпадають").css("color", "red");
    }
}

(document).ready(function() {
    $('#userType').change(function() {
        var selectedOption = $(this).val();

        if (selectedOption === 'customer') {
            $('#logisticianRegistrationForm').hide();
        } else if (selectedOption === 'logistician') {
            $('#customerRegistrationForm').hide();
        }
    });
});
