#%%[markdown]
#### Nutritional information from openfoodfacts
# %%
import os
import pandas as pd
import numpy as np
import openfoodfacts
from sqlalchemy import create_engine, text
from dotenv import load_dotenv, find_dotenv

#%%
load_dotenv(find_dotenv())

SQLALCHEMY_DATABASE_URL = os.environ["cockroack_db_deta_connect_string"]

engine = create_engine(SQLALCHEMY_DATABASE_URL)

# %%
barcodes = pd.read_csv("Scan session.csv", header=None).T.to_numpy().tolist()[0]
np.savetxt("food_barcodes.csv", barcodes + [5411188512271, 8718403014549], delimiter=",", fmt='%s')
barcodes = pd.read_csv("food_barcodes.csv", header=None).T.to_numpy().tolist()[0]
# %%
np.array(barcodes)
# %%
all_foods_df = pd.DataFrame()
failed_barcodes = list()
for barcode_int in barcodes:
    barcode=str(barcode_int)
    try:
        search_result = openfoodfacts.products.get_product(barcode)
        food_df = pd.concat([pd.DataFrame({"product_name":search_result["product"]["product_name"],
                                          "barcode":barcode}, index=[0]), 
                         pd.DataFrame(search_result["product"]["nutriments"], index=[0])], axis=1)
        all_foods_df = pd.concat([all_foods_df, food_df])
    except:
        print(f"Barcode == {barcode} not available in the database")
        failed_barcodes.append(barcode_int)
_ = all_foods_df.reset_index(inplace=True, drop=True)
# %%
foods_subset_df = (all_foods_df
.filter(regex="product_name|barcode|100g")
.drop("energy_100g", axis=1))
# %%
foods_subset_df.head()
# %%
# quick print statement check
# with engine.connect() as conn:
#     result = conn.execute(text("SELECT * FROM nutritional_information"))
#     print(result.all())
# %%
# upload data frame to SQL (be aware of the if_exists)
# with engine.connect() as conn:
#     foods_subset_df.to_sql('nutritional_information', 
#     con=conn, 
#     if_exists='append')
# %%
nut_info_df = pd.read_sql_table("nutritional_information", 
                                con=engine, index_col=[0])
display(nut_info_df)
nut_info_df.info()
# %%
