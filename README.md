# Real-Time-Analysis-of-Reddit-Comment-Streams

## Time Windows

### Overview

This section of the project involves the collection and analysis of streaming data from Reddit using the Reddit Stream API. The goal is to understand and apply different windowing techniques, namely Tumbling Window and Hopping Window, to analyze temporal data from two subreddits: AskUK and AskAnAmerican.

### Implementation Files

The analysis is performed in two primary files:

* reddit_listener.py: A Python script responsible for streaming and collecting data from the Reddit API.
* reddit_analytics.ipynb: A Jupyter notebook used for data analysis.

### Instructions for Data Collection

#### Task 1.1: Data Collection

* Run the reddit_listener.py script to collect 4 hours of data from the subreddits AskUK and AskAnAmerican.
* Ensure a stable collection process, possibly utilizing Google Cloud Platform's Vertex AI Notebook and disabling any idle shutdown features.
* Store the data in a CSV file with attributes such as author, id, submission, body, subreddit, created_utc, and collected_utc.

#### Task 1.2: Data Analysis

* Using the data from the CSV file:
** Compute and visualize the number of unique users per subreddit with a tumbling window of 20 minutes and a hopping window of 20 minutes with a 5-minute hopping size. Discuss the observed differences between the subreddits.
** Calculate and plot the average number of words per comment for each subreddit using the same windowing techniques. Discuss any differences noticed between the window types.


## Streaming Analysis

### Overview

This segment focuses on real-time data streaming and analysis of Reddit comments. It involves modifying the provided RedditProducer class to send data through a network socket and analyzing the streaming data using Spark's streaming capabilities.

### Objectives

* To further develop skills in handling and analyzing streaming big data.
* To learn and apply the documentation of big data tools effectively.
* To create advanced data visualizations based on real-time data streams.

### Implementation Files

The solution comprises two scripts:

* reddit_producer.py: This script is responsible for connecting to the Reddit API, collecting comments, and streaming them through a network socket to a designated port.
* spark_consumer.ipynb: A Jupyter notebook that establishes a Spark context to consume the streamed data, perform analyses, and generate visualizations.

### Instructions for Streaming Analyses

#### Task Overview
Leverage Spark's structured streaming capabilities to perform the following analyses:

* Timestamp Printing: Log the arrival timestamps of comments in the Spark streaming resource.
* Unique Words Visualization: Every 10 seconds, plot the average number of unique words per comment, with time on the x-axis and the average count on the y-axis.
* Cumulative Unique Words Plot: Create a plot displaying the cumulative count of unique words in comments, updated every 10 seconds, for both AskUK and AskAnAmerican subreddits. Compare the trends and hypothesize any observed differences.
* Real-Time Regression Modeling: Use a regression model from the River library to predict the number of unique words in a comment based on its length, training the model in real-time with the streaming data.


