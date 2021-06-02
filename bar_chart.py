import matplotlib.pyplot as plt
import mplcursors
import pandas as pd
import numpy as np
import re

def bar_graph(sheet):
    print("Found sheet by the name of " + sheet)
    #get just the fighter and the record
    sheet_name = pd.read_excel("UFC_rankings.xlsx", sheet_name=sheet)
    #get top 10
    top10 = sheet_name.head(11) 
    #change to Dataframe
    df = pd.DataFrame(top10)
    figher_array = []
    record = []
    #assign dataframe values in its corresponding array variable
    for index, row in df.iterrows():
        print(row["Fighter"], row["Record"])
        figher_array.append(row["Fighter"])
        #use regex to just allow numbers being passed in otherwise whitespace it
        record.append(re.sub('[^0-9]',' ', row["Record"]))

    print(record)

    wins = []
    losses = []
    #loop through record and where there is widespace assing win and loose value by 0 and 1 index
    for won in record:
        wins.append(won.split(' ')[0])
    for loss in record:
        losses.append(loss.split(' ')[1])
    print(wins)
    print(losses)
    

    # #change to integers
    record_wins = [int(x) for x in wins]
    record_losses = [int(x) for x in losses]
    
    #two iterables are passed in
    record = zip(record_wins, record_losses)

    ypos= np.arange(len(figher_array))
    plt.rcParams.update({'font.size': 10})

    plt.title(sheet)
    plt.xticks(ypos, figher_array)
    plt.xlabel("Fighters")
    plt.ylabel("UFC Record")
    wins = plt.bar(ypos - 0.2, record_wins, 0.4, label = "Wins", color="g")
    losses = plt.bar(ypos + 0.2, record_losses, 0.4, label = "Losses", color="r")
    plt.tight_layout()
    plt.legend()
    mplcursors.cursor((wins, losses))
    plt.show()
 
