from src.predicter import reactions_predicter
import sqlite3
import pandas as pd
def get_reactions(text: str):
    predicter = reactions_predicter()

def read_posts_from_db(database_path, column_name):
    db_con = sqlite3.connect(f"{database_path}")
    cur = db_con.cursor()
    cur.execute(f"""
        SELECT post_id, post_text
        FROM '{column_name}'
        ORDER BY post_id
    """)
    data = pd.DataFrame(cur.fetchall(), columns=['post_id','post_text', 'views'])
    data = data.iloc[1:, :]
    data = data.set_index('post_id')
    print(data.head(5))
def main():
    read_posts_from_db("./db/database.db", 'posts')