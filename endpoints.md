# ENDPOINTS DESCRIPTION
## Glossary
uuid = uuid_v4 formatted as a string  
sid  = session id cookie, HTTP Only, uuid  
HTTP Code = Expected HTTP Code if API call succeed  

## Endpoints
`/tos` GET, returns ToS and Privacy Policy, HTTP Code 200  

`/list_dbtypes` (GET) - returns list supported db types  
`/list_dbversions` (GET) - returns list supproted db versions   
`/list_envs` (GET) - returns list of environments  
`/list_regions` (GET) - returns list of regions  

`/register` (POST) takes email, password,  
returns HTTP Code 201  
`curl -X POST localhost:5000/register -d '{"email":"your_email","password":"your_password"}'`  

`/login` (POST) takes email, password,  
returns sid-as-a-cookie, HTTP Code 200  
`curl -X POST localhost:5000/login -d '{"email":"your_email","password":"your_password"}' -vvv`

`/db_list` (POST) takes sid,  
returns list of the user's databases, HTTP Code 200  

`/db_create` (POST) takes sid, `json` object with fields:  
`dbname` (string),   
`dbtype` (int),  
`dbversion` (int),  
`env` (int),  
`region` (int)  
returns HTTP Code 201  
Create MySQL DB v8+ in communal docker in CIS: `curl -X POST localhost:5000/db_create --cookie "sid=3653c381-3e25-450c-876b-cc670a753661" -d '{"dbname":"db1","dbtype":3, "dbversion":5, "env": 3,"region":3}'`  

--TODOs--  
--1st priority--  
`/db_delete`  
--2nd priority--  
`/db_backup`  
`/db_restore`  
--3rd priority--  
`/backup_listall`  
`/backup_delete`

`/get_query_size` (on an executor?)
`/_toggle_feature`
`/_get_freecapacity`

## TODOs
`/deletedb` in: sid, db uuid; out: HTTP Code  
`/backupdb` in: sid, db uuid; out: HTTP Code  
`/restoredb` in: sid, db uuid; out: HTTP Code    

## TODOs, Moneymaking :)
`/get_expenses` - get current period expenses  
`/get_hexpenses` - get history records of expenses  
`/get_expenses_a` - get current period expesnes, aggregated  
`/get_hexpenses_a` - get history records of expenses, aggregated  
`/add_credits` - top-ups the balance  

## TODOs  
`/broadcast_get` - separate endpoint to get broadcasts - GET  
`/broadcast_add` - POST, requires token    
`/broadcast_del` - DELETE, requires token    
`/broadcast_list` - GET, requires token  
`/broadcast_upd` - PATCH, requires token, uuid, new msg