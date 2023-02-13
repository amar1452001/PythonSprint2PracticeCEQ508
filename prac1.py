"""
HTTP_METHOD    API_ENDPOINT                         DESCRIPTION

GET            /customers                          Get a list of customers.
GET            /customer/<customer_id>             Get a single customer.
POST           /customer




"""






import requests

response = requests.get("https://jsonplaceholder.typicode.com/todos/1")
print(response)

print(response.json())
print(response.headers)


