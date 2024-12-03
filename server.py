from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

class Curso(BaseModel):
    id: int
    titulo: str
    descricao: str
    duracao: int

cursos = []

@app.get("/")
def get_api():
    return "Bem-Vindo a API"

@app.get("/cursos")
def get_cursos():
    return cursos

@app.post("/cursos")
def add_cursos(curso : Curso):
    cursos.append(curso)
    return curso

@app.put("/cursos/{curso_id}")
def update_curso(curso_id: int, curso: Curso):
    for i, c in enumerate(cursos):
        if c.id == curso_id:
            cursos[i] = curso
            return curso
    raise HTTPException(status_code=404, detail="Curso não encontrado")

@app.delete("/cursos/{curso_id}")
def delete_curso(curso_id: int):
    for i, c in enumerate(cursos):
        if c.id == curso_id:
            cursos.pop(i)
            return {"message": "Curso deletado"}
    raise HTTPException(status_code=404, detail="Curso não encontrado")