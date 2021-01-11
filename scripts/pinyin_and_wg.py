#%%
from pypinyin import lazy_pinyin
import pandas as pd

surnames = []
with open("surname.txt") as f:
    for line in f:
        l = line.strip().split("\t")
        surnames += l[1:]

pinyin = []
for surname in surnames:
    py = lazy_pinyin(surname)
    if len(py) == 1:
        pinyin += py
    else:
        pinyin += ["".join(py)]

df = pd.DataFrame({"chinese": surnames, "pinyin": pinyin})

# %%
wg = pd.read_csv("convert_chart/old_wade_giles.txt", sep=" ")
df = df.merge(wg, on="chinese", how="left")

df.to_csv("source/pinyin_wg.csv", index=False)
