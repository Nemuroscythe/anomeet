function sendMessage()
{
    var msg = document.getElementById("textinput").value;
    if(msg.length <= 512 && msg.length != 0)
    {
        var xhttp = new XMLHttpRequest();
        xhttp.onreadystatechange = function()
        {
            if (this.readyState == 4 && this.status == 200)
            {
                if(this.responseText == 0)
                {
                    console.log("message bien envoyé !");
                }
                else
                {
                    console.error("erreur d'envoi du message");
                    window.alert(this.responseText);
                }
            }
        };
        xhttp.open("POST", "msgSent", true);
        xhttp.send(msg);
    }
}

document.getElementById("sendbutton").addEventListener("click", sendMessage);
