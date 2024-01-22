
# class DataMySql:
    # def __init__(self, connection):
    #     self.connection = connection

    # @staticmethod
    # def data_to_connect_my_sql(post_db_list):
    #     list_db = post_db_list
    #     json_list_db = json.loads(list_db.text)
    #     first_db_uuid = list(json_list_db['content'].keys())[0]
    #     db_name = json_list_db['content'][first_db_uuid][0]
    #     user_name = json_list_db['content'][first_db_uuid][3].split(':')[1].replace('//', '')
    #     host = json_list_db['content'][first_db_uuid][3].split(':')[2].partition('@')[2]
    #     password_db = json_list_db['content'][first_db_uuid][3].split(':')[2].partition('@')[0]
    #     return host, user_name, db_name, password_db

    # def connect_my_sql(self, select=None):
    #     print('\nConnecting to DB...')
    #     if select is None:
    #         select = '''select 1 from dual'''
    #     else:
    #         select = select
    #     try:
    #         host, user, database, password = self.data_to_connect_my_sql(API.post_db_list(self.sid))
    #         connection = mysql.connector.connect(host=host,
    #                                              port=3306,
    #                                              user=user,
    #                                              database=database,
    #                                              password=password
    #                                              )
    #         print('Successfully connected...')
    #         try:
    #             with connection.cursor() as cursor:
    #                 cursor.execute(select)
    #                 res = cursor.fetchall()
    #                 connection.commit()
    #                 with allure.step(f'DB response {res}'):
    #                     print(f'DB response {res}!!!!')
    #                 assert res == [(1,)], 'Wrong result!!! Expected result: [(1,)].'
    #         finally:
    #             connection.close()
    #
    #         return connection
    #     except Exception as ex:
    #         print('Connection refused...\n')
    #         print(ex)

    # def connect_my_sql(self, select=None):
    #     """
    #     :param select:
    #     :return:
    #     """
    #     print('\nConnecting to DB...')
    #     if select is None:
    #         select = '''select 1 from dual'''
    #     else:
    #         select = select
    #     cursor = self.connection.cursor()
    #     with cursor:
    #         cursor.execute(select)
    #         res = cursor.fetchall()
    #         cursor.commit()
    #         with allure.step(f'DB response {res}'):
    #             print(f'DB response {res}!!!!')
    #         assert res == [(1,)], 'Wrong result!!! Expected result: [(1,)].'
    #
    # def create_table(self, query):
    #     cursor = self.connection.cursor()
    #     cursor.execute(query)
    #     cursor.commit()

        # print('\nConnecting to DB...')
        # try:
        #     host, user, database, password = self.data_to_connect_my_sql(API.post_db_list(self.sid))
        #     connection = mysql.connector.connect(host=host,
        #                                          port=3306,
        #                                          user=user,
        #                                          database=database,
        #                                          password=password
        #                                          )
        #     print('Successfully connected...')
        #     try:
        #         with connection.cursor() as cursor:
        #             cursor.execute(query)
        #             connection.commit()
        #     finally:
        #         connection.close()
        #
        #     return connection
        # except Exception as ex:
        #     print('Connection refused...\n')
        #     print(ex)

    # def load_db(self):
    #     try:
    #         host, user, database, password = self.data_to_connect_my_sql()
    #         connection = mysql.connector.connect(host=host,
    #                                              port=3306,
    #                                              user=user,
    #                                              database=database,
    #                                              password=password
    #                                              )
    #         print('Successfully connected...')
    #         try:
    #             letters = ascii_letters
    #             with connection.cursor() as cursor:
    #                 for x in range(1):
    #                     for i in range(10):
    #                         my_string = "".join(random.choice(letters) for i in range(4096))
    #                         cursor.execute("""
    #                         INSERT INTO accounts (name, text)
    #                         VALUES (
    #                         'lambotik',
    #                         %(my_string)s);""",
    #                                        {'my_string': my_string})
    #                     connection.commit()
    #                     print('+1000')
    #         finally:
    #             connection.close()
    #     except Exception as ex:
    #         print('Connection refused...\n')
    #         print(ex)
    #     try:
    #         host, user, database, password = self.data_to_connect_my_sql()
    #         connection = mysql.connector.connect(host=host,
    #                                              port=3306,
    #                                              user=user,
    #                                              database=database,
    #                                              password=password
    #                                              )
    #         print('Successfully connected...')
    #         try:
    #             letters = ascii_letters
    #             with connection.cursor() as cursor:
    #                 for x in range(1):
    #                     for i in range(10):
    #                         my_string = "".join(random.choice(letters) for i in range(4096))
    #                         cursor.execute("""
    #                         INSERT INTO accounts (name, text)
    #                         VALUES (
    #                         'lambotik',
    #                         %(my_string)s);""",
    #                                        {'my_string': my_string})
    #                     connection.commit()
    #                     print('+1000')
    #         finally:
    #             connection.close()
    #     except Exception as ex:
    #         print('Connection refused...\n')
    #         print(ex)


