from .connection import connection

def select():
    with connection() as (cur, _):
        cur.execute(f'SELECT * FROM file')
        description = cur.description
        data = cur.fetchall()
        return data, description
    
def insert(filename, id_proyect):
    with connection() as (cur, conn):
        cur.execute("INSERT INTO file(filename, id_proyect) VALUES(%s, %s) RETURNING id",  (filename, id_proyect))
        id = cur.fetchone()[0]
        conn.commit()
        return id
    
def select_one_by_proyect(id_proyect):
    with connection() as (cur, _):
        cur.execute('SELECT filename FROM file WHERE id_proyect=%s', (id_proyect,))
        data = cur.fetchone()
        return data
    
def select_one_by_name(filename):
    with connection() as (cur, _):
        cur.execute('SELECT id_proyect FROM file WHERE filename=%s', (filename,))
        data = cur.fetchone()
        return data

    