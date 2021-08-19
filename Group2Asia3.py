import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
class Asia:
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
    print('***** Years Split *****')

    Asia3_Country['Year'] = pd.to_numeric(Asia3_Country['Year'])
    app = Asia3_Country['Year'].dtypes
    print("Integer of year =", app)
    print("***** Periods Dropped ***** ")
    print(Asia3_Country.drop(['Periods'], axis=1))
    #Range 1998 to 2007
    Asia3_C = Asia3_Country[(Asia3_Country['Year'] >= 1998) & (Asia3_Country['Year'] <= 2007)]
    print('***** Asia3_Country *****')
    print(Asia3_C)

    ASIA3_DF = Asia3_C[
        ['Brunei Darussalam','Indonesia','Malaysia','Myanmar','Philippines','Thailand','Vietnam',
         'China','Hong Kong SAR','Taiwan','Japan','South Korea','Bangladesh','India','Pakistan','Sri Lanka','Iran','Kuwait',
         'Israel','Saudi Arabia','United Arab Emirates']]
    print('Asia3_C')
    print(ASIA3_DF)

    print('***** sorted *****')

    ASIA3_DF1 = ASIA3_DF.replace(',', '', regex=True)
    ASIA3_DF2 = ASIA3_DF1.replace('na', '0', regex=True)
    print('***** ASIA3_DF *****')
    print(ASIA3_DF2)

    ASIA3_DF3 = ASIA3_DF2.astype(int)
    print(ASIA3_DF3.dtypes)
    asiaSort = ASIA3_DF3.sum().sort_values(ascending=False)
    print('********** Sorted Values *********')
    print(asiaSort)
    print('********* Top Three countries *********')
    topthreeasia = asiaSort.head(3)
    print(topthreeasia)
    totalsum = topthreeasia.values.sum()
    meancount = round(topthreeasia.values.mean(), 2)
    print("The total number of visitors for the top 3 countries is ", totalsum)
    print("The mean value for the top three countries is ", meancount)
    index = np.arange(len(topthreeasia.index))
    plt.figure(figsize=(10, 10))
    plt.xlabel('Asia Countries', fontsize=8)
    plt.ylabel('No. of Travellers (in thousands)', fontsize=8)
    plt.xticks(index, topthreeasia.index, fontsize=6, rotation=30)
    plt.title('Top three countries of ASIA3')
    plt.bar(topthreeasia.index, topthreeasia.values / 1000)
    plt.show()
