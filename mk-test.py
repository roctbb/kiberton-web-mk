import requests

HOST = "http://127.0.0.1:2020"

#task 1
response = requests.post(HOST + '/task1')
print(response.text)

#task 2
data = {
    "name": "test"
}
response = requests.post(HOST + '/task2', data=data)
print(response.text)

#task 3
response = requests.request("LUPA", HOST + '/task3')
print(response.text)

#task 4
headers = {
    "User-Agent": "LupaBrowser v1.1"
}
response = requests.get(HOST + '/task4', headers=headers)
print(response.text)

#task 5
for token in range(111, 1000):
    response = requests.get(HOST + '/task5?token={}'.format(token))
    if "You need" not in response.text:
        print(response.text)
        break

#task 6
while True:
    response = requests.post(HOST + '/task6', data={"number": 8})
    if "No" not in response.text:
        print(response.text)
        break