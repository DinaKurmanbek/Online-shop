import requests

url = 'http://127.0.0.1:8000/products/'

# response = requests.get(url)
# response = requests.post(url, data = {'name': "gun",
#                                     'description': "dfjhbdvd",
#                                       'category': 1,
#                                       'price': 110})
#
# # print(response)
# print(response.headers)
#
# print("===================================")
# print(response.text)


url = 'http://127.0.0.1:8000/make_order/'

response = requests.post(url)
print(response.headers)
print("===================================")
print(response.text)