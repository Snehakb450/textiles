function validate_login() {

    lstatus = 1;

    username = document.getElementById("Username");

    password = document.getElementById("Password"); 

    if (username.value == "") {
        username.style.borderColor = "#FF0000";

        lstatus = 0;

    } else {

        username.style.borderColor = "#ced4da"

        lstatus = 1;

    }

    if (password.value == "") {
        password.style.borderColor = "#FF0000"; lstatus = 0;

    } else {

        password.style.borderColor = "#ced4da";

        lstatus = 1;

    }

   
    if (lstatus == 0) {

        return false;

    }
}