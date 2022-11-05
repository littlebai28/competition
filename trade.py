# Place any imports you need here!
import pandas as pd
from scipy import stats
# Helpful packages may include numpy, pandas, and sklearn.
class Trader:
    def __init__(self):
        self.team_id = 34 # TODO: CHANGE TO YOUR TEAM’S PASSWORD.
        self.password = "UpI7omaywRqCblA"
        self.totalMAX = 1000000
        self.singleMAX = 600000
        self.pos = {"Stock1":0,"Stock2":0,"Stock3":0,"Stock4":0}
        self.pnl = 0
        self.data = pd.DataFrame(columns=["time","Stock1","Stock2","Stock3","Stock4"])
        self.
# Add any additional info you want

    def MakeTrades(self, time, stock_prices):
        """
        Grader will call this once per timestep to determine your buys/sells.
        Args:
            time: int
            stock_prices: dict[string -> float]
        Returns:
            trades: dict[string -> float] of your trades (quantity) for this
            timestep. Positive is buy/long and negative is sell/short.
        """
        ## Y and Z are numpy arrays or lists of variables 
        #stats.pearsonr(Y, Z)
        stock_prices["time"] = time
        self.data.append(stock_prices, ignore_index=True)
        trades = {"Stock1":0,"Stock2":0}
        # TODO: PICK HOW TO MAKE TRADES.
        # trades['Stock1'] = 1000
        # if 'Stock2' in stock_prices:
        #     if stock_prices['Stock2'] > 123:
        #         trades['Stock2'] = 1000
        # else:
        #     trades['Stock2'] = -1000
        return trades