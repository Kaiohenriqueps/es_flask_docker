from locust import TaskSet, task, HttpLocust, between

class ESCrudTasks(TaskSet):
    @task
    def index_document(self):
        self.client.post("/index_doc/teste", '{"person_name": "Kaio", "age": 26}')

    @task
    def search_document(self):
        self.client.get("/search/teste/Kaio")


class ApiUser(HttpLocust):
    task_set = ESCrudTasks
    wait_time = between(5, 15)