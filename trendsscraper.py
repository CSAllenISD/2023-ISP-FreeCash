import pandas as pd
from pytrends.request import TrendReq
pytrend = TrendReq()

#get today's treniding topics
trendingtoday = pytrend.today_searches(pn='US')
print(trendingtoday.head(20))
