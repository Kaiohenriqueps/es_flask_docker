import logging
from lib import crud_es
from json import loads
from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/index_doc/<string:my_index>", methods=["POST"])
def index_doc(my_index: str):
    es = crud_es.connect_es()
    data = loads(request.data)
    response_index = crud_es.index_doc(es, my_index, data)
    return response_index, 200


@app.route("/search/<string:my_index>/<string:query>", methods=["GET"])
def search_doc(my_index: str, query: str):
    es = crud_es.connect_es()
    response_search = crud_es.search_doc(
        es=es, index=my_index, query=query)
    return response_search, 200


if __name__ == '__main__':
    app.run(host='0.0.0.0')
