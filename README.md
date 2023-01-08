# Fall 2022
<p align="center">
<img src="images/ub.png" alt="ub_logo.jpg" width="100" height="100"> <br>
  <b> CSE-587: Data Intensive Computing</b>
</p>

Link to dataset: https://www.kaggle.com/datasets/sobhanmoosavi/us-accidents

Link to Visualisations: https://app.powerbi.com/view?r=eyJrIjoiZGVmMzEzOTYtNjJlZS00ZGQxLWEyYWQtYjdlZjY1NzY1M2M1IiwidCI6Ijk2NDY0YThhLWY4ZWQtNDBiMS05OWUyLTVmNmI1MGEyMDI1MCIsImMiOjN9 https://app.powerbi.com/view?r=eyJrIjoiZmJhNDg5YTUtNTFhNC00NjJiLWFjMjYtODlmZmRmOTM3YjY3IiwidCI6Ijk2NDY0YThhLWY4ZWQtNDBiMS05OWUyLTVmNmI1MGEyMDI1MCIsImMiOjN9&pageName=ReportSection


### [Phase_01](Phase_01) :
<img src="images/bar.jpeg" alt="bar.jpeg" width="1100" height="3"> <br>

**Tasks:** 
1. Identify problems prevalent in public application domains. 
2. Research and identify data sets (preferably structured data) to address the problems and
collect the relevant data sets.
3. Clean and provision the data for downstream explorations and analytics. 
4. Understand the basic characteristics of the data by performing John Tukey’s exploratory
data analysis (EDA).
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; [Code](phase1/DIC2022_Phase1.ipynb)  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; [Report](phase1/DIC_Phase_1.pdf)



### [Phase_02](Phase_02) :
<img src="images/bar.jpeg" alt="bar.jpeg" width="1100" height="3"> <br>

**Tasks:** 
1. Identify suitable ML, MR, and/or statistical modeling algorithms. Model and apply
algorithms to get insights into the behavior of the data. It could be classification,
regression, clustering, etc.
2. Understand and explain the differences in each of the algorithms used.
3. Visualize the analytics using appropriate charts and graphs. You can use Seaborn or any
other plotting tool.
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; [Code](phase2/phase2.py)  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; [Report](phase2/DIC_Phase_2.pdf)




### [Phase_03](Phase_03) :
<img src="images/bar.jpeg" alt="bar.jpeg" width="1100" height="3"> <br>

**Tasks:** 
1. Build a data product around the exploration. Could be as simple as a web tool to input
different data sets to the model built and explore the outcomes with different parameters
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; <br><p align="center">[Code](phase3/script.py)  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; [Report](phase3/DIC_PHASE_3.pdf)</p>





### Model Selection Criteria:
<img src="images/bar.jpeg" alt="bar.jpeg" width="1100" height="3"> <br>

In phase 2 we have trained our processed data on 5 models

Model Accuracy Logistic Regression 0.569 K Nearest neighbors 0.71 Decision Tree 0.79 Random Forest Classifier 0.825 Artificial Neural Network 0.86

During phase 2 we have trained the models on a sample of dataset due to limited availability of computational resources, now we have divided the dataset into 5 sample, and performed training neural network on 5 samples, where we have downscaled the number of features by knowing the feature importance from random forest classifier and we have decided using 11 feature and chose the best model based on the accuracy metric, here we chose Neural network among the 5 models that we trained in phase 2 as this was rightly fitting the data, we were able to achieve an accuracy of 0.92 on the test dataset.

In this phase, in our react app, we have used Microsoft Power BI for visualization and to display the analysis on the dataset.





### Problem Statement Analysis:
<img src="images/bar.jpeg" alt="bar.jpeg" width="1100" height="3"> <br>

We got the US Accidents data from Kaggle researched the major causes of accidents and attempted to deduce the severity of each one. Living in a nation where everything is on wheels involves some amount of driving. If you had just put on your suit and were going to your first interview, what would you least want to happen? If your family has just started a road trip to a national park you've always wanted to see, what is the one thing you absolutely must avoid doing? The response is Car Accidents/Crashes. We learned more about the causes of incidents on the road and how they have changed over time. Where do accidents happen and what are the main causes of car crashes? Whether it is possible to predict how terrible an accident will be and prevent it before it occurs.

There are patterns in the hours, places, and weather when the majority of occurrences occurred. The seriousness of each accident may be reasonably predicted with the use of numerous classification machine learning methods.

The following are the questions that will be addressed and which will add to our issue: When do accidents most frequently happen? Daylight against nighttime, Monday through Friday versus weekends, and Peak time Where are accidents most likely to happen? Location, County, City, Zip Code, and Street Side What kind of weather has the highest accident rate? The most dangerous weather for accidents, the three weather conditions that cause accidents the most, and the weather's severity in each accident.



### Recommendations:
<img src="images/bar.jpeg" alt="bar.jpeg" width="1100" height="3"> <br>

The US government should limit the number of vehicles on the road. This can be accomplished by enhancing public transit by putting new modes of transportation, such as bullet trains, the hyperloop, and high-speed trains between key cities in California and Texas, into operation. These states have a higher accident rate due to the greater number of automobiles on the roads. The government should also consider the weather conditions while road construction and public transport availability. As places with more rain like Florida has the maximum number of accidents, therefore, the roads should be well constructed and proper placements of traffic controls should be there. The government should take new automobiles that can withstand high speed entering the market into account when building roadways. According to US Accident insights, Weekends had the maximum number of accidents and a major factor for this can be drunk driving. The legal system needs to update and strengthen state-by-state drunk driving sanctions. Additionally, in order to inculcate discipline among the populace, the government should see to it that those found breaking traffic laws face harsh legal penalties.



### Future Work:
<img src="images/bar.jpeg" alt="bar.jpeg" width="1100" height="3"> <br>

A significant portion of research has been devoted to the analysis and forecasting of traffic accidents, a major public safety concern. We were able to determine accident-causing factors. Numerous insights into the place, time, weather, and nearby areas of interest of an accident are discovered from this dataset. We were able to determine the most advantageous month, day, and hour for travel. Additionally, it enables us to foresee where accidents are most likely to occur in each state. In terms of our future work, We can make this platform accessible to the public and state governments so that it is readily available. This platform can be modified to meet certain issues facing the state's people and administration. To achieve a more current analysis, live data must be loaded into this application and launched on a website. The public can anticipate an accident location by using our machine-learning model using the source and destination locations, as well as the date and time of transit. The number of accidents that occur in the US may be decreased with the aid of this kind of prediction model. The prediction model may include a number of neural network-based elements that make use of a range of data properties, including traffic-related events, meteorological data, sites of interest, and time information.

---
## License

[![License](http://img.shields.io/:license-mit-blue.svg?style=flat-square)](http://badges.mit-license.org)

- **[MIT license](http://opensource.org/licenses/mit-license.php)**


&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Back To The Top](#spring-2019)
