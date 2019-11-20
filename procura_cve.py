#!/usr/env/bin python3

# AUTHOR: MATHEUS OLIVEIRA
# DATE: 14/11/2019
# LICENSE GPLV3 
# DESCRIPTION BOT TO SEARCH CVE BY VENDOR AND PRODUCT

import pycve as cve 
import json
#import requests 
op=int(input("digite 1 para pesquisar por fabricante\n2 para pesquisar por produto\n 3 para pesquisar por CVE_id\n4 as ultimas cves")
if (op==1):
    vendor=input("digite o fabricante que deseja buscar\n")
    busca_vendor(vendor)
elif (op==2):
    product=input("digite o produto que deseja bsucar\n")
    busca_product(product
elif (op==3):
    cvid=input("digite a cvid que deseja buscar\n")
    busca_id(cvid)
else:
    last()
#-----------------------------------------------------------------
def busca_vendor(vendor):
    json.loads("Busca por fabricante: ",[cve.browse(vendor)],result)
    return result
def busca_product(product): 
    json.loads("Busca por produto: ",[cve.search(product),result)
    return result
def busca_id(cvid):
    json.loads("Busca por cvid: ",[cve.id(cveid)],result)
    return result
def last():
    json.loads("Ultimas registradas: ",[cve.last],result)
    return result 

