import pandas as pd
from pytrends.request import TrendReq

# Store the country code in a variable
country_code = 'US'
num_topics = 20

# Use the 'with' statement to automatically close the TrendReq object
with TrendReq() as pytrend:
    # Get today's trending topics in the United States
    # The 'n' parameter specifies the number of topics to return
    trending_today = pytrend.today_searches(pn=country_code, n=num_topics)

# Convert the resulting series to a DataFrame with one column called 'topic'
trending_today_df = trending_today.to_frame(name='topic')

# Print the DataFrame to the console
print(trending_today_df)
