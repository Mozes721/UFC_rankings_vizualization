from bs4 import BeautifulSoup 
import requests
import pandas as pd

wiki_url = 'https://en.wikipedia.org/wiki/Ultimate_Fighting_Championship_rankings'

response = requests.get(wiki_url)
soup = BeautifulSoup(response.text, 'html.parser')


# Headlines
# headline = soup.find_all('span', {'class': 'mw-headline'})

# # for head in headline[1:-3]:
# #     print(head.text)


tables = soup.find_all('table', {'class': 'wikitable'})[1:]

df = pd.DataFrame(data=tables)

#All tables
for i, table in enumerate(tables):
    print("#"*10 + "Table {}".format(i) + "#"*10)
    print(table.text)
    print('.'*80)
print("#"*80)


# for tn, table in enumerate(tables):
#     rows = table.find_all("tr")
#     row_lenght = [len(r.find_all(['th', 'td'])) for r in rows]
    
    
    # ncols = max(row_lenght)
    # nrows = len(rows)
    # data = []
    # for i in range(nrows):
    #     rowD = []
    #     for j in range(ncols):
    #         rowD.append('')
    #     data.append(rowD)

    # for i in range(len(rows)):
    #     row = rows[i]
    #     rowD = []
    #     cells = row.find_all(['td', 'th'])
    #     for j in range(len(cells)):
    #         cell = cells[j]

    #         #lots of cells span cols
    #         cspan = int(cell.get('colspan', 1))
    #         rspan = int(cell.get('rowspan', 1))
    #         l = 0
    #         for k in range(rspan):
    #             while data[i + k][j + l]:
    #                 l += 1
    #             for m in range(cspan):
    #                 cell_n = j + l + m
    #                 row_n = i + k
                   

    #     data.append(rowD)
# for row in rows:
#     ticker = row.find_all('td')[0].text
#     tickers.append(ticker[:-1])

# print(rows)
