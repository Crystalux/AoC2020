
import os.path
import pandas as pd
import numpy as np
import re

passports = pd.DataFrame(columns=['byr','iyr','eyr','hgt','hcl','ecl','pid','cid'])

my_path = os.path.abspath(os.path.dirname(__file__))
path = os.path.join(my_path, "../input/day04.txt")
with open(path) as f1:
    newdict={}
    for lines in f1:

        line = lines.strip()
        # if empty line
        if len(line)<1:
            passports = passports.append(newdict, ignore_index=True)
            newdict.clear()
        else:
            items = line.split()
            for item in items:
                x=re.split('[-:]', item)
                newdict[x[0]]=x[1]
    if len(newdict)!=0:
        passports = passports.append(newdict, ignore_index=True)

df = passports.copy(deep=True)
df = df.drop('cid', axis=1)
df[['byr','iyr','eyr']] = df[['byr','iyr','eyr']].astype('float64')

def partA():
    return df.dropna().shape[0]

def partB():
    dfcopy = df.copy(deep=True)
    #separating height digit from measure
    heights = pd.DataFrame()
    heights= dfcopy['hgt'].str.split(r"(\d+)([A-Za-z]+)", expand=True)
    heights.rename(columns={1:'height', 2:'UoM'}, inplace=True)
    heights.drop(columns=[0,3], inplace=True)
    dfcopy= pd.concat([dfcopy,heights], axis=1)
    dfcopy.drop(columns=['hgt'], inplace=True)
    dfcopy['height'] = pd.to_numeric(dfcopy["height"])

    for index, row in dfcopy.iterrows():
        if pd.notnull(row['byr']):
            if (row['byr']<1920 or row['byr']>2020):
                dfcopy.loc[index, 'byr'] = np.nan
        if pd.notnull(row['iyr']):
            if (row['iyr']<2010 or row['iyr']>2020):
                dfcopy.loc[index, 'iyr'] = np.nan

        if pd.notnull(row['eyr']):
            if (row['eyr']<2020 or row['eyr']>2030):
                dfcopy.loc[index, 'eyr'] = np.nan

        if pd.notnull(row['UoM']):
            if (row['UoM']=='cm'):
                if (row['height']<150 or row['height']>193):
                    dfcopy.loc[index, 'height'] = np.nan
                    dfcopy.loc[index, 'UoM'] = np.nan
            if (row['UoM']=='in'):
                if (row['height']<59 or row['height']>76):
                    dfcopy.loc[index, 'height'] = np.nan
                    dfcopy.loc[index, 'UoM'] = np.nan

        if pd.notnull(row['ecl']):
            if not(row['ecl'] in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']):
                dfcopy.loc[index, 'ecl'] = np.nan

        if pd.notnull(row['hcl']):
            if not(row['hcl'][0]=='#' and len(row['hcl'][1:])==6 and re.match('^[a-fA-F0-9_]+$', row['hcl'][1:])):
                dfcopy.loc[index, 'hcl'] = np.nan
        
        if pd.notnull(row['pid']):
            if not((len(str(row['pid']))==9) and (str(row['pid']).isnumeric())): 
                dfcopy.loc[index, 'pid'] = np.nan


    return dfcopy.dropna().shape[0]


if __name__ == "__main__":
    
    print("Part A: ", partA())
    print('='*20)
    print('Part B: ',partB())


