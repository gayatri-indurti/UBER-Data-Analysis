#importing packages needed.
import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime
import time
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS
from PIL import Image
import folium
from google.colab import drive
drive.mount('/content/drive')
data= pd.read_csv('/content/drive/MyDrive/Uber data EDA/Uber data.csv')
data.head()
data.tail()
data.head(10)
data=data[:-1]
data

#Plot rectangular data as a color-encoded matrix.
sns.heatmap(data.isnull(),yticklabels=False,cmap='viridis')

data.isnull().sum()

data.loc[:,"Tip"]
data.loc[:,"Tip"].isnull()
data.loc[:,"Tip"].mean()
data.loc[:,"Tip"].median()
data.loc[:,"Tip"].mode()

14

data.isnull().sum()
data['Category'].mode()
data['Category'] = data['Category'].fillna(data['Category'].mode()[0])
data.isnull().sum()
data['Driver_Rating'].hist()
data['Driver_Rating'].mode()

data['Driver_Rating'] =
data['Driver_Rating'].fillna(data['Driver_Rating'].mode()[0])
data.isnull().sum()
data['Tip'].median()
data['Tip'] = data['Tip'].fillna(data['Tip'].median())
data.isnull().sum()
data=data.dropna()
data.isnull().sum()

#data cleaning
#purpose has 502 null values, replacing those null values with mode
purpose_mode = data.Purpose.mode()[0]
data.Purpose.fillna(purpose_mode, inplace = True)
data.Purpose.isnull().sum()
data=data.dropna()
sns.heatmap(data.isnull(),yticklabels=False,cmap="viridis")
data
#Univariate analysis(handling outliers)
#normalizing, removing outliers
data.Start_day.value_counts(normalize=True)
data.Start_day.value_counts(normalize=True).plot.barh()
#plt.xticks([])
plt.ylim(0,15)
plt.xlim(0,0.20)
plt.show()
#Univariate analysis(dealing with outliers)
data.Category.value_counts(normalize=True)
data.Category.value_counts(normalize=True).plot.pie()
plt.ylabel("")
plt.show()

15

#Univariate analysis(dealing with outliers)
data.Driver_Rating.value_counts(normalize=True)
data.Driver_Rating.value_counts(normalize=True).plot.pie()
#plt.ylabel("")
plt.show()
#analyzing whole data
data.describe()
#Bivariate analysis, 3 types, categorical-catergorical, numeric-numeric,
numeric-categorical
#Numeric-numeric, scatter plot,pair plot, correlation matrix
plt.scatter(data.KM,data.Purpose)
plt.show()
data.plot.scatter(x='Fare',y='Tip')
sns.pairplot(data = data, vars=['KM', 'Driver_Rating', 'Fare' ])
plt.yticks([])
plt.show()
data[['KM', 'Driver_Rating', 'Fare', 'Tip']].corr()
sns.heatmap(data[['KM', 'Driver_Rating', 'Fare', 'Tip']].corr(), annot=True, cmap =
'Purples')
plt.show()
data.groupby('Category')['KM'].median()
#sns.boxplot(data.Category, data.Driver_Rating)
#plt.ylim(0, 21)
sns.boxplot(data.Driver_Rating, data.Payment_Method)
plt.show()
data.info()
#plt.bar(Purpose, Category)
#plt.show
plt.bar(data.Category, data.Purpose ,color ='maroon')
#plt.xticks([])
plt.show
plt.bar(data.Pickup, data.Purpose ,color ='maroon')
plt.xticks([])
plt.show

16

#extract hour
plt.hist(data.Start_day)
#plt.xticks([])
plt.show
plt.bar(data.Start_day, data.Fare)
#data['Purpose'] = data['Purpose'].replace(np.nan)
#data[['Purpose', 'Category']] = data[['Purpose', 'Category']].fillna('none')
result = pd.pivot_table(data=data, index='Category',
columns='Purpose',values='Driver_Rating')
print(result)
#create heat map
sns.heatmap(result, annot=True, cmap = 'RdYlGn', center=0.117)
plt.show()
sns.violinplot(x="Driver_Rating", data=data)
sns.violinplot(x="Driver_Rating",y='KM', data=data)
plt.ylim(-30,50)
text = " ".join(Pickup for Pickup in data.Pickup)
wordcloud = WordCloud(collocations = False, background_color =
'black').generate(text)
# Display the generated Word Cloud
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.show()
text = " ".join(Destination for Destination in data.Destination)
wordcloud = WordCloud(collocations = False, background_color =
'black').generate(text)
# Display the generated Word Cloud
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.show()
text = " ".join(Purpose for Purpose in data.Purpose)
wordcloud = WordCloud(collocations = False, background_color =
'black').generate(text)
# Display the generated Word Cloud
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.show()
# Generate a word cloud image
stopwords = set(STOPWORDS)
mask = np.array(Image.open("/content/drive/MyDrive/Uber data
EDA/uber_icon.png"))

17

wordcloud = WordCloud(stopwords=stopwords,background_color='black',
max_words=1000,
mask=mask,contour_color='#023075',contour_width=3,colormap='rainbow').gene
rate(' '.join(data['Destination']))
# create image as cloud
plt.figure()
plt.imshow(wordcloud, interpolation="bilinear")
plt.axis("off")
# store to file
plt.savefig("uberdataicon.png", format="png")
plt.show()
data['SHour'].hist()
data['Status'].value_counts(ascending=True)
size=[597,55]
data.Status.value_counts(normalize=True)
data.Status.value_counts(normalize=True).plot.pie()
plt.pie(size, startangle=90, autopct='%1.1f%%')
#plt.ylabel("")
plt.show()
data['Payment_Method'].hist()
data['Pickup'].value_counts()[:7].index.tolist()
m = folium.Map(location=[35.791538,-78.781120], zoom_start=10, tiles="Stamen
Terrain")
tooltip1 = "Cary"
tooltip2 = "Morrisville"
tooltip3 = "Whitebridge"

folium.Marker([35.791538,-78.781120], popup="<b>Cary, NC</b>",
tooltip=tooltip1,).add_to(m)
folium.Marker([35.8235,-78.8256], popup="<b>Morrisville</b>",
tooltip=tooltip2).add_to(m)
folium.Marker([35.9813,-78.8311], popup="<b>Whitebridge</b>",
tooltip=tooltip3).add_to(m)
m
data['Duration'].min()
data['Duration'].max()
data['Fare'].min()

18

data['Fare'].max()
sns.relplot(x= 'Fare', y='Tip', hue='Category', data=data)
sns.distplot (data ['Fare'], bins=15)
sns.distplot (data ['KM'], bins=10)
sns.distplot (data['Driver_Rating'], bins=10)
data.to_csv("clean.csv")
stopwords = set(STOPWORDS)
mask = np.array(Image.open("/content/drive/MyDrive/Uber data
EDA/thanks3000.png"))
wordcloud = WordCloud(stopwords=stopwords,background_color='white',
max_words=1000,
mask=mask,contour_color='#023075',contour_width=3,colormap='rainbow').gene
rate(' '.join(data['End_day']))
# create image as cloud
plt.figure()
plt.imshow(wordcloud, interpolation="bilinear")
plt.axis("off")
# store to file
plt.savefig("Thankyou.png", format="png")
plt.show()
