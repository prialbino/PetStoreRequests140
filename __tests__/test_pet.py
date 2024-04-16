# 1 - bibliotecas
import pytest  #engine / framework de teste de unidade  
import requests   # framework de teste de API
import json       # leitor e escritor do json

from utils.utils import ler_csv    #importar a funcao de leitura do csv

# 2 - classes (optional no python)

# 2.1 - atributos ou variaveis 
# consulta e resultado esperado
pet_id = 21768             #id do animal  
pet_name = "Duna"          #nome do animal
pet_category_id = 1
pet_category_name = "dog" 
pet_tag_id = 1             #codigo do rotulo
pet_tag_name = "vacinado"  #titulo do rotulo

# informacoes em comum
url = 'https://petstore.swagger.io/v2/pet'      #endereco
headers= {'Content-Type': 'application/json'}   # formato dos dados trafegados

# 2.2 - funcoes / metodos
def test_post_pet():
    # configura
    # dados de entrada que estao no arq json
    pet = open('./fixtures/json/pet1.json')    # abre o arq json
    data = json.loads(pet.read())        # le o conteudo e carrega como json em uma variavel data
    #resultado esperado estao nos atributos acima das funcoes

    # executa
    response = requests.post(    #executa o metodo post com todas as info a seguir
        url=url,                 #endereco
        headers=headers,         #cabecalho
        data=json.dumps(data),   #msg = json
        timeout=5                #tempo limite da transmissao
    )

    response_body = response.json()   # cria uma variavel e carrega a resposta em formato json

    # valida
    assert response.status_code == 200
    assert response_body['id'] == pet_id
    assert response_body['name'] == pet_name
    assert response_body['category']['name'] == pet_category_name
    assert response_body['tags'][0]['name'] == pet_tag_name

def test_get_pet():
    response = requests.get(
        url=f'{url}/{pet_id}',   #chama o endereco do get;consulta passando o id do animal
        headers=headers
        #nao tem body;corpo da msg
    )

    response_body = response.json()
    assert response.status_code == 200 
    assert response_body['name'] == pet_name
    assert response_body['category']['id'] == pet_category_id
    assert response_body['tags'][0]['id'] == pet_tag_id
    assert response_body['status'] == 'available'

def test_put_pet():
    #configura
    #dados vem do arq json
    pet = open('./fixtures/json/pet2.json')
    data = json.loads(pet.read())    #ler o arq

    #executa
    response = requests.put(
        url=url,
        headers=headers,
        data=json.dumps(data),   #descarrega os dados
        timeout=5
    )

    #valida
    response_body = response.json()

    assert response.status_code == 200
    assert response_body['id'] == pet_id
    assert response_body['name'] == pet_name
    assert response_body['category']['id'] == pet_category_id
    assert response_body['category']['name'] == pet_category_name
    assert response_body['tags'][0]['id'] == pet_tag_id
    assert response_body['tags'][0]['name'] == pet_tag_name 
    assert response_body['status'] == 'sold'

def test_delete_pet():
    response = requests.delete(
        url=f'{url}/{pet_id}',
        headers=headers
    )
    response_body = response.json()
    assert response.status_code == 200
    assert response_body['code'] == 200
    assert response_body['type'] == 'unknown'
    assert response_body['message'] == str(pet_id)
    

#criamos as colunas
@pytest.mark.parametrize('pet_id,category_id,category_name,pet_name,tags,status',
                         ler_csv('./fixtures/csv/pets.csv')
                         )
#criamos as variaveis para receber as colunas
def test_post_pet_dinamico(pet_id,category_id,category_name,pet_name,tags,status):
    #configura
    pet = {}    # cria uma lista vazia chamada pet
    pet['id'] = int(pet_id)  # nesse caso [] sao as posicoes dos dados 
    pet['category'] = {}
    pet['category']['id'] = int(category_id)
    pet['category']['name'] = category_name
    pet['name'] = pet_name
    pet['photoUrls'] = []
    pet['photoUrls'].append('')  #append seriam os filhos de photourls
    pet['tags'] = []  

    tags = tags.split(';')
    for tag in tags:
        tag = tag.split('-')
        tag_formatada = {}
        tag_formatada['id'] = int(tag[0])
        tag_formatada['name'] = tag[1]
        pet['tags'].append(tag_formatada)   #cria e formatad a tags
    
    pet['status'] = status

    pet = json.dumps(obj=pet, indent=4) #formata o arq em json pulando linha
    print('\n' + pet) #visualiza como ficou criado o json dinamicamente

    #executa
    response = requests.post(
        url=url,
        headers=headers,
        data=pet,
        timeout=5
    )
    response_body = response.json()
    assert response.status_code == 200
    assert response_body['id'] == int(pet_id) 
    assert response_body['name'] == pet_name
    assert response_body['status'] == status

