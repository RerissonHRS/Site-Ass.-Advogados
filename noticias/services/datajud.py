import requests

BASE_URL = "https://datajud.cnj.jus.br/api_publica_teste/api/v1/"

TRIBUNAIS_PR = [
    "TJPR",
    "TRF4",
    "TRE-PR",
    "TRT9"
]

def buscar_processos_parana(limite=10):
    processos = []

    for tribunal in TRIBUNAIS_PR:
        url = f"{BASE_URL}processos?codigoTribunal={tribunal}&page=1&pageSize={limite}"

        try:
            response = requests.get(url, timeout=10)

            if response.status_code == 200:
                dados = response.json()
                processos.extend(dados.get("data", []))
            else:
                print(f"Erro {response.status_code} no tribunal {tribunal}")

        except Exception as e:
            print(f"Erro ao consultar API para {tribunal}: {e}")

    return processos
