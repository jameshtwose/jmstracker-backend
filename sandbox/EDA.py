#%%
import os
import pandas as pd
from sqlalchemy import create_engine, text
from dotenv import load_dotenv, find_dotenv

#%%
SQLALCHEMY_DATABASE_URL = os.environ["cockroack_db_deta_connect_string"]

engine = create_engine(SQLALCHEMY_DATABASE_URL)
# %%
# with engine.connect() as conn:
#     result = conn.execute(text("SELECT * FROM jmstracker_backend"))
#     print(result.all())

#%%
# with engine.connect() as conn:
#     result = conn.execute(text('DROP TABLE IF EXISTS jmstracker_backend;'))
#%%
jmstracker_backend_df = pd.read_sql_table("jmstracker_backend", con=engine)
display(jmstracker_backend_df)
jmstracker_backend_df.info()
# %%
# posts_df = pd.read_sql_table("posts", con=engine)
# display(posts_df)
# posts_df.info()
# %%
todos_df = pd.read_sql_table("todos", con=engine)
display(todos_df)
todos_df.info()
# %%
users_df = pd.read_sql_table("users", con=engine)
display(users_df)
users_df.info()
# %%
