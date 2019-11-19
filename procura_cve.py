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
    d1=cve.browse(vendor)
    d2=cve.search(product)
    d3=cve.id(cvid)
    j1=json_string'{"d1"}'

