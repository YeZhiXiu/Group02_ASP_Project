import pandas as pd

Asia03 = pd.read_excel("IMVA.xls", sheet_name="IMVA")
print(Asia03)
print(Asia03.columns)

df_AsiaCountries03 = Asia03[['Periods', 'Brunei Darussalam', 'Indonesia', 'Malaysia', 'Myanmar', 'Philippines', 'Thailand',
            'Vietnam', 'China','Hong Kong SAR', 'Taiwan', 'Japan', 'South Korea', 'Bangladesh', 'India', 'Pakistan',
            'Sri Lanka', 'Iran', 'Kuwait', 'Israel','Saudi Arabia', 'United Arab Emirates']]
print(df_AsiaCountries03.columns)

new = df_AsiaCountries03['Periods'].str.split(" ", n=1, expand=True)
df_AsiaCountries03 = df_AsiaCountries03.assign(Year=new[0])

print("       ▬▬ι═══════ﺤ ☾☾☾ Splitted Year ☽☽☽ -═══════ι▬▬")
df_AsiaCountries03["Year"] = pd.to_numeric(df_AsiaCountries03["Year"])
pd1 = df_AsiaCountries03["Year"].dtypes
print("Year type is", pd1)

print("      ▬▬ι═══════ﺤ ☾☾☾ dropped periods ☽☽☽ -═══════ι▬▬")
print(df_AsiaCountries03.drop(["Periods"], axis=1))
df_AsiaCountries33 = df_AsiaCountries03[(df_AsiaCountries03["Year"] >= 1998) & (df_AsiaCountries03["Year"] <= 2007)]

print("▬▬ι═══════ﺤ ☾☾☾ Singapore Visitors First & Last Three Year Dataframe ☽☽☽ -═══════ι▬▬")
print(df_AsiaCountries33.head(3))
print(df_AsiaCountries33.tail(3))

df_AsiaCountries04 = df_AsiaCountries33[['Brunei Darussalam', 'Indonesia', 'Malaysia', 'Myanmar', 'Philippines', 'Thailand',
            'Vietnam', 'China','Hong Kong SAR', 'Taiwan', 'Japan', 'South Korea', 'Bangladesh', 'India', 'Pakistan',
            'Sri Lanka', 'Iran', 'Kuwait', 'Israel','Saudi Arabia', 'United Arab Emirates']]
print("       ▬▬ι═══════ﺤ ☾☾☾ df_AsiaCountries04 ☽☽☽ -═══════ι▬▬")
print(df_AsiaCountries04)
print("sorted")

df_AsiaCountries05 = df_AsiaCountries04.replace(",", "", regex=True)
df_AsiaCountries06 = df_AsiaCountries05.replace("na", "0", regex=True)

print("▬▬ι═══════ﺤ ☾☾☾ df_AsiaCountries05 ☽☽☽ -═══════ι▬▬")
print(df_AsiaCountries06)
df_AsiaCountries07 = df_AsiaCountries06.astype(int)
print(df_AsiaCountries07.dtypes)
psNotSorted=df_AsiaCountries07.sum()
psSorted = df_AsiaCountries07.sum().sort_values(ascending=False)

print("▬▬ι═══════ﺤ ☾☾☾ sorted ☽☽☽ -═══════ι▬▬")
print(psSorted)
allCountries = psSorted

print("▬▬ι═══════ﺤ ☾☾☾ Top 3 countries ☽☽☽ -═══════ι▬▬")
top3countries = psSorted.head(3)
print(top3countries)
total=top3countries.values.sum()
mean=round(top3countries.values.mean(),2)

print("The total no. of visitors for the top 3 countries is ",total)
print("The mean value for the top 3 countries is ",mean)

import matplotlib.pyplot as plt
import numpy as np

indexAll = np.arange(len(allCountries.index))


