import pandas as pd

data = pd.read_csv("data.csv")

comp_account = {
    'xyz': ['abc', 'bbc'] 
}

ls_comp = ['xyz']
ls_acc = ['abc', 'bbc']

## Part One
df = data.groupby(['AccountId', 'AsofDt'])[['MktVl']].sum().unstack('AccountId') 
df.columns = list(df.columns.get_level_values(1))
df.index = pd.to_datetime(df.index)
df.sort_index(inplace=True)
for cc in ls_comp:
    df[cc] = df.loc[:,comp_account[cc]].sum(1)
df.fillna(method='ffill', inplace=True)
df = df.pct_change()


## Part Two (1 of 2: if no previous date report -- segment tree)

#For daily bu

#


## Part Two (2 of 2: use previous report)




