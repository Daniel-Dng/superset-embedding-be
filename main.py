from fastapi import FastAPI
import requests
import json
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
origins = [
    "http://localhost",
    "http://localhost:8080",
    "http://localhost:8088",
    '*'
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/guest_login")
async def guest_login():
    url = "http://127.0.0.1:8088/api/v1/security/login"
    payload = json.dumps({"password": "admin", "provider": "db", "refresh": "true", "username": "admin"})
    headers = {'Content-Type': 'application/json', 'Accept': 'application/json'}

    responsel = requests.request("POST", url, headers=headers, data=payload)
    print(responsel.text)
    superset_access_token = json.loads(responsel.text)['access_token']
    payload = json.dumps({
        "user": {
            "username": "admin",
        },
        "resources": [{
            "type": "dashboard",
            "id": "f6596a6c-f176-40c7-b159-4ec483a010ce"
        }],
        "rls": []
    })

    bearer_token = "Bearer " + superset_access_token
    print(bearer_token)
    response2 = requests.post(
        "http://127.0.0.1:8088/api/v1/security/guest_token",
        data=payload,
        headers={"Authorization": bearer_token, 'Accept': 'application/json', 'Content-Type': 'application/json'})
    print(response2.json())
    return response2.json()['token']

