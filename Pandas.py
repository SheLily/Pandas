import pandas as pd
from pprint import pprint

def count_top3(years):
    dfs = [pd.read_csv(f'yob{year}.txt', header=None) for year in years]
    df = pd.concat(dfs, ignore_index=True)
    df = df.groupby([0, 1]).sum()
    df = df.reset_index()
    
    df.sort_values(by=[2], inplace=True)
    
    
    return df[0][-3:]
    

def count_dynamics(years):
    dfs = [pd.read_csv(f'yob{year}.txt', header=None) for year in years]
    sexes = ('F', 'M')
    dynamic = {sex: [df[2][df[1] == sex].sum()  for df in dfs] for sex in sexes}
    return dynamic


if __name__ == '__main__':
    print(count_top3([1994, 1995]))

    print(count_dynamics([1994, 1995, 1996]))
