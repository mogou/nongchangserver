from mysql import MySQLDB


def insert(str_sql, param_list):
    command = str.format(str_sql, param_list)
    print(command)
    base_action(command)


def update(str_sql, param_list):
    command = str.format(str_sql, param_list)
    print(command)
    base_action(command)


def delete(str_sql, param_list):
    command = str.format(str_sql, param_list)
    print(command)
    base_action(command)


def find(str_sql, param_list):
    command = str.format(str_sql, param_list)
    print(command)
    base_action(command)


def base_action(str_sql):
    conn = MySQLDB.get_connect()
    if conn is not None:
        cursor = conn.cursor()
        try:
            cursor.execute(str_sql)
            conn.commit()
        except Exception as e:
            print(e)
        cursor.close()
