from pytrends.request import TrendReq
import pandas as pd
import matplotlib.pyplot as plt
 
pytrends = TrendReq(hl='pt-BR', tz=180)
 
kw_list = ["black friday"]
pytrends.build_payload(kw_list, cat=0, timeframe='today 12-m', geo='BR', gprop='')
 

# Get Google trends search interest
search_interest = pytrends.interest_over_time()
 

# Get Google trends related topics
related_topics = pytrends.related_topics()
 

# Google trends related queries
related_queries = pytrends.related_queries()


# Get Google trends top related queries
related_queries['black friday']['top']


# Get Google trends rising related queries
related_queries['black friday']['rising']
 

# Google trends suggestion queries
suggestion_queries = pytrends.suggestions(keyword = 'black friday')

#Visualise Web Search Interest overtime of your keyword
plt.plot(search_interest)
plt.show()
