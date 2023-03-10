# -*- coding: utf-8 -*-
"""Phase2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1R0IkNcSDXGoc-pIX1nhcwMUrtdkL8ogI
"""

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import GridSearchCV
from sklearn.feature_selection import SelectFromModel
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
from sklearn.metrics import roc_curve, auc

import pandas as pd
pd.options.mode.chained_assignment = None
pd.options.display.max_columns = 999
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.preprocessing import StandardScaler, MinMaxScaler
from sklearn.model_selection import train_test_split

from imblearn.over_sampling import SMOTE
from collections import Counter

accidents = pd.read_csv('/kaggle/input/us-accidents/US_Accidents_Dec21_updated.csv')

accidents.info()

"""# Data Cleaning/Processing
**1. Handling missing values**

Here, we will remove any incorrect or missing values from the dataset. Action on Side column:
"""

#Take care of incorrect and missing values

accidents = accidents.drop(accidents[accidents.Side == 'N'].index)
accidents["Side"].value_counts()

"""Here we observed that there is one row without side value as R/L therefore we can drop it.

Also dropped ID and Description column as they are not providing information on the accident which can be feeded into the models in the future.
"""

accidents.drop(['ID', 'Description'], axis=1, inplace=True)
pd.set_option('display.max_columns', 500)
accidents.sample(3)

"""**2. Handling data with a high cardinality**


"""

print(accidents.Weather_Condition.unique())

"""Data can be combined or binned. By assembling them into coherent sets, the goal is to lower the number of unique values. As long as the groupings do not significantly affect model performance and business stakeholder explainability, this approach is excellent."""

accidents.loc[accidents["Weather_Condition"].str.contains("N/A Precipitation", na=False), "Weather_Condition"] = np.nan
accidents.loc[accidents["Weather_Condition"].str.contains("Snow|Sleet|Wintry", na=False), "Weather_Condition"] = "Snow"
accidents.loc[accidents["Weather_Condition"].str.contains("Smoke|Volcanic Ash", na=False), "Weather_Condition"] = "Smoke"
accidents.loc[accidents["Weather_Condition"].str.contains("Cloud|Overcast", na=False), "Weather_Condition"] = "Cloudy"
accidents.loc[accidents["Weather_Condition"].str.contains("Sand|Dust", na=False), "Weather_Condition"] = "Sand"
accidents.loc[accidents["Weather_Condition"].str.contains("Wind|Squalls", na=False), "Weather_Condition"] = "Windy"
accidents.loc[accidents["Weather_Condition"].str.contains("Mist|Haze|Fog", na=False), "Weather_Condition"] = "Fog"
accidents.loc[accidents["Weather_Condition"].str.contains("Thunder|T-Storm", na=False), "Weather_Condition"] = "Thunderstorm"
accidents.loc[accidents["Weather_Condition"].str.contains("Rain|Drizzle|Shower", na=False), "Weather_Condition"] = "Rain"
accidents.loc[accidents["Weather_Condition"].str.contains("Hail|Pellets", na=False), "Weather_Condition"] = "Hail"
accidents.loc[accidents["Weather_Condition"].str.contains("Fair", na=False), "Weather_Condition"] = "Clear"

print('Unique values:',accidents["Weather_Condition"].unique())

"""**3. One-hot Encoding** 

We converted bool values to 0s and 1s as will be easier to feed the models we make in phase2.
"""

#One-hot Encoding 

accidents = accidents.replace([True, False], [1,0])
accidents.info()

"""**4. Remove Duplicate Data**

We did not have any duplicates but this was fail safe cleaning as Duplicate data sets have the potential to contaminate the training data with the test data, or the other way around. This can make the model bias towards one feature.
"""

Duplicate_Data = accidents[accidents.duplicated()]
print("Duplicate Rows :{}".format(Duplicate_Data))
accidents.drop_duplicates(inplace=True)

"""**5. NA value handling (Imputation by mean value)**

Since filling them with zero doesn't make much sense, we populated the following columns with their average value.
"""

