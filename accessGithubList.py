#Code to access GITHUB Account
#in which i am going to LIST ALL BRANCHES

import requests

BASE_URL ="https://api.github.com/"
token ="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"

def list_branch(owner,repo):
    url = BASE_URL + "repos/" + owner + "/" + repo + "/branches"
    print(url)
    req = requests.get(url, auth=(token,''))
    print(req)
    return req.json()

print(list_branch("amar1452001","portfolio")) 