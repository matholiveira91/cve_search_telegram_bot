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
    print("ADVERT:\n---------------\nSERÁ EXIBIDO APENAS O ULTIMO RESULTADO(O MAIS RECENTE)\n\n\n")
    vid=busca['data'][-1]['id']
    score=busca['data'][-1]['cvss']
    resumo=busca['data'][-1]['summary']
    access=busca['data'][-1]['access']
    impact=busca['data'][-1]['impact']
    vproduct=busca['data'][-1]['vulnerable_product']
    refs=busca['data'][-1]['references']
    return "Resultado da consulta \n-------------\n","Resumo: ",resumo,"\n\n CVE-ID: ",vid,"\n\n Acesso: ",access,"\n\n CVSS: ",score,"\n\n Impacto",impact,"\n\n Produtos Atingidos: ",vproduct,"\n\nReferências: ",refs,"\n------------\n"  

def busca_id(cvid):
    busca=vuln.id(cvid)
    impact=busca['impact']
    access=busca['access']
    score=busca['cvss']
    resumo=busca['summary']
    vproduct=busca['vulnerable_product']
    refs=busca['references']
    print("Resultado da consulta \n ---------- \n","Resumo: ",resumo,"\n\n Acesso: ",access,"\n\n CVSS: ",score,"\n\n Impacto: ",impact,"\n\n Produto Atingido: ",vproduct,"\n\nReferências: ",refs,"\n--------\n")

def ultimas():
    busca=vuln.last()
    vid=busca[0]['id']
    score=busca[0]['cvss']
    resumo=busca[0]['summary']
    access=busca[0]['access']
    impact=busca[0]['impact']
    vproduct=busca[0]['vulnerable_product']
    refs=busca[0]['references']
    print("Resultado da consulta \n ------------- \n","Resumo: ",resumo,"\n\n CVE-ID: ",vid,"\n\n Acesso: ",access,"\n\n CVSS: ",score,"\n\n Impacto",impact,"\n\n Produtos Atingidos: ",vproduct,"\n\n Referências: ",refs,"\n ---------------- \n")  

   

#op=int(input("1 para pesquisar por produto\n\n2 para pesquisar por CVE_id\n\n3 as ultimas cves\n\n"))
#if (op==1):
#   produto=input("digite o produto que deseja pesquisar\n") 
#   busca_produto(produto)       
#elif (op==2):
#    cvid= input("digite o id que deseja buscar \n")
#    busca_id(cvid)
#else:
#    ultimas()
    
