import mysql.connector
import pandas as pd
import config
import sentiment_analysis
import classification 
def connexion():
    con= mysql.connector.connect(
        host=config.HOST,
        user=config.USER,
        password=config.PASSWORD,
        database=config.DATABASE,
        auth_plugin='mysql_native_password'
    )
    return con
def run(con):
    cur=con.cursor()
    df=pd.read_csv(config.DATA_FILE)
    for i in range(df.shape[0]):
        id_groupe=filter.inference.run(df['comment'])
        if id_groupe!=0:
            score, sentiment=sentiment_analysis.interference.run(df['comment'])
            id_class= classification.inference.run(df['comment'])
            sql = "INSERT INTO data (date, comment, id_source, score, sentiment, id_class, id_groupe) VALUES (%s, %s, %s, %s, %s, %s, %s)"
            val = (df['date'], df['comment'], df['id_source'], score, sentiment, id_class, id_groupe)
            cur.execute(sql, val)
            con.commit()
if __name__ == "__main__":
    run(connexion())