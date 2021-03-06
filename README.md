# Teste para desenvolvedor Amo Promo

### Getting Started

```
# Endpoint para buscar recomendações de voo

http://127.0.0.1:5000/api/search/<iata_origin>/<iata_destiny>/<departure_date>/<return_date>
```

Exemplo   | Tipo   | Descrição
--------- | ------ | --------
iata_origin | string | IATA de Origem.
iata_destiny | string | IATA de Destino.
departure_date | string | Data de ida. Formato: **YYYY-MM-DD**
return_date | string | Data de volta. Formato: **YYYY-MM-DD**

### Pré-requisitos

Antes de começar, você vai precisar ter instalado em sua máquina as seguintes ferramentas:
[Git](https://git-scm.com/) e [Python 3.9](https://www.python.org/downloads/)

### Rodando Back-End

```bash
# Clone este repositório
$ git clone https://github.com/yurilimak9/amo-promo-test.git

# Acesse a pasta do projeto no terminal/cmd
$ cd amo-promo-test

# Crie um ambiente virtual 
$ python -m venv venv

# Ative o ambiente virtual 
$ source venv/bin/activate

# instale as dependências
$ pip install -r requirements.txt

# Crie um arquivo .env na raiz do projeto tomando como 
# exemplo o arquivo .env-example e adicione suas credencias

# Execute a aplicação
$ python app.py

# O servidor inciará na porta:5000 - acesse <http://127.0.0.1:5000>
```

### Tecnologias

- [Python](https://python.org/)
- [Flask](https://flask.palletsprojects.com/en/2.0.x/)
- [Requests](https://docs.python-requests.org/en/latest/)
- [Pydantic](https://pydantic-docs.helpmanual.io/)
- [Python-dotenv](https://pypi.org/project/python-dotenv/)

### Autor

[Yuri Gonçalves Lima](https://github.com/yurilimak9)