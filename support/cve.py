#!/usr/bin/env python
from requests import get

API_HOST = 'https://access.redhat.com/hydra/rest/securitydata'
endpoint = '/cve.json'

def get_data(query):
    full_query = f"{API_HOST}{endpoint}?package={query}"
    r = get(full_query)

    if r.status_code != 200:
        print(f'ERROR: Invalid request; returned {r.status_code} for the following query:\n → {full_query}')
        return None

    if not r.json():
        print(f'No data returned with the following query:{full_query}')
        return None

    return r.json()

def search_id(cvid):
    return get_data(f'{endpoint}?ids={cvid}')

def result(data):
    output = ""
    for cve in data:
        output += f"\n{cve['CVE']}\nIMPACTO:\t{cve['severity']}\nDESCIÇÃO:\t{cve['bugzilla_description']}\nLINK: \t\t{cve['resource_url']}\n"
    return output

