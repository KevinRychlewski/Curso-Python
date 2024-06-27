# JSON - (javascript object notation)
import json
with open('usuarios1.json',encoding='utf-8') as arquivo_json:
    data = json.load(arquivo_json) # converter arquivo JSON -> string
    print(data['nome'])
with open('usuarios.2json', encoding='utf-8') as arquivo_json:
    data = json.load(arquivo_json)
    print(data["permissões"][1])
    
with open('usuarios2.json',encoding='utf-8') as arquivo_json:
    data = json.load(arquivo_json)
    print(data["usuários"[0]["telefone"]])