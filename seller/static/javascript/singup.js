function signup_validate() {

    lstatus = 1;

    companyname=document.getElementById("resellercompanyname")
    companyid=document.getElementById("resellercompanyid")
    address=document.getElementById("adrs")
    mobile=document.getElementById("userMobile")
    email = document.getElementById("userEmail");
    accountname = document.getElementById("Rbankname"); 
    accountnumber=document.getElementById("Rbanknumber")
    accountifsc=document.getElementById("Raccountifsc")

    if (companyname.value == "") {
        companyname.style.borderColor = "#FF0000";

        lstatus = 0;

    } else {

        companyname.style.borderColor = "#ced4da"

        lstatus = 1;

    }

    if (companyid.value == "") {
        companyid.style.borderColor = "#FF0000"; lstatus = 0;

    } else {

        companyid.style.borderColor = "#ced4da";

        lstatus = 1;

    }

    if (address.value == "") {
        address.style.borderColor = "#FF0000"; lstatus = 0;

    } else {

        address.style.borderColor = "#ced4da";

        lstatus = 1;

    }
    if (mobile.value == "") {
        mobile.style.borderColor = "#FF0000"; lstatus = 0;

    } else {

        mobile.style.borderColor = "#ced4da";

        lstatus = 1;

    }
    if (email.value == "") {
        email.style.borderColor = "#FF0000"; lstatus = 0;

    } else {

        email.style.borderColor = "#ced4da";

        lstatus = 1;

    }
    if (accountname.value == "") {
        accountname.style.borderColor = "#FF0000"; lstatus = 0;

    } else {

        accountname.style.borderColor = "#ced4da";

        lstatus = 1;

    }
    if (accountnumber.value == "") {
        accountnumber.style.borderColor = "#FF0000"; lstatus = 0;

    } else {

        accountnumber.style.borderColor = "#ced4da";

        lstatus = 1;

    }
    if (accountifsc.value == "") {
        accountifsc.style.borderColor = "#FF0000"; lstatus = 0;

    } else {

        accountifsc.style.borderColor = "#ced4da";

        lstatus = 1;

    }
   
    if (lstatus == 0) {

        return false;

    }
}
