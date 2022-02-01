import requests
import json


def get_email_github(backend, user, response, *args, **kwargs):
    resp = requests.get(
        "https://api.github.com/user/emails",
        headers={"Authorization": "token %s" % response["access_token"]},
    )
    json = resp.json()
    email = [e["email"] for e in json]

    user.email = email[0]
    user.save()
