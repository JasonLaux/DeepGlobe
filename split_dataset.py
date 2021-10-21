from glob import glob
import pandas as pd
import os 

dataset_path = glob(".\\Road_Extraction_Dataset\\*")
# print(len(dataset_path)) # 6226 images + 6226 masks
counter = 0
temp = "train"
meta_data = pd.DataFrame(columns = ["split", "sat", "mask"])

for path in dataset_path:
    img_name = os.path.split(path)[-1]
    if counter > 10450:
        temp = 'test'
    if "mask" in img_name:
        meta_data.loc[counter, "split"] = temp
        meta_data.loc[counter, "mask"] = img_name
    else:
        meta_data.loc[counter - 1, "sat"] = img_name
    counter += 1


# test = meta_data[meta_data['split'] == "test"]
# print(len(test))
meta_data.to_csv('meta_data.csv', index=False)

    

    

    

