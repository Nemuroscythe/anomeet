from main import app
from main.hello.models.HelloMessage import HelloMessage
from main.hello.service.dto.HelloMessageDTO import HelloMessageDTO
from main.hello.service.dto.HelloMessagesDTO import HelloMessagesDTO


# Ce fichier nous permet de convertir un objet de type entité (lié à une table)
# en objet visible par l'utilisateur sous le patterne DTO (Data Transfer Object)
# L'idée de ce patterne est de filtrer les données que l'on veut pouvoir montrer à l'utilisateur

def convertHelloMessageToDTO(helloMessage):
    return HelloMessageDTO(helloMessage.content)


def convertJSONToHelloMessage(helloMessageJson, id=None):
    app.logger.debug(helloMessageJson)
    content = helloMessageJson["content"]
    helloMessage = HelloMessage(content, id)
    return helloMessage


def convertHelloMessageRowToDTO(helloMessage):
    helloMessage = helloMessage[0]  # Row est une classe de SQLAlchemy qui fonctionne comme un tuple
    return HelloMessagesDTO(helloMessage.id, helloMessage.content)


def convertHelloMessageListToDTO(helloMessages):
    helloMessagesDTO = map(convertHelloMessageRowToDTO, helloMessages)  # appelle la fonction convertHelloMessageToDTO
    # pour chaque élément de la liste helloMessages
    return list(helloMessagesDTO)
