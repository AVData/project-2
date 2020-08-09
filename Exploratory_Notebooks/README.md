# Exploratory Analysis of Collision Data from the [Los Angeles Police Department](https://data.lacity.org/A-Safe-City/Traffic-Collision-Data-from-2010-to-Present/d5tf-ez2w)

## In this exploratory analysis I will explore traffic collision data with the aim of generate probabilitsic predictions of collisions given a set of parameters.

###### Note: I initially began working with the complete dataset spanning 2010 to present day.  I have since changed that approach to only include a max of 500k rows of data collected from the [City of Los Angeles API](https://dev.socrata.com/foundry/data.lacity.org/d5tf-ez2w).  Connecting to the API allows one to query data more efficiently after cleaning.

### Steps of Exploration:
- Clean data
- Determine baselines
- Choose Classification or Regression
- Determine model baselines
- Choose best model with ROC/AUC