accidents['Wind_Speed(mph)']=accidents['Wind_Speed(mph)'].fillna(accidents['Wind_Speed(mph)'].mean())
accidents['Humidity(%)']=accidents['Humidity(%)'].fillna(accidents['Humidity(%)'].mean())
accidents['Temperature(F)']=accidents['Temperature(F)'].fillna(accidents['Temperature(F)'].mean())
accidents['Pressure(in)']=accidents['Pressure(in)'].fillna(accidents['Pressure(in)'].mean())
# accidents.dropna(inplace=True)

"""**6. NA value handling (Imputation by median value)**

When the data is skewed, it is wise to think about replacing the missing values with the median value. Keep in mind that only numerical data can be used to impute missing data using the median value. Because it lessens the impact of outliers, using the median to impute is more reliable.
"""

#NA value handling (Imputation by median value)

accidents['Visibility(mi)']=accidents['Visibility(mi)'].fillna(accidents['Visibility(mi)'].median())
accidents['Wind_Chill(F)']=accidents['Wind_Chill(F)'].fillna(accidents['Wind_Chill(F)'].median())
accidents['Precipitation(in)']=accidents['Precipitation(in)'].fillna(accidents['Precipitation(in)'].median())
# accidents.dropna(inplace=True)

"""**7. Impute empty value with most occurring value (or mode)**

The mode value, or most frequent value, of the full feature column is substituted for the missing values in mode imputation, a further approach. It is wise to think about utilizing mode values to replace missing values when the data is skewed. You might think about substituting values for data points like the city field with mode. It should be noted that both numerical and categorical data can be used to impute missing data using mode values.
"""

#Impute empty value with most occurring value (or mode)

accidents['City'] = accidents.groupby('State')['City'].transform(lambda data: data.fillna(data.value_counts().index[0]))

"""**8. Scaling of feature**

We will scale and normalize the characteristics in this part. We normalized the values of the continuous features to enhance the performance of our models.
"""

#Scaling of feature

ss = MinMaxScaler()
attributes = ['Wind_Speed(mph)','Pressure(in)','Humidity(%)','Distance(mi)','Visibility(mi)','Temperature(F)']
accidents[attributes] = ss.fit_transform(accidents[attributes])
accidents.sample(3)

"""**9. Adding of feature**

We made the decision to divide the Start Time feature (so that we can feed it to the model later) into the following components: year, month, day, weekday, hour, and minute.
"""

accidents['M'] = pd.to_datetime(accidents.Start_Time).dt.strftime('%m')
accidents['Y'] =  pd.to_datetime(accidents.Start_Time).dt.strftime('%Y')
accidents['D'] = pd.to_datetime(accidents.Start_Time).dt.strftime('%w')
accidents['H'] = pd.to_datetime(accidents.Start_Time).dt.strftime("%H")
accidents.sample(2)

"""**10. Examine feature variance**

This part will examine each feature's variance in order to eliminate features with very low variances because they cannot aid in instance discrimination.
"""

pd.set_option('display.max_columns', None)
accidents.describe()
accidents.round(2)

#filling all the null values in the below attributes 
features_to_fill = ["Temperature(F)", "Humidity(%)", "Pressure(in)", "Visibility(mi)", "Wind_Speed(mph)", "Precipitation(in)"]
accidents[features_to_fill] = accidents[features_to_fill].fillna(accidents[features_to_fill].mean())

# accidents.dropna(inplace=True)


accidents.isna().sum()

#Plot for bool feature attributes
fig = plt.figure(figsize=(11,11)) 
fig_dims = (3, 2)


plt.subplot2grid(fig_dims, (0, 0))
accidents['Amenity'].value_counts().plot(kind='bar', 
                                     title='Amenity')
plt.subplot2grid(fig_dims, (0, 1))
accidents['Bump'].value_counts().plot(kind='bar', 
                                     title='Bump')
plt.subplot2grid(fig_dims, (1, 0))
accidents['Crossing'].value_counts().plot(kind='bar', 
                                     title='Crossing')
plt.subplot2grid(fig_dims, (1, 1))
accidents['Junction'].value_counts().plot(kind='bar', 
                                     title='Junction')
plt.subplot2grid(fig_dims, (2, 0))
accidents['Sunrise_Sunset'].value_counts().plot(kind='bar', 
                                     title='Sunrise_Sunset')
plt.subplot2grid(fig_dims, (2, 1))
accidents['Traffic_Signal'].value_counts().plot(kind='bar', 
                                     title='Traffic_Signal')

