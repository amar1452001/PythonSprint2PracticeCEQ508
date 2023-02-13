import requests
import json

base_url = "https://api.github.com/"
token = "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"
def list_commit(owner,repo):
    url = base_url + "repos/" + owner + "/" + repo + "/commits"
    print(url)
    req = requests.get(url, auth=(token,''))
    print(req)
    return req.json()
print(list_commit("amar1452001","portfolio"))

