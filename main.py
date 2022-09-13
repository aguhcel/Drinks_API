# %%
import requests
import json

# %%
# Test API thecocktaildb
def cocktails():
    f = r"https://www.thecocktaildb.com/api/json/v1/1/search.php?s=margarita"
    data = requests.get(f)
    tt = json.loads(data.text)
    # webbrowser.open(tt["url"])

    for i in (tt["drinks"]):
        print(i, "\n")
    print(len(tt["drinks"]))


cocktails()

