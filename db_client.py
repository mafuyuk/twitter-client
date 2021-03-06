import psycopg2

class DBClient:
    def __init__(self, config):
        self.dsn = "postgresql://"+config["user"]+":"+config["password"]+"@"+config["host"]+":"+config["port"]+"/moya4"

    def __get_connection(self):
        return psycopg2.connect(self.dsn)

    def getUser(self, user_id):
        print("getUser")
        query = "select * from users where twitter_user_id=%s"

        with self.__get_connection() as conn:
            with conn.cursor() as cur:
                cur.execute(query, (user_id,))
                return cur.fetchone()

    def createUser(self, user_id, wallet_address):
        print("createUser")
        query = "insert into users (twitter_user_id, wallet_address) values (%s, %s)"

        with self.__get_connection() as conn:
            with conn.cursor() as cur:
                cur.execute(query, (user_id, wallet_address))
            conn.commit()

    def updateUserCultivationCoins(self, user_id, cultivation_coins):
        print("updateUserCultivationCoins")
        query = "update users set cultivation_coins = %s ,updated_at = now() where twitter_user_id = %s"

        with self.__get_connection() as conn:
            with conn.cursor() as cur:
                cur.execute(query, (cultivation_coins, user_id))
            conn.commit()

