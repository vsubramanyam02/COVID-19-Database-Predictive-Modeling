import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
from mpl_toolkits import mplot3d


class Hospital(object): 
    '''
    A simple class for representing directed links between states.
    Constructs a dictionary of link for fast lookups from a list of input link
    tuples.
    '''
    def __init__(self, data):
        '''
        initialize with a dictionary representing links via data_to_dictionary()
        Args:
        data: list of tuples
        Returns: None 
        '''
        
        #initalize class variables
        self.data = data 
        
    def __len__(self):  
        ''' 
        returns the number of entries in the dataset 
        '''
        return len(self.data)
    
    def summary(self, column_names, groupby_variable):
        '''
        Create a summary of the hospital data with all description data to give the users
        a quick way to examine a large amount of data
        '''
        
        return self.data[column_names].groupby(groupby_variable).describe()
    
    def visualizer(self, column_names):
        '''
        Create a visualization of the hospital data to give the users
        a quick way to examine the relationship between 2 or 3 columns of data
        '''
        
        if len(column_names)==1:
            raise ValueError("You entered a list that only contains one component. Try again with a larger list!")
            
        for i in column_names:
            if type(i) not in [str]:
                 raise TypeError("You entered a list that has values that are not strings! Try again!") 
        
        fig, ax = plt.subplots(1, 2, figsize=(30,10))

        title="Visualize Graph for Selected Columns: "

        for i in range(len(column_names)):
    
            average=[]
            dates=[]
    
            for date, df_date in self.data.groupby("collection_week"):
        
                avg=df_date[column_names[i]].mean()
        
                average.append(avg)
                dates.append(date) 

        
            ax[0].plot(dates,average, label=column_names[i])
            ax[0].set_title("Collection Week:", fontsize = 20) 
            ax[0].set_xlabel("collection week", fontsize=15) 
            ax[0].set_ylabel("COVID cases", fontsize=15)
            ax[0].legend()
            
            
        for i in range(len(column_names)):
    
            average=[]
            states=[]
    
            for state, df_state in self.data.groupby("state"):
        
                avg=df_state[column_names[i]].mean()
        
                average.append(avg)
                states.append(state) 

        
            ax[1].scatter(states,average, s=50, label=column_names[i])
            ax[1].set_title("State:", fontsize = 20) 
            ax[1].set_xlabel("state", fontsize=15) 
            ax[1].set_ylabel("COVID cases", fontsize=15)
            ax[1].legend()
        
           
        fig.suptitle(title, size=25)   
        plt.show()
        
        