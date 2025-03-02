function validate() {
    var email = document.getElementById("email").value;
    var At = false;
    var Dot = false;
    var AtPos = -1;
    
    for (var i = 0; i < email.length; i++) {
        if (email[i] == "@" && i != 0) { 
            At = true;
            AtPos = i;
        }
        if (At == true && email[i] == "." && i - AtPos > 1 && i != email.length - 1) {
            Dot = true;
        }
        if (At == true && Dot == true) {
            document.getElementById("result").innerText = "Valid email";
        }
        else {
            document.getElementById("result").innerText = "Invalid email";
        }
    }
    
}
