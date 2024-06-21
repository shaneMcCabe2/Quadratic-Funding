import math
import pandas as pd

## required = # of projects, list of projects, funding total amount, number of contributors, matched amount


def main():
    ## projects + contribtions

   getData()
    
          
    
    
def getData():   
    df = pd.DataFrame('Project': [], 'Contributions': [])
    projects = []
    contributions = []
    
    while i != 'n':
        p = input('Enter project name (n to stop): ')
        i = p
        projects.append(p)
    
    print(projects)
    
    for x in range(len(projects)):
        while j != 'n':
            q = input('Enter contribution amount for {} (n to stop): '.format(projects[x]))
            j = q
            
           ## contributions.append(q)
            df.loc[len(df.index)] = projects[x], q
            
    print(df)
    
            
            
        
        
        
    


def getMatched(): 
    matched_pool = input('Enter the total matched amount: ')
    print('Matched Amount: ', matched_pool)
    return matched_pool
    
    
    
## contributions = list of individual contributions
def value(contributions):
    sum = 0
    for c in contributions:
       sum += math.sqrt(c)
    
    # z = project weighted raw value
    z = math.pow(sum, 2)
    print('value: ', z)
    return z


def share(value, sum_values, matched_pool):
    
    weight = value / sum_values
    print('weight: ', weight)
    matched_amount = weight * matched_pool
    

if __name__ == "__main__":
    main()
    