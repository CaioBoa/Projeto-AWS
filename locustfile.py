from locust import HttpUser, task, between

class WebsiteUser(HttpUser):
    wait_time = between(1, 5)  

    @task(1)
    def create_item(self):
        headers = {'Content-Type': 'application/json'}
        data = {"YourPrimaryKey": "1", "name": "teste"}
        self.client.post("create_item", json=data, headers=headers)

    @task(2) 
    def get_item(self):
        self.client.get("get_item/1") 

    @task(1)
    def get_all_items(self):
        self.client.get("get_all_items")