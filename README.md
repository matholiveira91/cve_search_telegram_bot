# CVE SEARCH BOT 

TELEGRAM CHAT BOT TO SEARCH CVE'S
---
I'm using the wrapper from https://github.com/cve-search/PyCVESearch but adopting python3 syntax for integration with the API https://cve.circl.lu/api/ for search CVE'S	i'm searching to methods to integrate with mitre and NVD databases for a more acurated result but i dont find any eficient method to wrap this and for now this will be suficient, for now this will be all cli interface but soon i'll integrate with a telegram bot but first things first

---

## USAGE 

``` bash
cd pycvesearch 
pip install . 
cd ..
python3 procura_cve.py 
```

## FUNCTIONS 

### busca
permit to search a vunerable product by his name or vendor/hisname for less ambiguos return 

### id
permit to search a vulnerability by cve-id with the format: CVE-YEAR-ID example: CVE-2019-19516
