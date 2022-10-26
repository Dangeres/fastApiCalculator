import requests

print(
    requests.get(
        'http://0.0.0.0:8000/api/v1/eval/calc',
        params = {
            'phrase': "2+2"
        }
    ).text
)


print(
    requests.post(
        'http://0.0.0.0:8000/api/v1/eval/calc',
        json = {
            'phrase': "2+2*2"
        },
        params = {
            'phrase': "2+2"
        }
    ).text
)