#plot for bool feature attributes
fig = plt.figure(figsize=(11,11)) 
fig_dims = (3, 2)


plt.subplot2grid(fig_dims, (0, 0))
accidents['Give_Way'].value_counts().plot(kind='bar', 
                                     title='Give_Way')
plt.subplot2grid(fig_dims, (0, 1))
accidents['No_Exit'].value_counts().plot(kind='bar', 
                                     title='No_Exit')
plt.subplot2grid(fig_dims, (1, 0))
accidents['Railway'].value_counts().plot(kind='bar', 
                                     title='Railway')
plt.subplot2grid(fig_dims, (1, 1))
accidents['Roundabout'].value_counts().plot(kind='bar', 
                                     title='Roundabout')
plt.subplot2grid(fig_dims, (2, 0))
accidents['Station'].value_counts().plot(kind='bar', 
                                     title='Station')
plt.subplot2grid(fig_dims, (2, 1))
accidents['Stop'].value_counts().plot(kind='bar', 
                                     title='Stop')

accidents["Bump"].value_counts()

#voilin plot to study the distribution of the data
import seaborn as sns 


plt.figure(figsize=(12,8))
sns.violinplot(x='Severity', y='Wind_Chill(F)', data=accidents)
plt.xlabel('Severity', fontsize=12)
plt.ylabel('Wind_Chill(F)', fontsize=12)
plt.show()

#box plot for mean and quartile distribution
plt.figure(figsize=(12,8))
sns.boxplot(x="Severity", y="Wind_Chill(F)", data=accidents)
plt.ylabel('Wind_Chill(F)', fontsize=12)
plt.xlabel('Severity', fontsize=12)
plt.xticks(rotation='vertical')
plt.show()

#Plot for Weather condition
fig, ax=plt.subplots(figsize=(20,10))
accidents['Weather_Condition'].value_counts().sort_values(ascending=False).head(5).plot.bar(width=0.8,edgecolor='red',align='center',linewidth=2)
plt.xlabel('Weather_Condition',fontsize=18)
plt.ylabel('Number of Accidents',fontsize=18)
ax.tick_params(labelsize=20)
plt.title('Weather Condition for accidents - Top 5',fontsize=20)
plt.grid()
plt.ioff()

accidents["Weather_Condition"].value_counts()

#bar plot for state wise number of accidents
plt.figure(figsize=(12,8))
accidents.State.value_counts().sort_values(ascending=False).head(18).plot.bar(width=0.3,edgecolor='k',align='center',linewidth=2)
plt.xlabel('State_name',fontsize=18)
plt.ylabel('Number of Accidents',fontsize=18)
ax.tick_params(labelsize=20)
plt.title('State wise accidents',fontsize=20)
plt.grid()
plt.ioff()

#bar plot for timezone vs number of accidents
plt.figure(figsize=(12,8))
accidents.Timezone.value_counts().sort_values(ascending=False).head(18).plot.bar(width=0.3,edgecolor='k',align='center',linewidth=2)
plt.xlabel('Time Zone',fontsize=18)
plt.ylabel('Number of Accidents',fontsize=18)
ax.tick_params(labelsize=30)
plt.title('Accident cases for different timezones in US (2016-2020)',fontsize=20)
plt.grid()
plt.ioff()

#hour wise plot wrt accidents
plt.figure(figsize=(12,8))
accidents.H.value_counts().sort_values(ascending=True).head(24).reset_index().plot.bar(width=0.3,edgecolor='k',align='center',linewidth=2)
plt.xlabel('Hour',fontsize=18)
plt.ylabel('Number of Accidents',fontsize=18)
ax.tick_params(labelsize=30)
plt.title('Accident cases for different Hours',fontsize=20)
plt.grid()
plt.ioff()

#Correlation matrix

import matplotlib.pyplot as plt

corr = accidents.corr()
corr.style.background_gradient(cmap='YlOrRd')

sns.heatmap(accidents[['Severity','Start_Lat','Start_Lng','Temperature(F)', 'Humidity(%)', 'Pressure(in)', 'Visibility(mi)','Precipitation(in)','Weather_Condition']].corr())

