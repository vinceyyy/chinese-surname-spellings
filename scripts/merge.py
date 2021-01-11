import pandas as pd

py = pd.read_csv("source/pinyin_wg.csv")
df = pd.read_csv("source/汉姓罗马音标注.csv")

for index, row in df.iterrows():
    base = row["chinese"]
    target = py[py["chinese"] == base]
    wg = target["wade_giles"].to_list()
    if len(wg) > 0 and type(wg[0]) is str:
        df.loc[index, "wade_giles"] = "/".join(list(set(wg)))

df.to_csv("output.csv", index=False)
