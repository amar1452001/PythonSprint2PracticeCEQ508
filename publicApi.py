import requests

#BASE_URL = "https://wikimedia.org/api/rest_v1/metrics/pageviews/per-article/en.wikipedia/all-access/all-agents/Tiger_King/daily/20210901/20210930"

base_url = "https://api.github.com/"
token = "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"

# def get_user():
#     url = base_url + "users"
#     print(url)
#     response = requests.get(url,auth=(token,''))
#     print(response)
#     print(response.json())
# get_user()



#Listing the commits of a particular repository named as PythonAssignment1cloudeqAmar

# def list_commit(owner,repo):
#     url = base_url + "repos/" + owner + "/" + repo + "/commits"
#     print(url)
#     req = requests.get(url, auth=(token,''))
#     print(req)
#     return req.json()
# print(list_commit("amar1452001","PythonAssignment1cloudeqAmar"))



#listing branches for HEAD commits


# def list_head_commit(owner,repo,commit_sha):
#     url = base_url + "repos/" + owner + "/" + repo + "/commits" + "/" + commit_sha + "/branches-where-head"
#     print(url)
#     req = requests.get(url, auth=(token,''))
#     print(req)
#     return req.json()
# print(list_head_commit("amar1452001","TerraformAssignment1CEQ508","9d5885a1dfa129ab443f945740ecf48b6a7d23b5"))


#Listing pull requests associated with a commit

# def list_pull_commit(owner,repo,commit_sha):
#     url = base_url + "repos/" + owner + "/" + repo + "/commits" + "/" + commit_sha + "/pulls"
#     print(url)
#     req = requests.get(url, auth=(token,''))
#     print(req)
#     return req.json()
# print(list_pull_commit("amar1452001","PythonSprint2PracticeCEQ508","9d5885a1dfa129ab443f945740ecf48b6a7d23b5"))

# A Git reference ( git ref ) is a file that contains a Git commit SHA-1 hash. When referring to a Git commit, you can use the Git reference, which is an easy-to-remember name, rather than the hash. The Git reference can be rewritten to point to a new commit.

# Get a commit

def get_commit(owner,repo,ref):
    url = base_url + "repos/" + owner + "/" + repo + "/commits" + "/" + ref
    print(url)
    req = requests.get(url, auth=(token,''))
    print(req)
    return req.json()
print(get_commit("amar1452001","PythonSprint2PracticeCEQ508","9d5885a"))