day = pd.DataFrame(accidents.D.value_counts()).reset_index().rename(columns={'index':'Day', 'Start_Time':'Cases'})

day

#Week wise vs number of accidents
plt.figure(figsize=(9,4))
plt.title('\n Accident cases for different days of a week\n', size=20, color='grey')
plt.xlabel('\n Day \n', fontsize=15, color='grey')
plt.ylabel('\nAccident Cases\n', fontsize=15, color='grey')
plt.xticks(fontsize=13)
plt.yticks(fontsize=12)
a = sns.barplot(x=day.Day,y=day.D,palette="muted")
plt.show()

#wind direction vs accidents
fig = plt.figure(figsize = (12, 10))
sns.countplot(y='Wind_Direction', data=accidents, order=accidents['Wind_Direction'].value_counts()[:15].index).set_title("Top 15 Wind_Direction", fontsize = 18)
plt.show()

#Sunset Sunrise Day vs Night

plt.figure(figsize=(10,8))
accidents.Sunrise_Sunset.value_counts().sort_values(ascending=False).head(5).plot.bar(width=0.3,edgecolor='k',align='center',linewidth=2)
plt.xlabel('Sunrise_Sunset',fontsize=18)
plt.ylabel('Number of Accidents',fontsize=18)
ax.tick_params(labelsize=30)
plt.title('Accident cases for Sunrise_Sunset (2016-2020)',fontsize=20)
plt.grid()
plt.ioff()

#hour wise plot wrt accidents
plt.figure(figsize=(12,8))
accidents.M.value_counts().sort_values(ascending=True).head(24).reset_index().plot.bar(width=0.3,edgecolor='k',align='center',linewidth=2)
plt.xlabel('Month',fontsize=18)
plt.ylabel('Number of Accidents',fontsize=18)
ax.tick_params(labelsize=30)
plt.title('Accident cases Month Wise',fontsize=20)
plt.grid()
plt.ioff()

accidents['Start_Time'] = pd.to_datetime(accidents['Start_Time'], errors='coerce')
accidents['End_Time'] = pd.to_datetime(accidents['End_Time'], errors='coerce')

# Extract year, month, day, hour and weekday
accidents['Year']=accidents['Start_Time'].dt.year
accidents['Month']=accidents['Start_Time'].dt.strftime('%b')
accidents['Day']=accidents['Start_Time'].dt.day
accidents['Hour']=accidents['Start_Time'].dt.hour
accidents['Weekday']=accidents['Start_Time'].dt.strftime('%a')

# Extract the amount of time in the unit of minutes for each accident, round to the nearest integer
td='Time_Duration(min)'
accidents[td]=round((accidents['End_Time']-accidents['Start_Time'])/np.timedelta64(1,'m'))
accidents.info()
accidents.shape

print(accidents['Year'].unique())

year_df = pd.DataFrame(accidents.Start_Time.dt.year.value_counts()).reset_index().rename(columns={'index':'Year', 'Start_Time':'Cases'}).sort_values(by='Cases', ascending=True)

accidents[td][accidents[td]<=0]

# Drop the rows with td<0

neg_outliers=accidents[td]<=0

# Set outliers to NAN
accidents[neg_outliers] = np.nan

# Drop rows with negative td
accidents.dropna(subset=[td],axis=0,inplace=True)
accidents.info()


accidents[td][accidents[td]<=0]


n=3

median = accidents[td].median()
std = accidents[td].std()
outliers = (accidents[td] - median).abs() > std*n

# Set outliers to NAN
accidents[outliers] = np.nan

# Fill NAN with median
accidents[td].fillna(median, inplace=True)
accidents.info()

print('Max time to clear an accident: {} minutes or {} hours or {} days; Min to clear an accident td: {} minutes.'.format(accidents[td].max(),round(accidents[td].max()/60), round(accidents[td].max()/60/24), accidents[td].min()))

# selected features from above performed EDA

feature_lst= ['Severity','Traffic_Signal', 'Hour', 'Crossing', 'Temperature(F)', 'Wind_Chill(F)', 'Wind_Speed(mph)', 'Junction', 'Humidity(%)','Pressure(in)', 'Visibility(mi)', 'Weekday','Year', 'Time_Duration(min)']

