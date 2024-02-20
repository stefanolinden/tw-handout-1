import json

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
        
            
    
    
    

    
