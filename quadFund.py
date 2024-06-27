import numpy as np
import pandas as pd


'''
This script will prompt the user to input the matched pool amount, project names, and contributions for each project. It will then calculate the weighted values,
matched amounts, and the % change from the initial funding amount. The script will output the data in a dataframe.

'''

def main():
    
    print(share(dataframeUpdate(getData()), getMatched()))


## prompt user for the total matched amount
def getMatched(): 

    matched_pool = int(input('Enter the total matched amount: '))
    print('Matched Amount: ', matched_pool)
    return matched_pool
    
    
## prompt the user for necessary input data 
def getData():   

    ## establish df and create and update list for project names
    df = pd.DataFrame(columns=['project', 'contributions'])

    ## prompt user for project names and add to list of projects
    projects = []
    i = 'y'
    while i != 'n':
        p = input('Enter project name (n to stop): ')
        i = p
        if i != 'n':
            projects.append(p)
    
    ## get the contributions and write to dataframe along with project name
    for x in range(len(projects)):
        j = 'y'
        while j != 'n':
            q = input('Enter contribution amounts for {} (n to stop): '.format(projects[x]))
            j = q
            if j != 'n':
                q = int(q)
                df.loc[len(df.index)] = projects[x], q
           
    return df
    
    
## calcuate the raw weighted value from the contributions
def dataframeUpdate(df):

    ## calculate sum of funding for each project
    funding = df.groupby('project')['contributions'].sum()

    ## count contributors for each project
    contributors = df.groupby('project')['contributions'].count()
    
    ## take the square root of all individual contributions
    df['sqrt'] = np.sqrt(df['contributions'])

    ## sum the sqrt values for each project
    sum_sqrt = df.groupby('project')['sqrt'].sum()

    ## raise the sum for each project to the 2nd power
    w_value = np.power(sum_sqrt, 2)

    ## create new dataframe with the projects, weighted values, initial funding amounts, and # of contributors
    w_sums = pd.DataFrame({'project':w_value.index, 'funding': funding.values, 'contributors': contributors.values, 'w_value': w_value.values})
    
    return w_sums

## calculate share of matched amount based on weighted values
def share(w_sums, matched_pool):

    ## calculate the total sum of weighted value
    total_sum = w_sums['w_value'].sum()

    ## calculate the weight of each project as a proportion of total sum
    w_sums['weight'] = w_sums['w_value'] / total_sum

    ## multiply the weight by the total matched pool to get matched amount
    w_sums['matched_amount'] = w_sums['weight'] * matched_pool

    ## calculate the % increase of funding on top of the initial amount
    w_sums['% initial amount'] = w_sums['matched_amount'] / w_sums['funding'] * 100

    w_sums = w_sums.round(2)

    return w_sums
    

if __name__ == "__main__":
    main()
    
