from src.lib import crud_es


def test_search_document():
    es = crud_es.connect_es()
    crud_es.index_doc(
        es, "teste", {"name": "Henrique", "age": 26})
    search = crud_es.search_doc(
        es, "teste", "Henrique")
    assert search.get('hits').get('total').get('value') != 0


def test_index_document():
    es = crud_es.connect_es()
    insert_response = crud_es.index_doc(
        es, "teste", {"name": "Kaio", "age": 26})
    assert insert_response['result'] == 'created'
