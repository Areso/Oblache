# Design document
This document covers the basic functionality of the Oblache (Small cloud)

# Functionality
## Cloud databases
Oblache allows
- to create  
- to delete  

MySQL (8.0.20+), PostgreSQL (15) databases automatically from the  
- web interface
- from API  

As parameters it currently takes:
- type of a new DB (`mysql8`,`postgres`)
- version of a new DB (`mysql 8.0.20`, `Pg14`,`Pg15`)
- type of the host (`communal` means shared, `standalone` etc)
- region of the host (`EU`, `US`, `CIS` - please note, not all regions are allowed to all users)

For a created database the following information is provided:
- UUID of a database - great to provide the admin if there is any issue
- JDBC connection string with all the credentials and the host-port pair
- region (EU, CIS, US, etc)
- current known status (TODO to add `actualize` button here)
- date of creation
- gross size of the database

Known statuses are:
```
    # 0 db_creating          - EXCEPTION                        - OK
    # 1 db_created           -   NORMAL FLOW                    - OK
    # 2 error                -     COVERED with manual deletion - OK
    # 3 deleting             - EXCEPTION                        - OK
    # 4 deleted              -FILTERED OUT O on previous step   - OK
    # 5 read_only_threshold  -   NORMAL FLOW                    - OK
    # 6 error_creating       -     COVERED with manual deletion - OK
    # 7 error_deleting       - EXCEPTION                        - OK
    # 8 error_ro_threshold   - EXCEPTION?--???
    # 9 manual_deleting      - EXCEPTION?---??/
```

Current version (0.25) state machine (PlantUML) of the databases:  
```
"/db_create"->creating : Order accepted
creating->"/db_create" : db_uuid
creating->created : Success
creating->creation_error : Fail
created->deleting: "/db_delete" order accepted
deleting->deletion_error: Fail
deleting->deleted: Success
deletion_error->deleted : Manual deletion
creation_error->deleted : Manual deletion
```

Visualize:  
![image](https://www.plantuml.com/plantuml/png/ZOun3i8m34NtdiBg7h5toCY663X0PM8BHOeIv3RtnoGOsavijjxxzXzFT9-3CAuyEj-6c1ymmLM81J04VgvCWn7djmdrTAarReNEIDcjQdnPZYoMFBD84LNE6DFmIJXFdFWjJj2-j5M_b7qNiyotS_tQ4JFzYkpzhw0zBfWh9Z2XL_h7V040)

## Docker Container Engine
Oblache allows
- to create
- to delete

a Docker container from a Docker image, published on [DockerHub](https://hub.docker.com/)

As parameters it currently takes:  
1) TCP port(s) to expose. It could be written as 
- separate ports with commas `80,443`
- a range `5400-5410`, both borders ARE included  
- empty value is allowed
Please note, you ARE NOT allowed to mix them up like this `443,5400-5410`!
2) Environment key-value pairs, e.g.: 
- `username=myuser`
- `username=myuser;password=mypassword`
- empty value also allowed

For a created Docker Container the following information is provided:
- UUID of a container - great to provide the admin if there is any issue
- Docker Image name (used for Container creation)
- Docker Container name
- Ports (if any was exposed, `exposed:inner`)
- Creation date
- current known status (TODO to add `actualize` button here)

## User manipulation
Okay, we covered the basic functionality of the cloud  
Let's talk about user statuses and stuff here  