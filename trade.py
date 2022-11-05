# Place any imports you need here!
import pandas as pd
# Helpful packages may include numpy, pandas, and sklearn.
class Trader:
    def __init__(self):
        self.team_id = "UpI7omaywRqCblA" # TODO: CHANGE TO YOUR TEAM’S PASSWORD.
        self.totalMAX = 1000000
        self.singleMAX = 600000
        self.pos = {"Stock1":0,"Stock2":0,"Stock3":0,"Stock4":0}
        self.trans={"Stock1":0.0005,"Stock2":0.0010,"Stock3":0.0015,"Stock4":0.0020}
        self.pnl = 0
        self.data = pd.DataFrame(columns=["time","Stock1_Delay","Stock2_Delay","Stock3","Stock4"])
        self.pre1 = 0
        self.pre2 = 0
        self.ar_coef = 0.99998316
        self.ma_coef = 0.5344168
# Add any additional info you wantx

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
        trades = {"Stock1":0,"Stock2":0}
        # price1,price2 = Model(stock_prices)
        #trades["Stock1"] = -self.singleMAX/stock_prices["Stock1"]
        last1 = stock_prices["Stock1_Delay"]
        last2 = stock_prices["Stock2_Delay"]
        # cur1 = last1 * self.ar_coef + self.ma_coef *
        if self.pre1>0: 
            change1 = last1 - self.pre1#self.data[-1]["Stock1_Delay"]
            change2 = last2 - self.pre2#self.data[-1]["Stock2_Delay"]
            #print(change1,change2)
            trades["Stock1"] = max(-1,min((change1/5),1))*(self.singleMAX/stock_prices["Stock1"])
            trades["Stock2"] = max(-1,min((change2/70),1))*(self.singleMAX/stock_prices["Stock2"])
        self.pre1 = last1
        self.pre2 = last2
        #self.data = self.data.append(stock_prices, ignore_index=True)
        return trades
    
    