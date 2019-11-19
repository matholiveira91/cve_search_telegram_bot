#!/usr/env/bin python3

# AUTHOR: MATHEUS OLIVEIRA
# DATE: 14/11/2019
# LICENSE GPLV3 
# DESCRIPTION BOT TO SEARCH CVE BY VENDOR AND PRODUCT

import pyCVE as cve 
import json
import requests 

def main:
    
    vendor=str(raw_input("digite o fabricante que deseja buscar"))
    product=str(raw_input("digite o produto que deseja bsucar"))
    cvid=str(raw_input("digite a cvid que deseja buscar"))
    return vendor product cvid
def busca(vendor,product):
    if vendor is not None:
        json.load([cve.browse(vendor)],j1)
    elif product is not None:    
        json.load([cve.search(product)],j2)
    elif cvid is not None:
        json.load([cve.id(cvid)],j3)
    else:
        json.load([cve.last()],j4)
    

