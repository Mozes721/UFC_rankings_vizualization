import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import re

def pie_chart(sheet):
    print("Found sheet by the name of " + sheet)
    sheet_name = pd.read_excel("UFC_rankings.xlsx", sheet_name=sheet)

    df = pd.DataFrame(sheet_name)
    figher_array = []
    record = []
    #assign dataframe values in its corresponding array variable
    print("#"*10)
    for index, row in df.iterrows():
        print(row["Fighter"])
        figher_array.append(row["Fighter"])
        #use regex to just allow numbers being passed in otherwise whitespace it
    print("#"*10)
    running = True
    while running:
        fighter = input("Please choose a fighter from this list: ")
        if fighter in figher_array:
            print("You selected %s the pie graph will be displayed shortly..." % fighter)
            running = False
        else:
            print("Try again...")
    record = []
    for index, row in df.iterrows():
        if fighter in row["Fighter"]:
            record.append(re.sub('[^0-9]',' ', row["Record"]))
    
    wins = []
    losses = []
    #loop through record and where there is widespace adding win and loose value by 0 and 1 index
    for won in record:
        wins.append(won.split(' ')[0])
    for loss in record:
        losses.append(loss.split(' ')[1])
    
    # #change to integers
    record_wins = [int(x) for x in wins]
    record_losses = [int(x) for x in losses]

    record = zip(record_wins, record_losses)
    fighter_record = list(record)
    
    ####DISPLAY THE DATA ON PIE CHART####
    explode = [0.1, 0]

    fig, ax = plt.subplots(figsize=(12, 6), subplot_kw=dict(aspect="equal"))

    array_score = np.asarray(fighter_record[0])
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

