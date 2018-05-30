from flask import Flask, jsonify, request
from flask_restful import Resource, Api, reqparse
from text_sum import summary

app = Flask(__name__)
api = Api(app)


class SummaryApp(Resource):

    def get(self):
        return {'name': 'hello world'}

    def post(self):
    	data = dict(request.form)
    	raw_data = data['text'][0]
 
    	summ = summary(raw_data)
    	return jsonify({'text': summ})


class Statistics(Resource):

    def post(self):
    	data = dict(request.form)
    	raw_data = data['text'][0]
    	count = len(raw_data.split(' '))
 
    	stats = {'count': count}
    	return jsonify(stats)


api.add_resource(SummaryApp, '/')
api.add_resource(Statistics, '/stats')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
