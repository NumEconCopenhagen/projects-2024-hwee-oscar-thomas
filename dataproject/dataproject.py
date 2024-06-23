import matplotlib.pyplot as plt
import plotly.graph_objects as go

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

def plot_summary_statistics(grouped_returns, industry1, industry2):
    """
    Plot summary statistics for selected industries.

    Parameters:
    grouped_returns (pd.DataFrame): A pandas DataFrame containing grouped returns of stocks.
    industry1 (str): The first industry to plot.
    industry2 (str): The second industry to plot.
    """
    # Filter for the selected industries
    selected_industries = grouped_returns[[industry1, industry2]]
    
    # Describe the grouped returns to get summary statistics
    summary_stats = selected_industries.describe().iloc[[1, 2], :]  # Select mean and std rows
    
    # Plot the summary statistics
    plt.figure(figsize=(10, 6))
    summary_stats.plot(kind='bar', figsize=(10, 6))
    plt.title(f'Summary Statistics for {industry1} and {industry2}')
    plt.ylabel('Values')
    plt.xlabel('Statistics')
    plt.xticks(rotation=45)
    plt.legend(title='Sectors', bbox_to_anchor=(1.05, 1), loc='upper left')
    plt.tight_layout()
    plt.show()

# Function to plot a line graph of cumulative returns for each stock
def plot_cumulative_returns(cumulative_returns, selected_companies):
    fig = go.Figure()
    for company in selected_companies:
        fig.add_trace(go.Scatter(x=cumulative_returns.index, y=cumulative_returns[company], mode='lines', name=company))

    fig.update_layout(title='Cumulative Returns of Selected S&P 500 Companies',
                      xaxis_title='Date',
                      yaxis_title='Cumulative Returns',
                      hovermode='x unified')
    fig.show()

