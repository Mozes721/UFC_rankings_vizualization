import matplotlib.pyplot as plt
from openpyxl import Workbook, load_workbook
import pandas as pd
import numpy as np
import re

def bar_graph(sheet):
#get just the fighter and Record
    pvp = sheet.iloc[:, 1:3]
    top10 = pvp.head(11)
    #change to Dataframe
    pvpdf = pd.DataFrame(top10)

                #adjust record values in dataframe
    pvpdf.applymap(lambda x: re.sub("\(.*?\)", "", x))
    pvpdf.head()

    figher_array = []
    record = []
    #assign dataframe values in its corresponding array variable
    for index, row in pvpdf.iterrows():
        print(row["Fighter"], row["Record"])
        figher_array.append(row["Fighter"])
        record.append(row["Record"])

    records = [x.strip(' ') for x in record]
    wins = []
    losses = []
    for won in records:
        wins.append(won[0:2])
    for loss in records:
        losses.append(loss[-1])
    print(wins)

    #     #change to integers
    record_wins = [int(x) for x in wins]
    record_losses = [int(x) for x in wins]

    #change to integers
    record_wins = [int(x) for x in wins]
    record_losses = [int(x) for x in losses]

    #no iterateors are passed
    record = zip()
    #two iterables are passed in
    record = zip(record_wins, record_losses)

    # Converting iterator to set
    fighter_records = list(record)
    print(fighter_records)

    # for line in open(wins):
    #             if line.find == '-':
    #                 line.split()
    #             record_wins.append(int(line))
    #         record_losses = []
    #         for line in open(losses):
    #             record_losses.append(int(line))

    #                     no iterateors are passed
    #         record = zip()
    #             #two iterables are passed in
    #         record = zip(record_wins, record_losses)

    #         # Converting iterator to set
    #         fighter_records = list(record)

    #         ypos = np.arange(len(figher_array))
    #         plt.rcParams.update({'font.size': 22})

    #             #bar plot
    #             #f, ax = plt.subplots(figsize=(22,5))
    #         plt.title(sheet)
    # plt.xticks(rotation='vertical')
    # plt.xlabel("Fighters")
    # plt.ylabel("UFC Record")
    # plt.xticks(ypos, figher_array)
    # plt.bar(ypos - 0.2, record_wins, 0.4, label = 'Wins', color='g')
    # plt.bar(ypos + 0.2, record_losses, 0.4, label = 'Losses', color='r')
    # plt.legend()
    # plt.show()
    

