import ssl
from elasticsearch import Elasticsearch
from elasticsearch.connection import create_ssl_context


def connect_es():
    return Elasticsearch(
        hosts=["elasticsearch:9200"]
    )

def index_doc(es, index, doc):
    return es.index(index=index, body=doc, doc_type="_doc")

def search_doc(es, index, query):
    return es.search(index=index, body={
        "query": {
            "multi_match": {
                "query": query,
                "fields": "*"
            }
        }
    })
