# Oblache API Requests References

Table of contents:  
1. [Common](#common)  
1.1. [Get reference tables](#get-reference-tables)   
1.2. [Registration](###Registration)  
1.3. [Log-in](#log-in)  
1.4. [Is logged?](#is-logged)  
1.5. [Get profile](#get-profile)  
1.6. [Password update](#password-update)  
1.7. [Log-out](#log-out)  
2. [Docker containers](#docker-containers)  
2.1. [Create container](#create-container)  
2.2. [List containers](#list-containers)  
2.3. [Delete container](#delete-container)  
3. [Static sites](#static-sites)  
3.1. [Deploy site](#deploy-site)  
3.2. [List sites](#list-sites)  
3.3. [Undeploy site](#undeploy-site)  
## Common
### Get reference tables
1. `curl https://dbend.areso.pro/list_regions`
2. `curl https://dbend.areso.pro/list_dbtypes`
3. `curl https://dbend.areso.pro/list_dbversions`
4. `curl https://dbend.areso.pro/list_dbenvs`

### Registration
```
curl -i -X POST -H "Content-Type: application/json" \
-d '{"email":"johnblack@gmail.com","password":"histestpassword","tos_agree":true,"language":"en-us"}' \
https://dbend.areso.pro/register -v
```
For this project, accepted languages are "en-us" and "bg-bg".  
For more limitations of the registration, please follow limitations.md  

### Log-in
```
curl -i -X POST -H "Content-Type: application/json" \
-d '{"email":"johnblack@gmail.com","password":"histestpassword"}' \
https://dbend.areso.pro/login
```

### Is logged?
```
curl -i -X POST -H "Authorization: c4ac4567-1bf3-49cf-aae3-a398f36f0683" \
-H "Content-Type: application/json" \
https://dbend.areso.pro/is_logged -v
```
Should return empty object and HTTP code 200, if logged.  
Should return msg code 5, unauthenticated, code 401, if not logged.   

### Get profile

```
curl -i  -H "Authorization: 3f7bc762-c6ac-41d0-affc-0c2f0fa7376b" \
https://dbend.areso.pro/get_profile -v
```

### Password update
```
curl -i -X POST -H "Authorization: 3f7bc762-c6bc-41d9-affc-0c2f0fa7376b" \
-d '{"current_password": "histestpassword", "new_password": "62c6bc41d9affc0c2"}' \
 https://dbend.areso.pro/password_update -v
```

### Log-out
```
curl -i -X POST -H "Authorization: 3f7bc762-c6bc-41d9-affc-0c2f0fa7376b" \
-H "Content-Type: application/json" https://dbend.areso.pro/logout -v
```

## Databases

### Create database
```
curl -i -X POST \
-H "Authorization: 754ebfb5-1d19-4a40-a5c8-aff5968b3b88" \
-d '{"dbtype":3, "dbversion":5, "env": 3,"region":3}' \
https://dbend.areso.pro/db_create -v
```
### List databases
```
curl -i -X POST \
-H "Authorization: 754ebfb5-1a19-4a40-a5c8-aff5968b3b88" \
-H "Content-Type: application/json" https://dbend.areso.pro/db_list -v
```
Get details of one exact database:  
```
curl -i -X POST \
-H "Authorization: 754ebfb5-1a19-4a40-a5c8-aff5968b3b88" \
-d '{"db_uuid":"066fc119-44ba-72ed-8000-977a1afe0eb8"}' \
https://dbend.areso.pro/db_list -v
```
### Delete database
```
curl -i -X POST \
-H "Authorization: 754ebfb5-1a19-4a40-a5c8-aff5968b3b88" \
-d '{"db_uuid":"066fc119-44ba-72ed-8000-977a1afe0eb8"}' \
https://dbend.areso.pro/db_delete -v
```
## Docker Containers

### Create container

### List containers

### Delete container

## Static Sites

### Deploy site
```
curl -i -X POST -H "Authorization: 754ebfb5-1a19-4a40-a5c8-aff5968b3b88" \
 -d '{"source_url":"https://github.com/Areso/English-exercises","id_region":3,"branch":"master"}' \
https://dbend.areso.pro/site_deploy -v
```
### List sites
```
curl -X POST -H "Authorization: 754ebfb5-1a19-4a40-a5c8-aff5968b3b88" https://dbend.areso.pro/site_list -v
```
Get details of one exact site:  
```
curl -X POST -H "Authorization: 754ebfb5-1a19-4a40-a5c8-aff5968b3b88" \
-d '{"site_uuid":"066f9ba0-baa3-7003-8000-d66dced5bfa0"}' \
https://dbend.areso.pro/site_list -v
```
### Undeploy site
```
curl -X POST -H "Authorization: 754ebfb5-1a19-4a40-a5c8-aff5968b3b88" \
-d '{"site_uuid":"066f9ba0-baa3-7003-8000-d66dced5bfa0"}' \
https://dbend.areso.pro/site_undeploy -v
```