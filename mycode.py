
import os
import pandas as pd

# <-------- initial datafile V1 ------------->
info = {
    "Name" : ["Yasin","Arafat","Yasin Arafat"],
    "Age"  : [25,30,35],
    "City" : ["Savar","Dhaka","Jamalpur"]
}
df = pd.DataFrame(data=info)

# <-------- Add new  data: V2 ------------->
new_row_loc = {"Name":"GF1","Age":22,"City":"Dhaka"}
df.loc[len(df.index)] = new_row_loc

# <--------- save the data ------------>
data_dir = 'data'
os.makedirs(name=data_dir,exist_ok=True)

file_path = os.path.join("data","sample_data_v1.csv")
df.to_csv(path_or_buf=file_path,index=False)
print(f"csv file is saved in file path: {file_path}")

