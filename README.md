# CVE SEARCH BOT 

TELEGRAM CHAT BOT TO SEARCH CVE'S
---
I'm using the API https://access.redhat.com/documentation/en-us/red_hat_security_data_api/1.0/html-single/red_hat_security_data_api/ form RED HAT to wrap the vulnerabilities form RHSA database 

---

## USAGE 

```sh
git clone https://github.com/matholiveira91/cve_search_telegram_bot.git 
 
python3 cve.py 
```

## FUNCTIONS 

### busca
permit to search a vunerable product by his name 

**PS**
to alter the number of pages alter the param perpage by default the api will show only the first page ordened by date, the newst to the oldst like a LIFO   

### cvid
permit to search a vulnerability by cve-id with the format: CVE-YEARID example: CVE-201919516
