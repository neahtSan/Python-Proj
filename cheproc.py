import pandas as pd 
files = pd.read_csv("/Users/*/Downloads/che proc/import/Glycerol/Statistic_data_of_July_2021.csv")
total = sum(files['CIF (BAHT)(Jan - Jul 2021)'])
country_percent = (files['CIF (BAHT)(Jan - Jul 2021)'] / total) * 100
files['Country_Percent (%)'] = country_percent
#files.to_csv('Glycerol import data with percent calculated.csv',index=False)

files2 = pd.read_csv("/Users/*/Downloads/che proc/export/Glycerol/Statistic data of July 2021-2.csv")
total = sum(files2['FOB (BAHT)(Jan - Jul 2021)'])
country_percent = (files2['FOB (BAHT)(Jan - Jul 2021)'] / total) * 100
files2['Country_Percent (%)'] = country_percent
#files2.to_csv('Glycerol export data with percent calculated.csv',index=False)

files3 = pd.read_csv("/Users/*/Downloads/che proc/import/H2/Statistic data of July 2021.csv")
total = sum(files3['CIF (BAHT)(Jan - Jul 2021)'])
country_percent = (files3['CIF (BAHT)(Jan - Jul 2021)'] / total) * 100
files3['Country_Percent (%)'] = country_percent
#files3.to_csv('H2 import data with percent calculated.csv',index=False)

files4 = pd.read_csv("/Users/*/Downloads/che proc/export/H2/Statistic data of July 2021.csv")
total = sum(files4['FOB (BAHT)(Jan - Jul 2021)'])
country_percent = (files4['FOB (BAHT)(Jan - Jul 2021)'] / total) * 100
files4['Country_Percent (%)'] = country_percent
#files4.to_csv('H2 export data with percent calculated.csv',index=False)