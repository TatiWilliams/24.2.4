import requests
status = 'available'
res = requests.get(f'https://petstore.swagger.io/v2/pet/findByStatus?status={status}', headers={'accept':'application/json'})
print(res.status_code)
print(res.text)
print(res.json())
print(type(res.json()))

pet_data = {
    "id": 12345,
    "name": "Max",
    "photoUrls": [
        "string"
    ],
    "tags": [
        {
            "id": 0,
            "name": "string"
        }
    ],
    "status": "available"
}

res_post = requests.post('https://petstore.swagger.io/v2/pet', json=pet_data, headers={'accept': 'application/json', 'Content-Type': 'application/json'})

print(res_post.status_code)
print(res_post.text)
print(res_post.json())
print(type(res_post.json()))
pet_data = {
    "id": 12345,
    "name": "Max",
    "photoUrls": [
        "string"
    ],
    "tags": [
        {
            "id": 0,
            "name": "string"
        }
    ],
    "status": "sold"
}

res_put = requests.put('https://petstore.swagger.io/v2/pet', json=pet_data, headers={'accept': 'application/json', 'Content-Type': 'application/json'})

print(res_put.status_code)
print(res_put.text)
print(res_put.json())
print(type(res_put.json()))

pet_id = 12345  # Замените на реальный ID животного, которое вы хотите удалить

res_delete = requests.delete(f'https://petstore.swagger.io/v2/pet/{pet_id}', headers={'accept': 'application/json'})

print(res_delete.status_code)
print(res_delete.text)
