# importando bibliotecas

import numpy as np
from flask import Flask, jsonify, request
from flask_restful import Resource, Api
from joblib import load

# instanciando objetos das classes Flask e Api

app = Flask(__name__)

api = Api(app)

# carregando o modelo

model = load('model/model.joblib')


# criando uma classe com os métodos referentes as requisições GET e POST

class PrecoImoveis(Resource):

    def get(self):
        return {'Nome': 'Henrique Schwab Gelatti'}

    def post(self):
        args = request.get_json(force=True)
        input_values = np.asarray(list(args.values())).reshape(1, -1)
        predict = model.predict(input_values)[0]

        return jsonify({'Previsão': float(predict)})


# adicionando a classe criada na Api

api.add_resource(PrecoImoveis, '/')

# rodando a aplicação Flask

if __name__ == '__main__':
    app.run()
