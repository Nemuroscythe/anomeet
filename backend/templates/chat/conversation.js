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
                    console.error("message non envoyé!");
                }
            }
        };
        xhttp.open("POST", "msgSent", true);
        xhttp.send(JSON.stringify(msg));
    }
}

document.getElementById("sendbutton").addEventListener("click", sendMessage);
//////////////////////////////////////////////////////////////////////////////////
// Check le cookie et si pas de cookie redirige vers le login
var id_user = "user_id";
if (id_user == ""){window.location.href = "login"};
// Check l'id de la conversation
var url = window.location.href;
var urlArray = url.split("/");
var id_conversation = urlArray[urlArray.length -1];
var isOK = true;
if (id_conversation == "conversation"){isOK = false}

//////////////////////////////////////////////////////////////////////////////////
// SetInterval
//Faire le JSON {id_user:..., id_conversation:...}
var conversationInfo = {"id_user":id_user, "id_conversation":id_conversation}

function retrieveMsg() {

    var xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200){
            // Function pour traiter la reception des messages.
            loadMsg(this.responseText);
        }
    }
    xhttp.open("POST", "getMsg", true);
    if (isOK) {
        xhttp.send(JSON.stringify(conversationInfo));
    }
}

setInterval(retrieveMsg, 1000);


function loadMsg(listOfMessages){
    listOfMessages = JSON.parse(listOfMessages);
    var buffer = "";
    for(var i=0; i<listOfMessages.length; i++){
        //listOfMessage[i][0]:id_user
        //listOfMessage[i][1]:id_message
        //listOfMessage[i][2]:message
        //listOfMessage[i][3]:date
        var canvas = " <div>Contenu </div>"
        canvas.replace("Contenu",listOfMessages[i][2]);
        buffer = buffer + canvas;
    }
    document.getElementById("flow").innerHTML=buffer;
}
//var tabConversation = JSON.parse(this);

///////////////////////////////////////////////////////////////////////////////////////
// Fonctions du w3school pour la gestion des cookies
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
///////////////////////////////////////////////////////////////////////////////////////////