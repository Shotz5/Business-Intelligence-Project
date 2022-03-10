import pandas
import json
import numpy
import requests

def main():
    data = pandas.read_csv("BP_metadata.csv")

    with open("data.json", "r") as json_file:
        parent = json.load(json_file)

    # First 1800
    # for current_ds in data.code[:1800]:
    #     print(current_ds)
    #     url = "https://data.nasdaq.com/api/v3/datasets/BP/" + current_ds + "?api_key=AqAMK4Qe87CQRbnA_qbV"
    #     response = requests.get(url)
    #     parent[current_ds] = response.json()

    # After 1800
    # for current_ds in data.code[1800:]:
    #     print(current_ds)
    #     url = "https://data.nasdaq.com/api/v3/datasets/BP/" + current_ds + "?api_key=AqAMK4Qe87CQRbnA_qbV"
    #     response = requests.get(url)
    #     parent[current_ds] = response.json()

    # print("Outputting to file")
    # with open('data.json', "w") as json_file:
    #     json.dump(parent, json_file, ensure_ascii=False, indent=4)

def json_test():
    url = "http://api.open-notify.org/astros.json"
    response = requests.get(url)
    res_json = response.json()
    print(json.dumps(res_json, indent=2))

if __name__ == "__main__":
    main()
