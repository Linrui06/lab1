import requests
print(requests.__version__)

r = requests.get("https://www.google.com/")
print(r)

g = requests.get("https://raw.githubusercontent.com/Linrui06/lab1/main/printVersion.py")
print(g.text)
print(g)


