import csv
import re

# cleaning the data
f = open("data/listings.csv", "r")
f_new = open("data/listings_clean.csv", "w")

data = csv.DictReader(f)
data = list(data)

# header line
header = dict(data[0])
header.pop("description")
header.pop("neighbourhood_group_cleansed")
header.pop("bathrooms")
header.pop("amenities")
for k in header.keys():
    if str(k) == "reviews_per_month":
        f_new.write(str(k))
    else:
        f_new.write(str(k) + ",")
f_new.write("\n")

# rest of data
for row in data:
    row = dict(row)
    row.pop("description")
    row.pop("neighbourhood_group_cleansed")
    row.pop("bathrooms")
    row.pop("amenities")
    for key, value in row.items():
        k = str(key)
        v = str(value)
        if row['id'] == "4845861": # this entry was causing issues
            row["host_about"] = "J'ai l'esprit casanier et l'instinct voyageur Victor Hugo  I like to travel mostly for the preservation of biodiversity specially for the wildlife in Africa and i enjoy to take photographies_ one of my favorite hobby and passion !"
        if v == "N/A":
            v = "NaN"
        if v == "":
            v = "NaN"
        if "," in str(v):
            v = str(v).replace(",", "_")
        if "\r" in str(v):
            v = str(v).replace("\r", " ")
        if "\n" in str(v):
            v = str(v).replace("\n", " ")
        if '"' in v:
            #v = v.replace("'", " ")
            v = re.sub(r'"', ' ', v)
        if "'" in v:
            #v = v.replace("'", "-")
            v = re.sub(r"'", '-', v)
        if k == "reviews_per_month":
            f_new.write(str(v).strip())
        else:
            f_new.write(str(v) + ",")
    f_new.write("\n")