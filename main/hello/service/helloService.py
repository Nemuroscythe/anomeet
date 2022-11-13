from main.hello.repository import helloRepository
from main.hello.service import helloMapper


# Ce fichier contient notre logique et manipulations de données
def getHelloMessages():
    helloMessage = helloRepository.getHelloMessages()
    return helloMapper.convertHelloMessageListToDTO(helloMessage)


def getHelloMessage(id):
    helloMessage = helloRepository.getHelloMessage(id)
    return helloMapper.convertHelloMessageToDTO(helloMessage)


def createHelloMessage(helloMessageJson):
    helloMessage = helloMapper.convertJSONToHelloMessage(helloMessageJson)
    helloRepository.createHelloMessage(helloMessage)
    return helloMapper.convertHelloMessageToDTO(helloMessage)


def updateHelloMessage(id, helloMessageJson):
    helloMessage = helloMapper.convertJSONToHelloMessage(helloMessageJson, id)
    helloRepository.updateHelloMessage(helloMessage)
    return None


def deleteHelloMessage(id):
    helloRepository.deleteHelloMessage(id)
    return None
