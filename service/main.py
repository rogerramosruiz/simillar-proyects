from fastapi import FastAPI, File, UploadFile, Form
from fastapi.staticfiles import StaticFiles

import uvicorn
import shutil
from utilities import random_file_name, get_similar_files
from env import PUBLIC_DIR
from db.operations import insert, select_one_by_proyect, select_one_by_name
from db.init import create_tables
app = FastAPI()

app.mount("/public", StaticFiles(directory=PUBLIC_DIR), name="public")

@app.post('/uploadfile')
async def upload_file(file: UploadFile, id_proyect: int= Form(0)):
    ext = file.filename.split('.')[-1]
    full_file_name, file_name = random_file_name()
    file_name = f'{file_name}.{ext}'
    full_file_name = f'{full_file_name}.{ext}'
    with open(f'{full_file_name}', 'wb') as f:
        shutil.copyfileobj(file.file, f)    
    insert(filename=file_name, id_proyect=id_proyect)
    print(type(id_proyect))
    return {'filename':file_name}

@app.get("/similarfile/{id_proyect}")
def similarfile(id_proyect):
    pdf_file = select_one_by_proyect(id_proyect=id_proyect)[0]
    similar_names = get_similar_files(pdf_file)
    if len(similar_names) == 0:
        return {'Mesage':'Not found'}, 404
    
    response = {}
    for i in range(len(similar_names)):
        name = similar_names[i]
        id_proyect_similar = select_one_by_name(name)[0]
        print(id_proyect_similar)
        response[id_proyect_similar] = name
    return response



if __name__ == '__main__':
    create_tables()
    uvicorn.run("main:app", host = '0.0.0.0', port = 8080, reload = True)
