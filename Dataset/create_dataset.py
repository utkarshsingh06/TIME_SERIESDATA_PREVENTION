from pathlib import Path
import sys
import pandas as pd
dataset_to_split = sys.argv[0]
path = Path(dataset_to_split)
time_series = pd.read_csv(path)
print(time_series)
# num_row_list = list(map(int, sys.argv[2:])) # cast to int an entire list
# for num_row in num_row_list:
#     dataset = time_series.head(num_row)
#     dataset = dataset + 1 
#     dataset_abs = dataset.abs()
#     name_file = "Facebook_Economy_final_" + str(num_row) + ".csv"
#     dataset_abs.to_csv(path.parent / name_file, index=False)

