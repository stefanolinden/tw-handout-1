def extract_route(request):
    l = request.split()
    for i in l:
        if i.startswith('/'):
            return i[1:]
            
        
    
        
def read_file(Path):
    arquivo = open(Path, 'rb').read()
    return arquivo

    
