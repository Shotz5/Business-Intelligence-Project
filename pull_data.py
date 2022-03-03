import pandas
import nasdaqdatalink
import json
import numpy

def main():
    data = pandas.read_csv("BP_metadata.csv")

    # for line in data.code:
    #     print(line)

    nasdaqdatalink.api_key = 'AqAMK4Qe87CQRbnA_qbV'
    nasdaqdatalink.get("BP/" + data.code[1])

    # with open('data.json', "w", encoding='utf-8') as json_file:
    #     json_file.truncate(0)
    #     json.dump(nneato, json_file, separators=(',', ':'), ensure_ascii=False, sort_keys=True, indent=4)

if __name__ == "__main__":
    main()
