# Criando uma Api utilizando Flask

O arquivo 'Criando_Modelo_ML.ipynb' contém:
* Uma breve análise em um conjunto de dados sobre propriedades para venda e aluguel na cidade de São Paulo
* Criação de um modelo de Machine Learning para prever o preço de um imóvel
* Persistência do modelo em um arquivo novo utilizando a biblioteca Joblib

O arquivo 'app.py' contém:
* Criação de uma aplicação Flask
* Criação da Api

O conjunto de dados original utilizado na análise se encontra em: https://www.kaggle.com/argonalyst/sao-paulo-real-estate-sale-rent-april-2019 .

# Pacotes instalados para a criação da Api

pip install gunicorn\
pip install sklearn\
pip install numpy\
pip install flask\
pip install flask-restful\
pip install joblib


# Comandos utilizados para o deploy da aplicação no Heroku

Criar um arquivo "Procfile"\
Atualizar o Procfile com web: gunicorn app:app\
pip3 freeze > requirements.txt\
git init\
heroku login\
heroku create nomedasuaapp\
git add .\
git commit -m "Text do Commit"\
heroku git:remote -a nomedasuaapp\
git push heroku master


# Testando a API

Endereço da Api: https://apideployapp.herokuapp.com/

Insira o JSON abaixo numa requisição POST

{\
    "Condo": 210,\
    "Size": 65,\
    "Rooms": 3,\
    "Toilets": 2,\
    "Suites": 1,\
    "Parking": 1,\
    "Elevator": 1,\
    "Furnished": 0,\
    "Swimming Pool": 0,\
    "New": 0,\
    "Latitude": -23.543138,\
    "Longitude": -46.479486,\
    "District_Alto de Pinheiros": 0,\
    "District_Anhanguera": 0,\
    "District_Aricanduva": 0,\
    "District_Artur Alvim": 0,\
    "District_Barra Funda": 1,\
    "District_Bela Vista": 0,\
    "District_Bel\u00e9m": 0,\
    "District_Bom Retiro": 0,\
    "District_Brasil\u00e2ndia": 0,\
    "District_Brooklin": 0,\
    "District_Br\u00e1s": 0,\
    "District_Butant\u00e3": 0,\
    "District_Cachoeirinha": 0,\
    "District_Cambuci": 0,\
    "District_Campo Belo": 0,\
    "District_Campo Grande": 0,\
    "District_Campo Limpo": 0,\
    "District_Canga\u00edba": 0,\
    "District_Cap\u00e3o Redondo": 0,\
    "District_Carr\u00e3o": 0,\
    "District_Casa Verde": 0,\
    "District_Cidade Ademar": 0,\
    "District_Cidade Dutra": 0,\
    "District_Cidade L\u00edder": 0,\
    "District_Cidade Tiradentes": 0,\
    "District_Consola\u00e7\u00e3o": 0,\
    "District_Cursino": 0,\
    "District_Ermelino Matarazzo": 0,\
    "District_Freguesia do \u00d3": 0,\
    "District_Graja\u00fa": 0,\
    "District_Guaianazes": 0,\
    "District_Iguatemi": 0,\
    "District_Ipiranga": 0,\
    "District_Itaim Bibi": 0,\
    "District_Itaim Paulista": 0,\
    "District_Itaquera": 0,\
    "District_Jabaquara": 0,\
    "District_Jaguar\u00e9": 0,\
    "District_Jaragu\u00e1": 0,\
    "District_Jardim Helena": 0,\
    "District_Jardim Paulista": 0,\
    "District_Jardim S\u00e3o Luis": 0,\
    "District_Jardim \u00c2ngela": 0,\
    "District_Ja\u00e7an\u00e3": 0,\
    "District_Jos\u00e9 Bonif\u00e1cio": 0,\
    "District_Lajeado": 0,\
    "District_Lapa": 0,\
    "District_Liberdade": 0,\
    "District_Lim\u00e3o": 0,\
    "District_Mandaqui": 0,\
    "District_Medeiros": 0,\
    "District_Moema": 0,\
    "District_Mooca": 0,\
    "District_Morumbi": 0,\
    "District_Pari": 0,\
    "District_Parque do Carmo": 0,\
    "District_Pedreira": 0,\
    "District_Penha": 0,\
    "District_Perdizes": 0,\
    "District_Perus": 0,\
    "District_Pinheiros": 0,\
    "District_Pirituba": 0,\
    "District_Ponte Rasa": 0,\
    "District_Raposo Tavares": 0,\
    "District_Rep\u00fablica": 0,\
    "District_Rio Pequeno": 0,\
    "District_Sacom\u00e3": 0,\
    "District_Santa Cec\u00edlia": 0,\
    "District_Santana": 0,\
    "District_Santo Amaro": 0,\
    "District_Sapopemba": 0,\
    "District_Sa\u00fade": 0,\
    "District_Socorro": 0,\
    "District_S\u00e3o Domingos": 0,\
    "District_S\u00e3o Lucas": 0,\
    "District_S\u00e3o Mateus": 0,\
    "District_S\u00e3o Miguel": 0,\
    "District_S\u00e3o Rafael": 0,\
    "District_S\u00e9": 0,\
    "District_Tatuap\u00e9": 0,\
    "District_Trememb\u00e9": 0,\
    "District_Tucuruvi": 0,\
    "District_Vila Andrade": 0,\
    "District_Vila Curu\u00e7\u00e1": 0,\
    "District_Vila Formosa": 0,\
    "District_Vila Guilherme": 0,\
    "District_Vila Jacu\u00ed": 0,\
    "District_Vila Leopoldina": 0,\
    "District_Vila Madalena": 0,\
    "District_Vila Maria": 0,\
    "District_Vila Mariana": 0,\
    "District_Vila Matilde": 0,\
    "District_Vila Olimpia": 0,\
    "District_Vila Prudente": 0,\
    "District_Vila S\u00f4nia": 0,\
    "District_\u00c1gua Rasa": 0,\
    "Negotiation Type_rent": 1,\
    "Negotiation Type_sale": 0,\
    "Property Type_apartment": 0\
}