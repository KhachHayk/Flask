import requests

response = requests.post(
    'http://127.0.0.1:5000/adv/',
    json={"title": "Автомобиль", "description": "TOYOTA 2023 года"},
    headers={"Authorization": "Nik"}
)
print(response.status_code)
print(response.text)

# response = requests.get(
#     'http://127.0.0.1:5000/user_1/',
# )
# print(response.status_code)
# print(response.text)

# response = requests.get(
#     'http://127.0.0.1:5000/user_1/600/',
# )
# print(response.status_code)
# print(response.text)

# response = requests.patch(
#     'http://127.0.0.1:5000/user_1/4/',
#     json={"name": "new_user_2", "password": "000000"}
# )
# print(response.status_code)
# print(response.text)
#
# response = requests.get(
#     'http://127.0.0.1:5000/user_1/1/',
# )
# print(response.status_code)
# print(response.text)


# response = requests.delete(
#     "http://127.0.0.1:5000/user_1/4/",
# )
# print(response.status_code)
# print(response.text)
#
# response = requests.get(
#     "http://127.0.0.1:5000/user_1/4/",
# )
# print(response.status_code)
# print(response.text)