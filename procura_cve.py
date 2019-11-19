#!/usr/env/bin python3

# AUTHOR: MATHEUS OLIVEIRA
# DATE: 14/11/2019
# LICENSE GPLV3 
# DESCRIPTION BOT TO SEARCH CVE BY VENDOR AND PRODUCT

import pycve as cve 
import json
#import requests 
op=int(input("digite 1 para pesquisar por fabricante\n2 para pesquisar por produto\n 3 para pesquisar por CVE_id\n")
if (op==1):
    vendor=input("digite o fabricante que deseja buscar\n")
    busca_vendor(vendor)
elif (op==2):
    product=input("digite o produto que deseja bsucar\n")
    busca_product(product
else:
    cvid=input("digite a cvid que deseja buscar\n")

def busca_vendor(vendor):
    json.loads("Busca por fabricante: ",[cve.browse(vendor)],result)
    return result
def busca_product 

