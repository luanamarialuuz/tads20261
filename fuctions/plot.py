from fuctions.data import download_history
from plotly.graph_objects import Figure
import plotly.express as px


def plot_history(ticker:str) -> Figure:

     
    """
    Flot historical data  from yahoo finance.

    Args:
        ticker (str): Ticker name.

    """
    
    df = download_history(ticker)

    fig = px.line(
        df,
        x = 'Date',
        y= 'Close', 
        title = f'{ticker} stock price.'
    )
    
    return fig