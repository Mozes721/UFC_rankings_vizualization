from bs4 import BeautifulSoup 
import requests
import pandas as pd

wiki_url = 'https://en.wikipedia.org/wiki/Ultimate_Fighting_Championship_rankings'

response = requests.get(wiki_url)
soup = BeautifulSoup(response.text, 'html.parser')



# Headlines
headline = soup.find_all('span', {'class': 'mw-headline'})

# for head in headline[1:-3]:
#     print(head.text)


tables = soup.find_all('table', {'class': 'wikitable'})

for table in tables[1:2]:
    rows = table.find_all('tr')
    columns = [v.text.replace('\n', '') for v in rows[0].find_all('th')]
    df = pd.read_html(str(table))
    df = pd.DataFrame(df[0])
print(df.head())
    # for i in rows[1:]:
    #     tds = rows[i].find_all('td')

    #     values = [tds[0].text, tds[1].text, tds[2].text, '', tds[4].text, tds[5].text]
#     #     row = [v.text.replace('\n', '') for v in row.find_all('th')]
#     #     print(row)
# df = pd.DataFrame(columns=columns)
# row_values = []
# for table in tables[1:2]:
#     rows = table.find_all('td')
#     row = [v.text.replace('\n', '') for v in rows]
#     if len(row) == 6:
#         row_values.append(row)

    
#     print(columns)
#     print(row_values)
# print(df)

# for i in range(1, len(rows)):
#     tds = rows[1].find_all('td')

#     # if len(tds) == 6:
#     #     values = [tds[0].text, tds[1].text, tds[2].text, '', tds[4].text, tds[5].text]
#     # else:

#     print(tds)