df_sel=accidents[feature_lst].copy()
df_sel.info()

df_sel.dropna(subset=df_sel.columns[df_sel.isnull().mean()!=0], how='any', axis=0, inplace=True)
df_sel.shape

df_sel['Year'].unique()

df2 = df_sel.dropna()

df_sel.isnull().mean()

Years_list = [2016., 2017., 2021., 2020., 2019., 2018.]

df_y1=df2[df2['Year']==2020.0]
df_y1.drop('Year',axis=1, inplace=True)
df_y1.info()

df2.isnull().mean()

# Generate dummies for categorical data
df_state_dummy = pd.get_dummies(df_y1,drop_first=True)

df_state_dummy.info()

df_state_dummy.shape

# df=df_state_dummy


# Set the target for the prediction
target='Severity'



# Create arrays for the features and the response variable

# set X and y
y = df_state_dummy[target]
X = df_state_dummy.drop(target, axis=1)

# Split the data set into training and testing data sets
# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=21, stratify=y)
sm = SMOTE(random_state=42)
X_res, y_res = sm.fit_resample(X, y)

scaler = StandardScaler()
X_res = scaler.fit_transform(X_res)

X_train, X_test, y_train, y_test = train_test_split(X_res, y_res, test_size=0.2, random_state=42)

y_res.shape
X_train.shape

def run_lr_training(X,y):
  X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=21, stratify=y)
  lr = LogisticRegression(random_state=0, max_iter= 10000)
  lr.fit(X_train,y_train)
  y_pred=lr.predict(X_test)

  # Get the accuracy score
  acc=accuracy_score(y_test, y_pred)

  # Append to the accuracy list
  accuracy_lst.append(acc)
  with open('lr_model.pkl','wb') as f:
    pickle.dump(lr,f)

  print("[Logistic regression algorithm] accuracy_score: {:.3f}.".format(acc))
  return acc, y_pred, y_test

#training without upsampling

acc, y_pred, y_test = run_lr_training(X,y)

confusion_matrix = metrics.confusion_matrix(y_test, y_pred)

cm_display = metrics.ConfusionMatrixDisplay(confusion_matrix = confusion_matrix, display_labels = [1,2,3,4])

cm_display.plot()
plt.show()

# training on the upsampled data sample

acc, y_pred, y_test = run_training(X_res, y_res)

confusion_matrix = metrics.confusion_matrix(y_test, y_pred)

cm_display = metrics.ConfusionMatrixDisplay(confusion_matrix = confusion_matrix, display_labels = [1,2,3,4])

cm_display.plot()
plt.show()

#KNN training

def knn_training(X,y):
  X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=21, stratify=y)

  knn = KNeighborsClassifier(n_neighbors=6)

  # Fit the classifier to the data
  knn.fit(X_train,y_train)

  # Predict the labels for the training data X
  y_pred = knn.predict(X_test)

  # Get the accuracy score
  acc=accuracy_score(y_test, y_pred)

  # Append to the accuracy list
  accuracy_lst.append(acc)
  

  print('[K-Nearest Neighbors (KNN)] knn.score: {:.3f}.'.format(knn.score(X_test, y_test)))
  print('[K-Nearest Neighbors (KNN)] accuracy_score: {:.3f}.'.format(acc))
  return acc, y_pred, y_test

#training on upsampled data sample year 2020

acc, y_pred, y_test = knn_training(X_res,y_res)

confusion_matrix = metrics.confusion_matrix(y_test, y_pred)

cm_display = metrics.ConfusionMatrixDisplay(confusion_matrix = confusion_matrix, display_labels = [1,2,3,4])

cm_display.plot()
plt.show()

# Decision tree algorithm
from sklearn.tree import DecisionTreeClassifier
# Instantiate dt_entropy, set 'entropy' as the information criterion
dt_entropy = DecisionTreeClassifier(max_depth=8, criterion='entropy', random_state=1)

print(X_train.shape)

# Fit dt_entropy to the training set
dt_entropy.fit(X_train, y_train)

# Use dt_entropy to predict test set labels
y_pred= dt_entropy.predict(X_test)



# Evaluate accuracy_entropy
accuracy_entropy = accuracy_score(y_test, y_pred)

