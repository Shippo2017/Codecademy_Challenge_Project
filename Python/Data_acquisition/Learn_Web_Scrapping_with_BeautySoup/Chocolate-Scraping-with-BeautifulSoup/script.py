import codecademylib3_seaborn
from bs4 import BeautifulSoup
import requests
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

webpage = requests.get('https://content.codecademy.com/courses/beautifulsoup/cacao/index.html')
soup = BeautifulSoup(webpage.content, 'html.parser')
print(soup)

# Rating Distribution
ratings = []
rating_list = soup.find_all(attrs={'class': 'Rating'})
for td in rating_list[1:]:
  ratings.append(float(td.get_text()))
print(ratings)

plt.hist(ratings)
plt.title("Chocolate")
plt.show()
plt.clf()

# The Best Chocolate

# Company
company = []
company_names = soup.select('.Company')
for td in company_names[1:]:
  company.append(td.get_text())
print(company)

# Dataframe Company & Ratings
df = pd.DataFrame.from_dict({
  'Company': company,
  'Rating': ratings
})
print(df)

# Average
df_mean = df.groupby('Company').Rating.mean()
ten_best = df_mean.nlargest(10)
print(ten_best)


# Better Cacao
cocoa_percents = []
cocoa_percent_tags = soup.select('.CocoaPercent')
for td in cocoa_percent_tags[1:]:
  percent = int(float(td.get_text().strip('%')))
  cocoa_percents.append(percent)
print(cocoa_percents)

# add column in pandas
df['CocoaPercentage'] = cocoa_percents
print(df)

# Scatterplot
plt.scatter(df.CocoaPercentage, df.Rating)
z = np.polyfit(df.CocoaPercentage, df.Rating, 1)
line_function = np.poly1d(z)
plt.plot(df.CocoaPercentage, line_function(df.CocoaPercentage), "r--")
plt.xlabel('Percentage')
plt.ylabel('Rating')
plt.title('Percentage Vs Rating')
plt.show()


# Where are the best cocoa beans grown?
cocoa_origin = []
cocoa_origin_tags = soup.select('.Origin')
for td in cocoa_origin_tags[1:]:
  cocoa_origin.append(td.get_text())

df['CocoaOrigin'] = cocoa_origin

cocoa_origin_broad = []
cocoa_origin_broad_tags = soup.select('.BroadBeanOrigin')
for td in cocoa_origin_broad_tags[1:]:
  cocoa_origin_broad.append(td.get_text())

df['CocoaBoardOrigin'] = cocoa_origin_broad
print(df)

best_cocoa_origin = df[df.Rating >= df.Rating.max()]
print(f"The best cocoa beans grown in {best_cocoa_origin.CocoaOrigin.iloc[0]}, {best_cocoa_origin.CocoaBoardOrigin.iloc[0]}")


# Which countries produce the highest-rated bars?
company_location = []
company_location_tags = soup.select('.CompanyLocation')
for td in company_location_tags[1:]:
  company_location.append(td.get_text())

df['Company_location'] = company_location
print(df)

best_cocoa_origin = df[df.Rating >= df.Rating.max()]
best_bar_rated = best_cocoa_origin.Company_location
print(f"The highest rated bars produced in {next(iter(set(best_bar_rated)))}")
