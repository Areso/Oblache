## Technologies used in the project for automation:

| <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original-wordmark.svg" width="80" heigh="80"/> | <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/mysql/mysql-original-wordmark.svg"  width="80" heigh="80"/> | <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/git/git-original-wordmark.svg" width="80" heigh="80"/> | <img src="https://github.com/allure-framework/allure2/blob/main/.idea/icon.png" width="80" heigh="80"/> | <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/selenium/selenium-original.svg" width="80" heigh="80"/> |
|---------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------|
___

To view the current test report, click the button: [![Allure Report](https://img.shields.io/badge/Allure%20Report-deployed-green)](https://areso.github.io/Oblache/)

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


### mysql> select * from localizations order by id_string ASC\G
___
*************************** 1. row ***************************
- id_string: 0
- inner_label: localization_not_found
- used_for: 1000001
- en_us_value: localization string not found
- ru_ru_value: строка локализации не найдена
- bg_bg_value: низът за локализация не е намерен
- es_es_value: cadena de localización no encontrada
- eo_value: lokaliza ĉeno ne trovita
___
*************************** 2. row ***************************
- id_string: 1
- inner_label: registered_successfully
- used_for: 1000001
- en_us_value: registered successfully
- ru_ru_value: пользователь зарегистрирован успешно
- bg_bg_value: регистриран успешно на потребитель
- es_es_value: usario registrado con éxito
- eo_value: registrita sukcese
___
*************************** 3. row ***************************
- id_string: 2
- inner_label: registration_failed
- used_for: 1000001
- en_us_value: user registration failed
- ru_ru_value: регистрация пользователя не удалась
- bg_bg_value: неуспешна регистрация на потребител
- es_es_value: error en el registro de usuario
- eo_value: registrita malsukcese
___
*************************** 4. row ***************************

- id_string: 3
- inner_label: email_taken
- used_for: 1000001
- en_us_value: registration failed, this email is taken
- ru_ru_value: регистрация не удалась, данный email занят
- bg_bg_value: неуспешна регистрация на потребител, имейлът е зает
- es_es_value: el registro falló, se tomó el correo electrónico
- eo_value: registrita malsukcese, retpoŝto estas prenita
___
*************************** 5. row ***************************
- id_string: 4
- inner_label: success_order_for_new_db
- used_for: 1000001
- en_us_value: your order for a new database created successfully
- ru_ru_value: заказ на новую базу зарегистрирован успешно
- bg_bg_value: вашата поръчка за нова база данни е създадена успешно
- es_es_value: su pedido para una nueva base de datos creada exitosamente
- eo_value: via mendo por nova datumbazo kreita sukcese
___
*************************** 6. row ***************************
- id_string: 5
- inner_label: unauthenticated
- used_for: 1000001
- en_us_value: unauthenticated
- ru_ru_value: пользователь не залогинен
- bg_bg_value: неудостоверен
- es_es_value: no autenticado
- eo_value: neaŭtentikigita
___
*************************** 7. row ***************************
- id_string: 6
- inner_label: login_successful
- used_for: 1000001
- en_us_value: login successful
- ru_ru_value: залогинен успешно
- bg_bg_value: успешен вход
- es_es_value: inicio de sesión exitoso
- eo_value: ensaluto sukcesa
___
*************************** 8. row ***************************
- id_string: 7
- inner_label: user_password_incorrect
- used_for: 1000001
- en_us_value: user with this creds not found
- ru_ru_value: пользователь с такими данными не найден
- bg_bg_value: потребител с това удостоверение не е намерен
- es_es_value: usuario con estos créditos no encontrado
- eo_value: uzanto kun ĉi tiu akreditaĵo ne trovita
___
*************************** 9. row ***************************
- id_string: 8
- inner_label: user_not_found
- used_for: 1000001
- en_us_value: user with this creds not found
- ru_ru_value: пользователь с такими данными не найден
- bg_bg_value: потребител с това удостоверение не е намерен
- es_es_value: usuario con estos créditos no encontrado
- eo_value: uzanto kun ĉi tiu akreditaĵo ne trovita
___
*************************** 10. row ***************************
- id_string: 9
- inner_label: some_error
- used_for: 1000001
- en_us_value: some error. please contact support
- ru_ru_value: неизвестная ошибка. обратитесь за помощью
- bg_bg_value: някаква грешка. моля, свържете се с поддръжката
- es_es_value: algún error. por favor contacte con soporte
- eo_value: ia eraro. bonvolu kontakti subtenon
___
*************************** 11. row ***************************
- id_string: 10
- inner_label: tos
- used_for: 1000001
- en_us_value: Hello. This pet-project (later Project) works AS IS, no warranty at all.
- Using Project, you agree to that.
- You MUST create backups of your databases for sake reasons. 

Because I do run project on my own pocket money,
I limit total size of the databases per 1 user as 100 MBs.
Any account don't used more than 6 monts is subject for deletion with all databases.


ru_ru_value: Привет, это пет-проект (Проект) работает КАК ЕСТЬ без каких-либо гарантий.
Пользуюясь Проектом, вы соглашаетесь с этим.
Вы ДОЛЖНЫ создавать бэкапы ваших баз данных с целью их сохранности.
Поскольку я плачу за проект из своих карманных денег,
я лимитирую суммарный объем баз данных на одного пользователя 100 МБ.
Любой аккаунт, не используемый более 6 месяцев, может быть удалён.


bg_bg_value: Здравейте. Този проект (по-късно Проект) работи КАКВОТО Е, без никаква гаранция.
Използвайки Проект, вие се съгласявате с това.
ТРЯБВА да създавате резервни копия на вашите бази данни поради съображения.
Тъй като управлявам проект със собствените си джобни пари,
Ограничавам общия размер на базите данни на 1 потребител като 100 MB.
Всеки акаунт, който не е използван повече от 6 месеца, подлежи на изтриване с всички бази данни.


es_es_value: Hola. Este proyecto favorito (proyecto posterior) funciona TAL CUAL, sin garantía alguna.
Al usar Project, usted acepta eso.
DEBE crear copias de seguridad de sus bases de datos por razones de seguridad.
Porque dirijo el proyecto con mi propio dinero de bolsillo,
Limito el tamaño total de las bases de datos por 1 usuario a 100 MB.
Cualquier cuenta que no haya usado más de 6 meses está sujeta a eliminación con todas las bases de datos.

eo_value: Saluton. Ĉi tiu dorlotbesto-projekto (pli posta Projekto) funkcias KIEL ESTAS, tute ne garantio.
Uzante Project, vi konsentas pri tio.
Vi DEVAS krei sekurkopiojn de viaj datumbazoj pro kialoj.
Ĉar mi efektivigas projekton per mia propra poŝmono,
Mi limigas totalan grandecon de la datumbazoj por 1 uzanto al 100 MBs.
Ajna konto ne uzata pli ol 6 monatoj estas forigita kun ĉiuj datumbazoj.
___
*************************** 12. row ***************************
- id_string: 11
- inner_label: not_allowed_create_new_db
- used_for: 1000001
- en_us_value: you are not allowed to create new databases
- ru_ru_value: вам нельзя создавать новые БД
- bg_bg_value: нямате право да създавате нови бази данни
- es_es_value: no se le permite crear nuevas bases de datos
- eo_value: vi ne rajtas krei novajn datumbazojn
___
*************************** 13. row ***************************
- id_string: 12
- inner_label: db_name_already_taken
- used_for: 1000001
- en_us_value: this db name is already taken
- ru_ru_value: это имя БД уже занято
- bg_bg_value: това бази данни име вече е заето
- es_es_value: este nombre de base de datos ya está en uso
- eo_value: ĉi tiu db-nomo jam estas prenita
___
*************************** 14. row ***************************
- id_string: 13
- inner_label: deletion_request_accepted
- used_for: 1000001
- en_us_value: successfully accepted request for deletion
- ru_ru_value: успешно принят запрос на удаление
- bg_bg_value: успешно приета заявка за изтриване
- es_es_value: solicitud de eliminación aceptada con éxito
- eo_value: sukcese akceptis peton por forigo
___
*************************** 15. row ***************************
- id_string: 14
- inner_label: account_blocked
- used_for: 1000001
- en_us_value: your account is blocked. contact support
- ru_ru_value: ваш аккаунт заблокирован. обратитесь за помощью
- bg_bg_value: някаква грешка. моля, свържете се с поддръжката
- es_es_value: tu cuenta está bloqueada. por favor contacte con soporte
- eo_value: via konto estas blokita. bonvolu kontakti subtenon
___
*************************** 16. row ***************************
- id_string: 15
- inner_label: account_deleted
- used_for: 1000001
- en_us_value: your account is deleted
- ru_ru_value: ваш аккаунт заблокирован. обратитесь за помощью
- bg_bg_value: някаква грешка. моля, свържете се с поддръжката
- es_es_value: tu cuenta está bloqueada. por favor contacte con soporte
- eo_value: via konto estas blokita. bonvolu kontakti subtenon
___
*************************** 17. row ***************************
- id_string: 16
- inner_label: database_not_found
- used_for: 1000001
- en_us_value: requested database is not found
- ru_ru_value: запрошенная БД не найдена
- bg_bg_value: исканата база данни не е намерена
- es_es_value: la base de datos solicitada no se encuentra
- eo_value: petita datumbazo ne estas trovita
___
*************************** 18. row ***************************
- id_string: 17
- inner_label: marked_for_manual_deletion
- used_for: 1000001
- en_us_value: broken database marked for manual deletion
- ru_ru_value: сломанная БД помечена для ручного удаления
- bg_bg_value: повредената база данни, маркирана за ръчно изтриване
- es_es_value: la base de datos rota marcada para eliminación manual
- eo_value: la rompita datumbazo markita por mana forigo
___
*************************** 19. row ***************************
- id_string: 18
- inner_label: cant_delete_db_while_creating
- used_for: 1000001
- en_us_value: error: can't delete a db while it's creating
- ru_ru_value: ошибка: нельзя удалить БД, пока она создается
- bg_bg_value: грешка: не може да изтрие БД, докато се създава
- es_es_value: error: no se puede eliminar una base de datos mientras se está creando
- eo_value: eraro: ne povas forigi db dum ĝi kreiĝas
___
*************************** 20. row ***************************
- id_string: 19
- inner_label: cant_delete_db_while_deleting
- used_for: 1000001
- en_us_value: error: can't delete a db while it's deleting
- ru_ru_value: ошибка: нельзя удалить БД, пока она удаляется
- bg_bg_value: грешка: не може да изтрие БД, докато се изтрива
- es_es_value: error: no se puede eliminar una base de datos mientras se está eliminando
- eo_value: eraro: ne povas forigi db dum ĝi forigas
___
*************************** 21. row ***************************
- id_string: 20
- inner_label: cant_delete_db_in_deletion_error
- used_for: 1000001
- en_us_value: error: can't delete a db while it is in deletion error state
- ru_ru_value: ошибка: нельзя удалить БД пока она ошибке удаления
- bg_bg_value: грешка: не може да изтрие БД, докато е състояние на грешка при изтриване
- es_es_value: error: no se puede eliminar una base de datos mientras está en estado de error de eliminación
- eo_value: eraro: ne povas forigi db dum ĝi estas en foriga erara stato
___
*************************** 22. row ***************************
- id_string: 21
- inner_label: region_notfound_notavailable
- used_for: 1000001
- en_us_value: error: region isn't found or isn't available for order
- ru_ru_value: ошибка: регион не найден или недоступен для заказа
- bg_bg_value: грешка: регионът не е намерен или не е наличен за поръчка
- es_es_value: error: la región no se encuentra o no está disponible para realizar pedidos
- eo_value: eraro: regiono ne estas trovita aŭ ne haveblas por mendo
___
*************************** 23. row ***************************
- id_string: 22
- inner_label: dbtype_notfound_notavailable
- used_for: 1000001
- en_us_value: error: DB type isn't found or isn't available for order
- ru_ru_value: ошибка: тип БД не найден или недоступен для заказа
- bg_bg_value: грешка: Типът DB не е намерен или не е наличен за поръчка
- es_es_value: error: El tipo de BD no se encuentra o no está disponible para realizar pedidos
- eo_value: eraro: DB-tipo ne estas trovita aŭ ne haveblas por mendo
___
*************************** 24. row ***************************
- id_string: 23
- inner_label: dbver_notfound_notavailable
- used_for: 1000001
- en_us_value: error: DB version isn't found or isn't available for order
- ru_ru_value: ошибка: версия БД не найдена или недоступна для заказа
- bg_bg_value: грешка: Версията на DB не е намерен или не е наличен за поръчка
- es_es_value: error: La versión de BD no se encuentra o no está disponible para realizar pedidos
- eo_value: eraro: DB-versio ne estas trovita aŭ ne haveblas por mendo
- 24 rows in set (0.00 sec)