confusion_matrix = metrics.confusion_matrix(y_test, y_pred)

cm_display = metrics.ConfusionMatrixDisplay(confusion_matrix = confusion_matrix, display_labels = [1,2,3,4])

cm_display.plot()
plt.show()

# Print accuracy_entropy
print('[Decision Tree -- entropy] accuracy_score: {:.3f}.'.format(accuracy_entropy))



# Instantiate dt_gini, set 'gini' as the information criterion
dt_gini = DecisionTreeClassifier(max_depth=8, criterion='gini', random_state=1)


# Fit dt_entropy to the training set
dt_gini.fit(X_train, y_train)

# Use dt_entropy to predict test set labels
y_pred= dt_gini.predict(X_test)

# Evaluate accuracy_entropy
accuracy_gini = accuracy_score(y_test, y_pred)

confusion_matrix = metrics.confusion_matrix(y_test, y_pred)

cm_display = metrics.ConfusionMatrixDisplay(confusion_matrix = confusion_matrix, display_labels = [1,2,3,4])

cm_display.plot()
plt.show()

# Print accuracy_gini
print('[Decision Tree -- gini] accuracy_score: {:.3f}.'.format(accuracy_gini))

#tree visualisation 

from sklearn import tree

tree.plot_tree(dt_gini, max_depth = 5)

# Random Forest algorithm
from sklearn.ensemble import RandomForestClassifier
#Create a Gaussian Classifier
clf=RandomForestClassifier(n_estimators=100)

#Train the model using the training sets y_pred=clf.predict(X_test)
clf.fit(X_train,y_train)

y_pred=clf.predict(X_test)


# Get the accuracy score
acc=accuracy_score(y_test, y_pred)

# Append to the accuracy list
# accuracy_lst.append(acc)


# Model Accuracy, how often is the classifier correct?
print("[Randon forest algorithm] accuracy_score: {:.3f}.".format(acc))

confusion_matrix = metrics.confusion_matrix(y_test, y_pred)

cm_display = metrics.ConfusionMatrixDisplay(confusion_matrix = confusion_matrix, display_labels = [1,2,3,4])

cm_display.plot()
plt.show()

feature_imp = pd.Series(clf.feature_importances_,index=X.columns).sort_values(ascending=False)

# Creating a bar plot, displaying only the top k features
k=10
sns.barplot(x=feature_imp[:10], y=feature_imp.index[:k])
# Add labels to your graph
plt.xlabel('Feature Importance Score')
plt.ylabel('Features')
plt.title("Visualizing Important Features")
plt.legend()
plt.show()

import tensorflow as tf
import keras
from keras.models import Sequential
from keras.layers import Dense, Dropout

y_test = y_test-1
y_train =  y_train-1



inputs = tf.keras.Input(shape=(X.shape[1],))
x = tf.keras.layers.Dense(256, activation='relu')(inputs)
x = tf.keras.layers.Dense(128, activation='relu')(x)
x = tf.keras.layers.Dense(64, activation='relu')(x)
x = tf.keras.layers.Dense(32, activation='relu')(x)
x = tf.keras.layers.Dense(32, activation='relu')(x)
outputs = tf.keras.layers.Dense(4, activation='softmax')(x)

model = tf.keras.Model(inputs, outputs)

model.compile(
    optimizer='adam',
    loss='sparse_categorical_crossentropy',
    metrics=['accuracy']
)

batch_size = 20
epochs = 100

history = model.fit(
    X_train,
    y_train,
    validation_split=0.2,
    batch_size=batch_size,
    epochs=epochs,
    callbacks=[
        tf.keras.callbacks.ReduceLROnPlateau(),
        tf.keras.callbacks.EarlyStopping(
            monitor='val_loss',
            patience=3,
            restore_best_weights=True
        )
    ]
)

y_test = y_test-1

print("Test Accuracy:", model.evaluate(X_test, y_test, verbose=0)[1])

losses=pd.DataFrame(history.history)
l = pd.DataFrame({'loss':losses['loss'], 'validation_loss':losses['val_loss']})
l.plot()

losses=pd.DataFrame(history.history)
l = pd.DataFrame({'accuracy':losses['accuracy'], 'val_accuracy':losses['val_accuracy']})
l.plot()

