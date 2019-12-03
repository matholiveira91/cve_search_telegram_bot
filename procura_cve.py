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
    print("Resultado da consulta \n ------------- \n","Resumo: ",resumo,"\n\n CVE-ID: ",vid,"\n\n Acesso: ",access,"\n\n CVSS: ",score,"\n\n Impacto",impact,"\n\n Produtos Atingidos: ",vproduct)  

def busca_id(cvid):
    busca=vuln.id(cvid)
    impact=busca['impact']
    access=busca['access']
    score=busca['cvss']
    resumo=busca['summary']
    vproduct=busca['vulnerable_product']
    print("Resultado da consulta \n ---------- \n","Resumo: ",resumo,"\n\n Acesso: ",access,"\n\n CVSS: ",score,"\n\n Impacto: ",impact,"\n\n Produto Atingido: ",vproduct)

def ultimas():
    busca=vuln.last()
    vid=busca[-1]['id']
    score=busca[-1]['cvss']
    resumo=busca[-1]['summary']
    access=busca[-1]['access']
    impact=busca[-1]['impact']
    vproduct=busca[-1]['vulnerable_product']
    print("Resultado da consulta \n ---------- \n","Resumo: ",resumo,"\n\n Acesso: ",access,"\n\n CVSS: ",score,"\n\n Impacto: ",impact,"\n\n Produto Atingido: ",vproduct)
   

op=int(input("1 para pesquisar por produto\n\n2 para pesquisar por CVE_id\n\n3 as ultimas cves\n\n"))
if (op==1):
   produto=input("digite o produto que deseja pesquisar\n") 
   busca_produto(produto)       
elif (op==2):
    cvid= input("digite o id que deseja buscar \n")
    busca_id(cvid)
else:
    ultimas()
    


