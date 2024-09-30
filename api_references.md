# Oblache API References

Table of contents:  
1. [Common](#common)  
1.1. [Get reference tables"](#get-reference-tables)   
1.2. [Registration](###Registration)  
1.3. [Log-in](#log-in)  
1.4. [Is logged?](#is-logged)  
1.5. [Get profile](#get-profile)  
1.6. [Password update](#password-update)  
1.7. [Log-out](#log-out)

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

### List databases

### Delete database

## Docker Containers

### Create database

### List databases

### Delete database

## Sites

### Create database

### List databases

### Delete database

