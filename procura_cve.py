#!/usr/env/bin python3
# _*_ coding utf-8 _*_

# AUTHOR: MATHEUS OLIVEIRA
# DATE: 14/11/2019
# LICENSE GPLV3 
# DESCRIPTION BOT TO SEARCH CVE BY VENDOR AND PRODUCT
from pycvesearch import CVESearch 

#-------------------------------------------------------------
vuln=CVESearch()
op=int(input("digite 1 para ir à pagina do fabricante\n\n2 para pesquisar por produto\n\n3 para pesquisar por CVE_id\n\n4 as ultimas cves\n\n"))
if (op==1):
    vendor= input("digite o nome do fabricante\n")
    print('pagina do vendor {}\n'.format(vuln.browse(vendor)))
elif (op==2):
    product= input("digite o nome do produto que deseja pesquisar\n")
    print('vulnerabilidades cadastradas para o produto {}\n'.format(vuln.search(product)))
elif (op==3):
    cvid= input("digite o id que deseja buscar \n")
    
    print('detalhes da CVE solicitada {}\n'.format(vuln.id(cvid)))
else:
    print('últimas CVEs cadastradas {}\n'.format(vuln.last()))


