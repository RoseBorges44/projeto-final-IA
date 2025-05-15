import requests

# Token fixo obtido anteriormente
headers = {"X-API-Key": "b40c86da871865b961d048d747843a6fc7e3699afb91041f92cd4206362d482a"}

# Envio da predição para avaliação
files = {"file": open("C:/Users/rosej/OneDrive/Desktop/UNISENAI/predicoes_final.csv", "rb")}
params = {"threshold": 0.5}

response = requests.post(
    "http://3.138.252.216:5000/evaluate/multilabel_metrics",
    headers=headers,
    files=files,
    params=params
)

# Exibir o resultado
print(response.status_code)
print(response.json())



