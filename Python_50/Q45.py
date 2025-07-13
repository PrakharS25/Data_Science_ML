# Accept a CSV file and convert it into a list of dictionaries.
import csv

with open(r"D:\Documents\Ds_Ml\sales_data_sample.csv", "r") as f:
    reader = csv.DictReader(f)
    data = list(reader)

print(data)