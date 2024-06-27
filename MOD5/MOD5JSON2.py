import json
# criar ou ler JSON existente
computador_json = """{
    "marca": "dell",
    "preço": 15000
}"""
# lendo um string JSON
data = json.loads(computador_json)
print(data["preço"])
# salvar um string JSON -> arquivo JSON
with open('computador.json','w',encoding='utf-8')as arquivo_json:
    json.dump(computador_json,arquivo_json)
# para ler um arquivo JSON
with open('computador.json',encoding='utf-8') as arquivo_json:
    string_computador_json = json.load(arquivo_json) # convertendo JSON -> string
    dicionario_computador_json = json.loads(string_computador_json) # converter de string -> dicionario python
    print(dicionario_computador_json["marca"])
# desafio
computador = """{
    "name": "John Smith",
    "age": 30,
    "city": "new york",
    "isStudente": true,
    "gpa": 3.5
}"""
with open('desafio.json','w',encoding='utf-8') as arquivo_json:
    json.dump(computador,arquivo_json)
    