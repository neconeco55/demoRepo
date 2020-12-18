import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import io
import requests
# pd.set_option("display.max_columns", all=True)

url = 'https://raw.githubusercontent.com/fivethirtyeight/data/master/fandango/fandango_score_comparison.csv'
download = requests.get(url).content
fandango = pd.read_csv(io.StringIO(download.decode("utf-8")))
# df_url = pd.read_csv(url, error_bad_lines=False)


# print(fandango.columns)
#gecici olarak bazi columnn lari siliyoruz ve istediklerimizi tutuyoruz
cols = ['FILM', 'RT_user_norm', 'Metacritic_user_nom', 'IMDB_norm', 'Fandango_Ratingvalue', 'Fandango_Stars']
new_fandango = fandango[cols]
num_cols = ['RT_user_norm', 'Metacritic_user_nom', 'IMDB_norm', 'Fandango_Ratingvalue', 'Fandango_Stars']
print("new fandango len")

# bar_widths = new_fandango[cols].iloc[0].values
# x = fandango[cols].loc[0].values
# print(bar_widths)

# print(new_fandango.iloc[0])
# num_cols = ['RT_user_norm', 'Metacritic_user_nom', 'IMDB_norm', 'Fandango_Ratingvalue', 'Fandango_Stars']
#
# bar_heights = fandango[num_cols].iloc[0].values
# print(bar_heights)
# print(new_fandango.iloc[:,].values)
#bar plot
#generate a single subplot annd return the figure and axes obj
# fig, ax = plt.subplot()
# ax.bar()
# plt.show()

arr = np.random.randint(1,10)

raw_data = {'first_name': ['Jason', 'Ali', 'Tina', 'Jake', 'Amy'],
            'last_name': ['Miller', 'Veli', np.nan, 'Milner', 'Cooze'],
            'age': [42, 11, 36, 24, 73],
            'preTestScore': [arr],
            'postTestScore': [25, 250, 57, np.nan, np.nan]}
emp = pd.read_csv("employees.csv", index_col="First Name")

print((emp.Team[0]))
pd.DataFrame(raw_data)

marketing = emp[emp.Team == "Marketing"]

#retrieveing column
# raw_data_df = pd.DataFrame(raw_data)
# plt.plot(raw_data_df.age, raw_data_df.preTestScore)
#retrieveing column
# plt.bar(raw_data_df.age, raw_data_df.preTestScore)

# raw_data_df.plot(x="first_name" ,y="age")
# plt.xticks(rotation=90)
# print(emp)
# print(emp.isnull().sum())
# print(emp.dtypes)
# print(emp.columns)
# plt.style.use('fivethirtyeight')
# emp.plot(y="Salary")
# print(emp[["Salary", "Bonus %"]])
# plt.show()
# bar_p = np.arange(10) + 0.20
# print(bar_p)


# emp = emp.dropna(inplace=True)
# print(emp.isnull().sum())


#duplicate values, NAN values, missing values
# df = pd.DataFrame(raw_data)
# print(df)
# print(df.isnull().sum())
# df.dropna(inplace=True, axis=0)
# print(df)
#
# df.set_index("age", inplace=True)
# print(df)


# data cleaning processes
# 1- drop irrelvannt columns
# 2- renaming column names meaingfully
# 3- making data consistent
# 4- imputtig missing values
# 5-