import pymysql as db




class DD(object):

    def __init__(self):
        self._conn = None

    def __link_mysql(slef, _host, _user, _password, _database, _charset="utf8"):
        try:
            return db.connect(host=_host, user=_user, password=_password, database=_database, charset=_charset)
        except Exception as e:
            print(e)
        return None


    def get_connect(slef):
        if slef._conn is None:
            slef._conn = slef.__link_mysql("47.98.233.255", "nongchang", "Hiahia233!", "zxx")
        return slef._conn

