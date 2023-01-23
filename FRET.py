import pandas as pd
import csv
main_df = pd.read_csv('T1 pH 7.0 Ensemble Run 3.csv') # Change the name to the directory location of the CSV data
FRET_E = main_df[["ID", "Frame index", "FRET efficiency"]]
new_FRET_E = FRET_E[FRET_E["FRET efficiency"] != 0]
id_tag = 0
id_dict = {}
max_id = new_FRET_E["ID"].max()
while id_tag <= max_id: # Calculates the average FRET efficiency values of each trace detected by the ONI machine
    fretcalc = new_FRET_E[new_FRET_E["ID"] == id_tag]
    fretmean = fretcalc["FRET efficiency"].mean()
    id_dict.update({f"{fretmean}":f"{id_tag}"})
    id_tag += 1

for i in id_dict.values():
    if i == "nan":
        id_dict.pop(i)
# id_dict.pop(f"{max_id - 1}")
id_dict = dict((v,k) for k,v in id_dict.items())
with open('T1E4run3_fretmean.csv', 'w') as f: # Rename the new CSV sheet 
    w = csv.DictWriter(f, id_dict.keys())
    w.writeheader()
    w.writerow(id_dict)

# CODE BELOW HERE IS NOT TO BE USED
# # Rename keys in id_dict to numbers from 1 to the number of items in the dictionary
# plot_dict = {}
# counter = 0
# tracker = 0
# print(type(max(id_dict.keys())))
# while counter <= int(max(id_dict.keys())):
#     if tracker in id_dict.keys():
#         plot_dict[f"{tracker}"] = id_dict[f"{tracker}"]
#         counter += 1
#     else:
#         tracker += 1

# # # Create a dataframe to generate a plot from
# plot_df = pd.DataFrame(plot_dict.items(), columns = ['Trace number', 'Average FRET efficiency'])
# print(plot_df)
