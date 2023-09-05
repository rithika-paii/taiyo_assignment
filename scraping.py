# %%
import requests
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import bs4
import re
import seaborn as sns

# %%
res = requests.get("https://www.bea.gov/news/2023/personal-income-and-outlays-july-2023")
res.text

# %%
soup= bs4.BeautifulSoup(res.text, "lxml")

# %%
title = soup.title
print(title)
print(title.text)

# %%
links = soup.find_all('a', href=True)
for link in links:
    print(link['href'])

# %%
data = []
allrows = soup.find_all("tr")
for row in allrows:
    row_list = row.find_all("td")
    dataRow =[]
    for cell in row_list:
        dataRow.append(cell.text)
    data.append(dataRow)
data = data[1:]
print(data[-2:])

# %%
df = pd.DataFrame(data)
print(data)

# %%
df = pd.DataFrame(data)
print(df.head())
print(df.tail())

# %%
df = df.fillna("N/A")

# %%
df = df.drop_duplicates()

# %%
header_list =[]
col_headers = soup.find_all("th")
for col in col_headers:
    header_list.append(col.text)
print(header_list)

# %%
df.shape

# %%
df.describe

# %%
df.columns

# %%
df.to_csv(r'D:\rithika\web_scraping\taiyoai_assignment\data.csv', header = True, index = False)

# %%
df = pd.read_csv("data.csv")

# %%
df.head()

# %%



