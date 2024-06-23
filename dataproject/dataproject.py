def keep_regs(df, regs):
    """ Example function. Keep only the subset regs of regions in data.

    Args:
        df (pd.DataFrame): pandas dataframe 

    Returns:
        df (pd.DataFrame): pandas dataframe

    """ 
    
    for r in regs:
        I = df.reg.str.contains(r)
        df = df.loc[I == False] # keep everything else
    
    return df

def calculate_returns(dataframe):
    """
    Calculate monthly and cumulative returns for a given DataFrame of stock prices

    Parameters:
    dataframe (pd.DataFrame): A pandas DataFrame where each column represents a stock and each row represents a time period (e.g., month)

    Returns:
    tuple: A tuple containing:
        - pd.DataFrame: Monthly returns for each stock
        - pd.DataFrame: Cumulative returns for each stock
    """
    # Calculate monthly returns using the pct_change() function
    monthly_return = dataframe.pct_change()

    # Calculate cumulative returns using the cumprod() function
    cumulative_return = (1 + monthly_return).cumprod()

    # Returns monthly and cumulative stock returns
    return monthly_return, cumulative_return

