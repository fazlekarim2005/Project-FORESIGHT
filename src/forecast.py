def seasonal_naive(series,season=7,horizon=7): return list(series[-season:])*((horizon+season-1)//season)
