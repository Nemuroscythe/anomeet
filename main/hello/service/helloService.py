from main.hello.repository import helloRepository
from main.hello.service import helloMapper


# Ce fichier contient notre logique et manipulations de données
def getHelloMessage():
    helloMessage = helloRepository.getHelloMessage()
    return helloMapper.convertHelloMessageToDTO(helloMessage)


def createHelloMessage(helloMessageJson):
    helloMessage = helloMapper.convertJSONToHelloMessage(helloMessageJson)
    helloRepository.createHelloMessage(helloMessage)
    return helloMapper.convertHelloMessageToDTO(helloMessage)