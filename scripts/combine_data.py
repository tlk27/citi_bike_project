# import pandas as pd 
# import glob
# import os


def combine_data(path, sample = False, fraction = None, write_csv = False, file_name = ''):
    '''
    This function will read in csv files from a path and concatenate them by row.
    If sample is indicated as True, the function will allow you to sample a fraction of each data frame.
    By default, fraction is set to 1 (100%).
    
    Similarly, write_csv = True will allow you write the newly concatenated data frame to a csv.
    The file name can be specified under file_name. 
    ------------------------------------------------------------
    Inputs:
    
        path = file path - string format
        sample = bool, True or False
        fraction = int, the proportion of data to sample
        write_csv = bool, True or False
        file_name = string, representing the desired file name
    
    Returns:
        
        Either a csv with the given file name or a data frame.
    
    '''
    df_list = []
    
    all_files = glob.glob(os.path.join(path, '*.csv'))
    
    for file in all_files:
        if sample == True:
                df1 = pd.read_csv(file)
                df1.columns = df1.columns.str.replace(' ', '').str.lower()
                df_sample = df1.sample(frac = fraction)
                df_list.append(df_sample)
        if sample == False:
            df = pd.read_csv(file)
            df.columns = df.columns.str.replace(' ', '').replace(':', '').str.lower()
            df_list.append(df)
   
    concatenated_df = pd.concat(df_list, axis = 0)
    
    if write_csv:
        concatenated_df.to_csv(file_name, index = False )
    else:
        return concatenated_df