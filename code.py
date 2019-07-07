# --------------
#Importing header files
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#Path of the file
path
data = pd.read_csv(path)
data.rename(columns={'Total':'Total_Medals'},inplace=True)
data.head(10)


#Code starts here



# --------------
#Code starts here
data['Better_Event'] =np.where(data['Total_Summer']>data['Total_Winter'],'Summer',(np.where(data['Total_Summer']<data['Total_Winter'],'Winter','Both')))
better_event = data['Better_Event'].value_counts().idxmax() 


# --------------
#Code starts here
top_countries = data[['Country_Name','Total_Summer', 'Total_Winter','Total_Medals']]
top_countries =top_countries[:-1]
def top_ten(variable1,variable2):
    country_list =list()
    country_list =variable1.nlargest(10,variable2)
    return country_list['Country_Name'].tolist()
top_10_summer = top_ten(top_countries,'Total_Summer')
top_10_winter = top_ten(top_countries,'Total_Winter')
top_10 = top_ten(top_countries,'Total_Medals')
common =list(set(top_10_summer) & set(top_10_winter) & set(top_10))


# --------------
#Code starts here
summer_df = data[data['Country_Name'].isin(top_10_summer)]
winter_df = data[data['Country_Name'].isin(top_10_winter)]
top_df = data[data['Country_Name'].isin(top_10)]
summer_df.plot.bar(y='Total_Summer')
plt.xlabel('Country')
plt.ylabel('Total_Summer')

winter_df.plot.bar(y='Total_Winter')
plt.xlabel('Country')

plt.ylabel('Total_Winter')

top_df.plot.bar(y='Total_Medals')
plt.xlabel('Country')
plt.ylabel('Total_Medals')



# --------------
#Code starts here
summer_df.set_index('Country_Name', inplace=True)
summer_df['Golden_Ratio'] =round(summer_df['Gold_Summer']/summer_df['Total_Summer'],2)
summer_max_ratio= summer_df['Golden_Ratio'].max()
summer_country_gold= summer_df['Golden_Ratio'].idxmax()

winter_df.set_index('Country_Name', inplace=True)
winter_df['Golden_Ratio'] =winter_df['Gold_Winter']/winter_df['Total_Winter']
winter_max_ratio= round(winter_df['Golden_Ratio'].max(),2)
winter_country_gold= winter_df['Golden_Ratio'].idxmax()

top_df.set_index('Country_Name', inplace=True)
top_df['Golden_Ratio'] =round(top_df['Gold_Total']/top_df['Total_Medals'],2)
top_max_ratio= top_df['Golden_Ratio'].max()
top_country_gold= top_df['Golden_Ratio'].idxmax()



# --------------
#Code starts here
data_1 =data[:-1]
data_1['Total_Points']=(data_1['Gold_Total']*3)+(data_1['Silver_Total'])*2+(data_1['Bronze_Total']*1)
most_points = data_1['Total_Points'].max()
best_country =data_1.loc[data_1['Total_Points'].idxmax(),'Country_Name']
best_country


# --------------
#Code starts here
data.head(2)
best =data[data['Country_Name']==best_country]
best =best[['Gold_Total','Silver_Total','Bronze_Total']].copy()
best.plot.bar()
plt.xlabel('United States')
plt.ylabel('Medals Tally')
plt.xticks(rotation=45)


