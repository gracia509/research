# pip install XlsxWriter

import pandas as pd
import glob


all_data = pd.DataFrame()
for f in glob.glob("../ment*.xlsx"):
    df1 = pd.read_excel(f,sheetname='data')
    #xl = pd.ExcelFile(f)
    #df1 = xl.parse('data')
    all_data = all_data.append(df1)

all_data.head()

#write data to excel
writer = pd.ExcelWriter('MentCombined.xlsx',engine='xlsxwriter')
all_data.to_excel(writer,'Sheet1', index=False)
writer.save()

#write data to csv
all_data.to_csv("MentCombined.csv", index=False)
