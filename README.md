1. COVID-19-Database-Predictive-Modeling

2. Group Members: Cecilia McCormick and Varsha Subramanyam

3. This project aims to use a COVID-19 clinical trial dataset on hospital data from HealthData.gov made by the United States government in order to create a predictive model that uses number of COVID cases in different parts of a certain hospital (ie. in the ICU, Emergency room, etc) to predict the state (1 of the 50 United States) that the hospital is located in.

4. Imported Packages:

  numpy (1.23.5)
  pandas (pandas 1.5.2)
  matplotlib import pyplot (matplotlib 3.6.2)
  sklearn import tree (sklearn 1.2.0)
  sklearn.model_selection import train_test_split (sklearn 1.2.0)
  sklearn.model_selection import cross_val_score (sklearn 1.2.0)
  sklearn import svm (sklearn 1.2.0)
  sklearn.svm import SVR (sklearn 1.2.0)
  sklearn.ensemble import RandomForestClassifier (sklearn 1.2.0)
  sklearn.ensemble import BaggingClassifier (sklearn 1.2.0)
  sklearn.neighbors import KNeighborsClassifier (sklearn 1.2.0)
  sklearn.datasets import make_blobs (sklearn 1.2.0)
  
5. Detailed Description of Demo File:

  1. First begin by importing all necessary packages, including the Visualizer.py file that contains our custom class with all the data analysis functions.
  2. Then run the cell containg our 2 custom functions outside of the Hospital class which are tree_depth_finder and forest_depth_finder functions. These functions serve to help the user determine the optimal complexity of the model where the test score is the highest without overfitting the model. 
  3. The next part of the demo file serves to test these 2 functions on different data that is not the COVID hospital dataset. Here, we use the titanic.csv file as an example. 
  4. Run the cell that splits the titanic data into train and test datasets and use our custom tree_depth_finder function to plot the train and test scores at different depth values. Here is the plot:  
  ![PNG image](https://user-images.githubusercontent.com/114379054/206581131-5cbc7dd7-24b6-4594-8410-73631d5e2274.jpeg)
 
  From this plot, we can see that overfitting of the data tends to start around a depth value of 7. We can see from the plot that the most ideal depth value for this data seems to be around 5. This is where the test scores are the highest but the model is not overfitted yet (training score is not super high compared to test). 
  
  5. Next, run the cell that tests the titanic data train and test splits on our custom forest_depth_finder function. Here is the plot:
  ![IMG_2810](https://user-images.githubusercontent.com/114379054/206581585-5b630344-31b8-41f9-b207-96b9246a15bf.png)
  
  From this plot, we can see that overall the test scores remain relatively low despite changing the depth value. The training value seems to be relatively high no matter the depth value, which is a sign of overfitting.  This tells us that for this modeling problem, the DecisionTreeClassifier may be a better model than the RandomForest Classifier. 
  
  6. Next, we want to make an instance of our custom Hospital class from our imported COVID-19 hospital data. We can then test our length function by calling print(len(covid_data)). This tells us how many rows of data are in the COVID-19 hospital dataframe. 
  7. Next we can test our summary function by calling covid.data_summary. This function takes in a list of column names that the user wants summary statsitics on as well as a groupby variable by which the summary statsitic will be grouped. In this case, the groupby variable is "states" and the summary statistics will be on the total_staffed_pediatric_icu_beds_7_day_coverage. 
  
  The resulting table gives the user the summary statistics (count, mean, std, min, 25th Quartile, 50th Quartile, 75th Quartile, and max) grouped by state for the total_staffed_pediatric_icu_beds_7_day_coverage. 
  
  8. Next, we will visualize the data using our visualizer function in our Hospital class. This function takes the inputted listed of column names and gives 2 plots: one that plots the average given columns against collection date and one that plots the average given columns against states. 
  Here is the Graph:
  
![IMG_5960](https://user-images.githubusercontent.com/114379054/206628977-aefd12ca-af14-41b5-8d7f-394218ae8980.png)

From this graph, we can see the averages grouped by collection date and the averages grouped by state for total_staffed_pediatric_icu_beds_7_day_coverage and staffed_icu_pediatric_patients_confirmed_covid_7_day_coverage plotted against the collection date and state respectively. We chose to visualize the variables as a line graph against collection date since this is continuous and as a scatter plot against the states because these are discrete values. 


6. The scope of this data is the COVID-19 dataset that we acquired from the public databases on HealthData.gov made by the United States government. This data can be accessed at https://healthdata.gov/Hospital/COVID-19-Reported-Patient-Impact-and-Hospital- Capa/uqq2-txqb/data (https://healthdata.gov/Hospital/COVID-19-Reported-Patient-Impact-and-Hospital-Capa/uqq2-txqb/data). Obviously since we are training our model just on this singular dataset, there are limitations on what this model can be used for. There is information about more than 600,000 hospitals and the number of covid cases that they had during a particular week. But it is important to note that this may not be completely representative of all hospitals across the country, thus the model has its limitations on how accurate it will be in predicting the state the hospital is located in based on new data. 

7. References and Acknowledgements:
  
  Professor Harlin Lee's Lecture Slides 
  Scikitlearn packages for all classifiers 
  
8. Source of dataset: HealthData.gov

https://healthdata.gov/Hospital/COVID-19-Reported-Patient-Impact-and-Hospital- Capa/uqq2-txqb/data (https://healthdata.gov/Hospital/COVID-19-Reported-Patient-Impact-and-Hospital-Capa/uqq2-txqb/data)
