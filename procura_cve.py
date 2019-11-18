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
    
