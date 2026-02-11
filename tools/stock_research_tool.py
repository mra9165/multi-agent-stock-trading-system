import yfinance as yf
from crewai.tools import tool
@tool("Live stock information tool")
def get_stock_price(stock_symbol:str)-> str:
    """
    Retrieves the latest stock price and other info for a given stock symbol using Finance
    parameters:
        stock_symbol (str): Stock ticker symbol (e.g., AAPL, TSLA)
    Returns:
        str: Summary of stock price and daily change

    """
    stock= yf.Ticker(stock_symbol)
    info= stock.info
    current_price= info.get("regularMarketPrice")
    change= info.get("regularMarketChange")
    change_percent = info.get("regularMarketChangePercent")
    currency= info.get("currency","USD")
    if current_price is None:
        return f"Could not fetch price for {stock_symbol}.Please check the symbol"
    return (
        f"Stock: {stock_symbol.upper()}\n"
        f"Price: {current_price}{currency}\n"
        f"Change:{change}({round(change_percent,2)}%)"
    )
# print(get_stock_price("AAPL"))
