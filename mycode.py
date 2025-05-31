
import os
import pandas as pd

# <-------- initial datafile ------------->
info = {
    "Name" : ["Yasin","Arafat","Yasin Arafat"],
    "Age"  : [25,30,35],
    "City" : ["Savar","Dhaka","Jamalpur"]
}
df = pd.DataFrame(data=info)



# <--------- save the data ------------>
data_dir = 'data'
os.makedirs(name=data_dir,exist_ok=True)

file_path = os.path.join("data","sample_data_v1.csv")
df.to_csv(path_or_buf=file_path,index=False)
print(f"csv file is saved in file path: {file_path}")