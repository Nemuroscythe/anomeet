from main.hello.repository import helloRepository
from main.hello.service.helloMapper import convertHelloMessageToDTO


# Ce fichier contient notre logique et manipulations de données
def getHelloMessage():
    hello_message = helloRepository.getHelloMessage()
    return convertHelloMessageToDTO(hello_message).content
