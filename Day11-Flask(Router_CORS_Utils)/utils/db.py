import mysql.connector

def getConnection():
    return mysql.connector.connect(
        host = "localhost",
        port = 3306,
        user = "root",
        password = "root",
        database = "edu",
        use_pure = True
    )

def executeQuery(sql, params):
    with getConnection() as con:
        with con.cursor(dictionary=True) as cur:
            cur.execute(sql, params)
            if cur.description:
                return cur.fetchall()
            else:
                con.commit()
                return {
                    "affectedRows": cur.rowcount
                }