import requests
import json

def getberry(name):
    request = requests.get(f'https://pokeapi.co/api/v2/berry/{name}/')
    response = json.loads(request.content)
    nome = response['firmness']['url']
    print(nome)


#def nomedafuncao2(parametro):
#    requests = requests.get(f"url da requisicao?parametro={parametro}")
#    response = json.loads(requests.content)
#    nome = response[0]['nome']
#    print(nome)


if __name__ == '__main__':
    name = input('inserir o id: ')
    getberry(name)
    #nomedafuncao2("parametro")