import requests
from ast import literal_eval

# http://search.rcsb.org/#search-api

InChI_for_search='1S/FH/h1H/p-1' # Fluoride
# InChI_for_search=input("Input chemical's InChI for searching: ")
file_name_for_save_result='search_result.txt'

url = 'http://search.rcsb.org/rcsbsearch/v1/query'
data={
  "query": {
    "type": "terminal",
    "service": "chemical",
    "parameters": {
      "value": "InChI="+InChI_for_search,
      "type": "descriptor",
      "descriptor_type": "InChI",
      "match_type": "graph-strict"
    }
  },
  "request_options": {
      # "return_all_hits": True
      "pager": {
          "start": 0,
          "rows": 50000
      }
  },
  "return_type": "entry"
}

print("Querying RCSB PDB REST API...")

header = {'Content-Type': 'application/json;charset=utf-8'}
response = requests.post(url, json=data, headers=header)

if response.status_code == 200:
    result_data=literal_eval(response.text)        
    print(f'Found {result_data["total_count"]} PDB entries matching query.')
    with open(file_name_for_save_result, 'w') as w:
        for i in range(result_data["total_count"]):
            w.write(result_data["result_set"][i]["identifier"]+"\n")
else:
        print("Failed to retrieve results")