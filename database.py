import sqlite3

class Database():
    def __init__(self, name):
        self.conn = sqlite3.connect(name + '.db')
        self.conn.execute('CREATE TABLE IF NOT EXISTS note (id INTEGER PRIMARY KEY, title TEXT,content TEXT NOT NULL );')
        self.conn.commit()


    def add(self,note):
        self.conn.execute(f"INSERT INTO note (title, content) VALUES ('{note.title}', '{note.content}');")
        self.conn.commit()

    def get_all(self):
        cursor = self.conn.execute("SELECT id, title, content FROM note")
        l = []
        for linha in cursor:
            id = linha[0]
            title = linha[1]
            content = linha[2]
            nota = Note(id,title,content)
            l.append(nota)
        return l
    
    def update(self,entry):
        
        self.conn.execute(f'UPDATE note SET title = "{entry.title}", content = "{entry.content}" WHERE id = "{entry.id}"')
        self.conn.commit()
    def delete(self,note_id):
        self.conn.execute(f"DELETE FROM note WHERE id = '{note_id}';")
        self.conn.commit()
from dataclasses import dataclass

@dataclass
class Note:
    id: int = None
    title: str = None
    content: str = ''
