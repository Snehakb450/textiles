function validate() {

    lstatus = 1;

    fname=document.getElementById("fname")
    dob=document.getElementById("dob")
    address=document.getElementById("adrs")
    mobile=document.getElementById("userMobile")
    email = document.getElementById("userEmail");
    password = document.getElementById("userPassword"); 
    cpassword=document.getElementById("cnfPassword")
    

    if (fname.value == "") {
        fname.style.borderColor = "#FF0000";

        lstatus = 0;

    } else {

        fname.style.borderColor = "#ced4da"

        lstatus = 1;

    }

    if (dob.value == "") {
        dob.style.borderColor = "#FF0000"; lstatus = 0;

    } else {

        dob.style.borderColor = "#ced4da";

        lstatus = 1;

    }

    if (address.value == "") {
        address.style.borderColor = "#FF0000"; lstatus = 0;

    } else {

        address.style.borderColor = "#ced4da";

        lstatus = 1;

    }

     // validate mobile number

     var phoneformat = /^\d{10}$/;

     phone = document.getElementById("userMobile");
 
     if (phone.value.match(phoneformat)) {
         phone.style.borderColor = "#ced4da";
 
     } else {
 
         phone.style.borderColor = "#FF0000";
         signinstatus = 0;
 
     }
 
     // Validate mail valid or not
 
     var mailformat = /^[a-zA-Z0-9. !#$%&* +/=?^_` {|}~~]+@[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)$/;
 
     mail = document.getElementById("userEmail")
     if (mail.value.match(mailformat)) {
         mail.style.borderColor = "#ced4da";
 
     } else {
 
         mail.style.borderColor = "#FF0000";
         signinstatus = 0;
 
     }
 
     // validate password is entered or not
 
     password = document.getElementById("userPassword");
     cnfpassword = document.getElementById("cnfPassword");
     document.getElementById("pswerror").innerHTML = ""
 
     if (password.value == "") {
         password.style.borderColor = "#FF0000";
         signinstatus = 0;
 
     } else {
 
         password.style.borderColor = "#ced4da";
 
     }
     if (password.value != cnfpassword.value) {
 
         signinstatus = 0;
 
         document.getElementById("pswerror").innerHTML = "password and confirm password mismatch";
         cnfpassword.style.borderColor = "#FF0000";
 
     } else {
 
         cnfpassword.style.borderColor = "#ced4da";
 
     }
    
   
    if (lstatus == 0) {

        return false;

    }
}
