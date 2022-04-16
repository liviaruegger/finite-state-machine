from fastapi import FastAPI, Response, status
import uvicorn

from mef import MEF, TransicaoIndisponivel


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


mef = MEF()


@app.get("/")
def home(response: Response):
    try:
        estado_atual = mef.listar_estado_atual()
        resposta = {
            "Mensagem": "MEF iniciada com sucesso",
            "Estado atual": estado_atual
        }
    except AttributeError:
        response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        resposta = {
            "Mensagem": "erro na inicialização da MEF"
        }
    except IndexError:
        response.status_code = status.HTTP_404_NOT_FOUND
        resposta = {
            "Mensagem": "MEF não possui estados definidos"
        }

    return resposta


@app.get("/estado")
def listar_estado_atual():
    return {
        "Estado atual": mef.listar_estado_atual()
    }


@app.post("/estado")
def novo_estado(transicao: str, response: Response):
    try:
        novo_estado = mef.atualizar_estado(transicao)
        return {
            "Novo estado": novo_estado
        }
    except TransicaoIndisponivel:
        response.status_code = status.HTTP_405_METHOD_NOT_ALLOWED
        return {
            "Erro": "transição indisponível"
        }


@app.get("/transicoes")
def listar_transicoes():
    return {
        "Transições possíveis": mef.listar_transicoes_possiveis()
    }


if __name__ == "__main__":
    uvicorn.run("main:app", port=5000, reload=True)