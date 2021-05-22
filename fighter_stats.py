import matplotlib.pyplot as plt
from openpyxl import Workbook
import pandas as pd
import numpy as np

mpp = pd.read_excel("UFC_rankings.xlsx", sheet_name="Men's pound-for-pound")

#get just the fighter and Record
menspp = mpp.iloc[:, 1:3]


# print(menspp.iloc[0])

fighter = menspp.iloc[0][0]
record = menspp.iloc[0][1]
print(fighter + ' ' + record)

won = record.split()[0][0:2]
lost = record.split()[0][3:4]
score = int(won), int(lost)
# print(score)
colors = ['tab:green', 'tab:red']
explode = [0.1, 0]

fig, ax = plt.subplots(figsize=(6, 3), subplot_kw=dict(aspect="equal"))

array_score = np.asarray(score)
labels = ["wins", "losses"]


def func(pct, allvals):
    absolute = int(round(pct/100.*np.sum(allvals)))
    return "{:.1f}%\n({:d})".format(pct, absolute)


wedges, texts, autotexts = ax.pie(array_score, autopct=lambda pct: func(pct, array_score),
                                  textprops=dict(color="w"), explode=explode)


ax.legend(wedges, labels,
          title="Score",
          loc="center left",
          bbox_to_anchor=(1, 1))
texts[0].set_fontsize(10)

plt.setp(autotexts, size=8, weight="bold")


ax.set_title(fighter)


plt.show()
