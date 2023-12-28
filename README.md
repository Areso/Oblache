## Technologies used in the project for automation:

| <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original-wordmark.svg" width="80" heigh="80"/> | <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/mysql/mysql-original-wordmark.svg"  width="80" heigh="80"/> | <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/git/git-original-wordmark.svg" width="80" heigh="80"/> | <img src="https://github.com/allure-framework/allure2/blob/master/.idea/icon.png" width="80" heigh="80"/> | <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/selenium/selenium-original.svg" width="80" heigh="80"/> |
|---------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------|
___

To view the current test report, click the button: [![Allure Report](https://img.shields.io/badge/Allure%20Report-deployed-green)](https://lambotik.github.io/API/)

# DBaaS backend
`export FLASK_APP=dbaas_backend.py`
`flask run`
## RabbitMQ
to up the mq
1. sudo mkdir /home/docker  
2. sudo chmod 0777 /home/docker
```
docker run \
    -v /home/docker:/bitnami/rabbitmq/mnesia \
    --name rabbitmq \
    -p 15672:15672 -p 5672:5672 -d \
    rabbitmq:management
```
defaults: user/bitnami, web: guest/guest
```
docker start rabbitmq
```

register:  
```
curl -H "Content-Type: application/json" -d '{"email":"test3@mail.ru","password":"password"}' localhost:5000/register
```
login:  
```
curl -i -H "Content-Type: application/json" -d '{"email":"test3@mail.ru","password":"password"}' localhost:5000/login -v
```
  
list user's databases:  
```
curl -X POST -i -H "Content-Type: application/json" --cookie "sid=94951dfd-f994-4aa9-910e-ccc814748011" localhost:5000/db_list
```

delete a database:
```
curl -X POST -i -H "Content-Type: application/json" -d '{"db_uuid":"0653dc62-1fc2-7f65-8000-e9d3b71bdabc"}' --cookie "sid=94951dfd-f994-4aa9-910e-ccc814748011" localhost:5000/db_delete
```

create db:  
```
curl -X POST localhost:5000/db_create --cookie "sid=c2e9e313-6762-434d-94e7-7eec27048b14" -d '{"dbtype":3, "dbversion":5, "env": 3,"region":3}'
```
create db (with db name), currently disabled:  
```
curl -X POST localhost:5000/db_create --cookie "sid=11c7c5d0-41c0-45df-ad4a-275d0018798a" -d '{"dbname":"db1","dbtype":3, "dbversion":5, "env": 3,"region":3}'
```
todo list  
1. billing. 
2. credits placement every month (set credits =0; set credits = days number x 24 x 60 / 12 (5m billing period)
3. credits disposal every 5m
4. "premium acc" for non-communal deployments
5. more credits for more place.
