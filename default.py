from client import RequestHandler

r = RequestHandler(None)
url = "http://localhost:8000/playlist/1/"
s = r.get(url=url, auth=("willian", "1q2w3e4r"))
print(s)
