import json
import os

def extract_route(request):
    l = request.split()
    for i in l:
        if i.startswith('/'):
            return i[1:]
            
        
    
        
def read_file(Path):
    arquivo = open(Path, 'rb').read()
    return arquivo

def load_data(nome):
    path = './data/' + nome
    arquivo = open(path, 'r').read()
    data = json.loads(arquivo)   
    return data
        
def load_template(nome):
    path = './templates/' + nome
    with open(path, 'r') as arquivo:
        data = arquivo.read()
    return data

def adiciona_anotacao(params):
    file_path = os.path.join('data', 'notes.json')
    with open(file_path, 'r') as file:
        data = json.load(file)
    data.append(params)
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4,ensure_ascii=False)

def build_response(body='', code=200, reason='OK', headers=''):
    if len(headers) > 0:
        response = f'HTTP/1.1 {code} {reason}\n{headers}\n\n{body}'
    else:
        response = f'HTTP/1.1 {code} {reason}\n\n{body}'

    print(response)
    return response.encode()

        
            
    
    
    

    
