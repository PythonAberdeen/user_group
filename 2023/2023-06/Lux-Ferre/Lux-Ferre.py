import json
import httpx
import requests
import time


def test_run(apikey: str):
    auth_tuple = (apikey, "")
    headers = {'Authorization': apikey}

    response = requests.get("https://api.company-information.service.gov.uk/company/SC126553", headers=headers)
    requests_res = json.loads(response.content)

    response = httpx.get("https://api.company-information.service.gov.uk/company/SC126553", auth=auth_tuple)
    httpx_res = json.loads(response.content)

    print(requests_res)
    print(httpx_res)


def query_api(query:str) -> dict:
    auth_tuple = (apikey, "")

    root_endpoint = "https://api.company-information.service.gov.uk/"

    full_endpoint = root_endpoint + "advanced-search/companies?"

    full_query = full_endpoint + query

    response = httpx.get(full_query, auth=auth_tuple)
    result = json.loads(response.content)["items"]

    results_list = []

    for company in result:
        results_list.append(company["company_name"])

    return results_list


if __name__ == "__main__":
    apikey=""

    aberdeen_postcodes = ["AB10", "AB11", "AB12", "AB13", "AB24", "AB25"]
    company_list = []

    # All Aberdeen software companies still active
    for postcode in aberdeen_postcodes:
        company_list += query_api(f"company_status=active&location={postcode}&size=5000&sic_codes=62012")
        time.sleep(1)

    with open('company_list.txt', 'a') as f:
        f.writelines(line + '\n' for line in company_list)

    print(company_list)
