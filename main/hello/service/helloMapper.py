from main.hello.service.dto.HelloMessageDTO import HelloMessageDTO
from main.hello.models.HelloMessage import HelloMessage


# Ce fichier nous permet de convertir un objet de type entité (lié à une table)
# en objet visible par l'utilisateur sous le patterne DTO (Data Transfer Object)
# L'idée de ce patterne est de filtrer les données que l'on veut pouvoir montrer à l'utilisateur

def convertHelloMessageToDTO(helloMessage):
    return HelloMessageDTO(helloMessage.content)


def convertJSONToHelloMessage(helloMessageJson):
    return HelloMessage(helloMessageJson["content"])