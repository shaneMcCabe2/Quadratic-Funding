import math
import pandas as pd

## required = # of projects, list of projects, funding total amount, number of contributors, matched amount


def main():

    df = dataframeUpdate(getData())
    
    
## prompt the user for necessary input data 
def getData():   

    ## establish df and create and update list for project names
    df = pd.DataFrame(columns=['Project', 'Contributions'])
    projects = []
    i = 'y'

    while i != 'n':
        p = input('Enter project name (n to stop): ')
        i = p
        if i != 'n':
            projects.append(p)
    
    ## get the contributions for each project
    for x in range(len(projects)):
        j = 'y'
        while j != 'n':
            q = input('Enter contribution amounts for {} (n to stop): '.format(projects[x]))
            j = q
            if j != 'n':
                df.loc[len(df.index)] = projects[x], q
           
    return df
    
## prompt user for the total matched amount
def getMatched(): 
    matched_pool = input('Enter the total matched amount: ')
    print('Matched Amount: ', matched_pool)
    return matched_pool
    
    
## calcuate the raw weighted value from the contributions
def dataframeUpdate(df):
    total_sum = 0
    projects = df['Project']
    contributions = df['Contributions']
    sqrt = math.sqrt(df['Contributions'])

    
    
    ## not sure about how to implement below cleanly just yet
    w_value += math.sqrt(c)
    w_value = 0
    # w = project weighted raw value
    w = math.pow(w_value, 2)
    


def share(w_value, sum_values, matched_pool):
    
    weight = value / sum_values
    print('weight: ', weight)
    matched_amount = weight * matched_pool
    

if __name__ == "__main__":
    main()
    