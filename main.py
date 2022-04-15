# Para rodar: uvicorn main:app --reload

from fastapi import FastAPI
import uvicorn

from mef import Estado, Transicao, MEF


description = """
Implementação de uma máquina de estados finitos em Python.
"""

app = FastAPI(
    title="Máquina de Estados Finitos (Aplicação 2)",
    description=description,
    contact={
        "name": "Ana Lívia Ruegger Saldanha",
        "url": "https://github.com/liviaruegger",
        "email": "analiviaruegger@gmail.com",
    },
)