#!/usr/env/bin python3
# _*_ coding utf-8 _*_

# AUTHOR: MATHEUS OLIVEIRA
# DATE: 14/11/2019
# LICENSE GPLV3 
# DESCRIPTION BOT TO SEARCH CVE BY VENDOR AND PRODUCT
from pycvesearch import CVESearch 

#-------------------------------------------------------------
vuln=CVESearch()

def busca_produto(produto):
    busca=vuln.search(produto)
    vid=busca['data'][-1]['id']
    score=busca['data'][-1]['cvss']
    resumo=busca['data'][-1]['summary']
    access=busca['data'][-1]['access']
    impact=busca['data'][-1]['impact']
    vproduct=busca['data'][-1]['vulnerable_product']
    print("Resultado da consulta \n ------------- \n","Resumo: ",resumo,"\n\n CVE=ID: ",vid,"\n\n Acesso: ",access,"\n\n CVSS: ",score,"\n\n Impacto",impact,"\n\n Produtos Atingidos: ",vproduct)  

op=int(input("digite 1 para ir à pagina do fabricante\n\n2 para pesquisar por produto\n\n3 para pesquisar por CVE_id\n\n4 as ultimas cves\n\n"))
if (op==1):
    vendor= input("digite o nome do fabricante\n")
    print('pagina do vendor {}\n'.format(vuln.browse(vendor)))
elif (op==2):
   produto=input("digite o produto que deseja pesquisar\n") 
   busca_produto(produto)       
elif (op==3):
    cvid= input("digite o id que deseja buscar \n")
    print('detalhes da CVE solicitada {}\n'.format(vuln.id(cvid)))
else:
    ultimas=vuln.last()
    print('últimas CVEs cadastradas {}\n'.format(vuln.last()))


