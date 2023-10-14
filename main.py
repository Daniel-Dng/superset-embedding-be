from fastapi import FastAPI
import requests
import json
from fastapi.middleware.cors import CORSMiddleware
from config import settings


app = FastAPI()
origins = [
    # "http://localhost",
    # "http://localhost:8080",
    # "http://localhost:8088",
    # settings.SUPERSET_BASE_URL,
    '*'
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/guest_login/{dashboard_id}")
async def guest_login(dashboard_id):
    url = f"{settings.SUPERSET_BASE_URL}/api/v1/security/login"
    payload = json.dumps({"password": settings.SUPERSET_PW, "username": settings.SUPERSET_USER,
                          "provider": "db", "refresh": "true"})
    headers = {'Content-Type': 'application/json', 'Accept': 'application/json'}

    _response = requests.post(url, headers=headers, data=payload)
    superset_access_token = json.loads(_response.text)['access_token']
    payload = json.dumps({
        "user": {
            "username": settings.SUPERSET_USER,
        },
        "resources": [{
            "type": "dashboard",
            "id": dashboard_id  # e.g. "f6596a6c-f176-40c7-b159-4ec483a010ce"
        }],
        "rls": []
    })

    bearer_token = "Bearer " + superset_access_token
    # print(bearer_token)
    response2 = requests.post(
        url=f"{settings.SUPERSET_BASE_URL}/api/v1/security/guest_token",
        data=payload,
        headers={"Authorization": bearer_token, 'Accept': 'application/json', 'Content-Type': 'application/json'})
    # print(response2.json())
    return response2.json()['token']

