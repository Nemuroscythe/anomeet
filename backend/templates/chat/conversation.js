//////////////////////////////////////////////////////////////////////////////////
function sendMessage() {
    var msg = document.getElementById("textinput").value;
    if (msg.length <= 512 && msg.length != 0) {
        var xhttp = new XMLHttpRequest();
        xhttp.onreadystatechange = function () {
            if (this.readyState == 4 && this.status == 200) {
                if (this.responseText == 0) {
                    console.log("message bien envoyé !");
                } else {
                    console.error(this.responseText);
                }
            }
        };
        xhttp.open("POST", "msgSent", true);
        xhttp.send(JSON.stringify(msg));
    }
}

document.getElementById("sendbutton").addEventListener("click", sendMessage);
//////////////////////////////////////////////////////////////////////////////////

/*
TODO : recupérer le cookie qui spécifie l'id de l'utilisateur
TODO : recupérer l'id de la conversation dans l'url
*/


// Check le cookie et si pas de cookie redirige vers le login
var id_user = "cookie..."
if (id_user == ""){window.location.href = "login"};

//////////////////////////////////////////////////////////////////////////////////

// SetInterval
function retrieveMsg() {

    //Faire le JSON {id_user:..., id_conversation:...}

    var xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200){
            // Function pour traiter la reception des messages
        }
    }
    xhttp.open("POST", "getMsg", true);
    xhttp.send(/*JSON a faire*/);
}

setInterval(retrieveMsg, 1000);



///////////////////////////////////////////////////////////////////////////////////////
Fonctions du w3school pour la gestion des cookies
//////////////////////////////////////////////////////////////////////////////////////

function setCookie(cname, cvalue, exdays) {
  const d = new Date();
  d.setTime(d.getTime() + (exdays * 24 * 60 * 60 * 1000));
  let expires = "expires="+d.toUTCString();
  document.cookie = cname + "=" + cvalue + ";" + expires + ";path=/";
}

function getCookie(cname) {
  let name = cname + "=";
  let ca = document.cookie.split(';');
  for(let i = 0; i < ca.length; i++) {
    let c = ca[i];
    while (c.charAt(0) == ' ') {
      c = c.substring(1);
    }
    if (c.indexOf(name) == 0) {
      return c.substring(name.length, c.length);
    }
  }
  return "";
}

function checkCookie() {
  let user = getCookie("username");
  if (user != "") {
    alert("Welcome again " + user);
  } else {
    user = prompt("Please enter your name:", "");
    if (user != "" && user != null) {
      setCookie("username", user, 365);
    }
  }
}