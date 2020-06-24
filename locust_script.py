from locust import TaskSet, task, HttpUser, between

class ESCrudTasks(TaskSet):
    @task
    def index_document(self):
        self.client.post("/index_doc/teste", '{"person_name": "Kaio", "age": 26}')

    @task
    def search_document(self):
        self.client.get("/search/teste/Kaio")


class ApiUser(HttpUser):
    task_set = ESCrudTasks
    wait_time = between(5, 15)