plt.figure(figsize=(10, 10))
plt.xlabel("Countries", fontsize=8)
plt.ylabel("No. of Travellers (in thousands)", fontsize=8)
plt.xticks(indexAll, allCountries.index, fontsize=6, rotation=30)
plt.title("▬▬ι═══════ﺤ ☾☾☾ Visitors From Asia Countries To Singapore (1998-2007) ☽☽☽ -═══════ι▬▬")
plt.bar(allCountries.index, allCountries.values / 1000)
plt.show()

class Cliff:
    #Read Dataframe
    Asia3 = pd.read_excel('IMVA.xls', sheet_name='IMVA')
    print(Asia3)
    print(Asia3.columns)

    #Print Dataframe and Column headers
    Asia3_Country = Asia3[
        ['Periods','Brunei Darussalam','Indonesia','Malaysia','Myanmar','Philippines','Thailand','Vietnam',
        'China','Hong Kong SAR','Taiwan','Japan','South Korea','Bangladesh','India','Pakistan','Sri Lanka','Iran','Kuwait'
        ,'Israel','Saudi Arabia','United Arab Emirates']]
    print(Asia3_Country.columns)

    #Country of Asia
    Asia = Asia3_Country['Periods'].str.split(' ', n=1, expand=True)
    Asia3_Country = Asia3_Country.assign(Year=Asia[0])
    print('       ->>>>>佛<<<<<- Years Split ->>>>>佛<<<<<-')

    Asia3_Country['Year'] = pd.to_numeric(Asia3_Country['Year'])
    app = Asia3_Country['Year'].dtypes
    print("Integer of year =", app)
    print("      ->>>>>佛<<<<<- Periods Dropped ->>>>>佛<<<<<-")
    print(Asia3_Country.drop(['Periods'], axis=1))
    #Range 1998 to 2007
    Asia3_C = Asia3_Country[(Asia3_Country['Year'] >= 1998) & (Asia3_Country['Year'] <= 2007)]
    print('     ->>>>>佛<<<<<- Singapore Visitors First & Last Three Year Dataframe ->>>>>佛<<<<<-')
    print(Asia3_C.head(3))
    print(Asia3_C.tail(3))

    ASIA3_DF = Asia3_C[
        ['Brunei Darussalam','Indonesia','Malaysia','Myanmar','Philippines','Thailand','Vietnam',
         'China','Hong Kong SAR','Taiwan','Japan','South Korea','Bangladesh','India','Pakistan','Sri Lanka','Iran','Kuwait',
         'Israel','Saudi Arabia','United Arab Emirates']]
    print('Asia3_C')
    print(ASIA3_DF)

    ASIA3_DF1 = ASIA3_DF.replace(',', '', regex=True)
    ASIA3_DF2 = ASIA3_DF1.replace('na', '0', regex=True)
    print('      ->>>>>佛<<<<<- ASIA3_DF ->>>>>佛<<<<<-')
    print(ASIA3_DF2)

    ASIA3_DF3 = ASIA3_DF2.astype(int)
    print(ASIA3_DF3.dtypes)
    asiaSort = ASIA3_DF3.sum().sort_values(ascending=False)
    print('->>>>>佛<<<<<- Sorted Values ->>>>>佛<<<<<-')
    print(asiaSort)
    print('->>>>>佛<<<<<- Top Three countries ->>>>>佛<<<<<-')
    topthreeasia = asiaSort.head(3)
    print(topthreeasia)
    total = topthreeasia.values.sum()
    mean = round(topthreeasia.values.mean(), 2)
    print("The total number of visitors for the top 3 countries is ", total)
    print("The mean value for the top three countries is ", mean)
    index = np.arange(len(topthreeasia.index))
    plt.figure(figsize=(10, 10))
    plt.xlabel('Countries', fontsize=8)
    plt.ylabel('No. of Travellers (in thousands)', fontsize=8)
    plt.xticks(index, topthreeasia.index, fontsize=6, rotation=30)
    plt.title('Top Three Visited Asian Countries (1998-2007)')
    plt.bar(topthreeasia.index, topthreeasia.values / 1000)
    plt.show()
