#!/usr/bin/env python
from __future__ import print_function
import sys
from requests import get
from datetime import datetime, timedelta

API_HOST = 'https://access.redhat.com/hydra/rest/securitydata'


def get_data(query):
    full_query = f"{API_HOST}{query}"
    r = get(full_query)

    if r.status_code != 200:
        print('ERROR: Invalid request; returned {r.status_code} for the following query:\n → {full_query}')
        sys.exit(1)

    if not r.json():
        print(f'No data returned with the following query:{full_query}')
        sys.exit(0)

    return r.json()

def busca_id(cvid):
    params = 'ids='+cvid

    return get_data(f'{endpoint}?{params}')
    #fim da funcao
endpoint = '/cve.json'
produto = input('Digite o produto que deseja pesquisar ou o "cvid" para pesquisar pelo cvid\n → ')

if (produto != 'cvid'):
    params = f'package={produto}'
    data=get_data(f'{endpoint}?{params}')
else: 
    cvid = input("digite um ou mais CVEIDs separado(s) por virgula no forma CVE-ANONUMERO\n")
    data=busca_id(cvid)

for cve in data:
    print(f"{cve['CVE']}\nIMPACTO:\t{cve['severity']}\nDESCIÇÃO:\t{cve['bugzilla_description']}\nLINK: \t\t{cve['resource_url']}\n")


print('-----')
# Get a list of kernel advisories for the last 30 days and display the
# packages that they provided.
endpoint = '/cvrf.json'
date = datetime.now() - timedelta(days=5)
params = 'package=kernel&after=' + str(date.date())

data = get_data(endpoint + '?' + params)

#kernel_advisories = []
#for advisory in data:
 #   print(advisory['RHSA'], advisory['severity'], advisory['released_on'])
  #  print('-', '\n- '.join(advisory['released_packages']))
   # kernel_advisories.append(advisory['RHSA'])


#print('-----')
# From the list of advisories saved in the previous example (as
# `kernel_advisories`), get a list of affected products for each advisory.
#endpoint = '/cvrf/'

#for advisory in kernel_advisories:
#    data = get_data(endpoint + advisory + '.json')
#    print(advisory)

#    product_branch = data['cvrfdoc']['product_tree']['branch']
#    for product_branch in data['cvrfdoc']['product_tree']['branch']:

#        if product_branch['type'] == 'Product Family':

#            if type(product_branch['branch']) is dict:
#                print('-', product_branch['branch']['full_product_name'])

 #           else:
 #               print('-', '\n- '.join(pr['full_product_name'] for
#                                       pr in product_branch['branch']))
