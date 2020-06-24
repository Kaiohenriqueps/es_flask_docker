# TESTES UNITÁRIOS
Entrar no container com as portas liberadas e rodar o pytest
```
$ docker-compose run -p 8888:80 -p 5000:5000 --rm --entrypoint bash web_tests
$ pytest
```

# SUBINDO OS SERVIÇOS
Subir com o comando
```
$ docker-compose up
```
| service | port |
| ----- | ----- |
| flask | 5000 |
| elasticsearch | 9200 |
| locust | 8989 |

# INDEXANDO OS DOCS
Fazer uma requisição POST no endereço:
```
localhost:5000/index_doc/<nome_do_index>
```

# BUSCANDO OS DOCS
Fazer uma requisição GET no endereço, passando a query no body da requisição:
```
localhost:5000/search/<nome_do_index>
```
Exemplo de query:
```
{"query": {"match": {"nome": "Kaio"}}}
```

# EXECUTANDO TESTE DE PERFORMANCE
```
$ locust -f perfomance_test/locust_script.py –H http://127.0.0.1:5000
```