# NYT-Keyword-Analysis

### Project Overview
The pandemic has changed the way Americans are living their lives. Stuck at home while restaurants are closed and office spaces are slow to reopen, Americans are adapting their behaviors by spending more of their time online and as a result, consuming more media. The United States is also approaching an election which may be, to many Americans, as important as any election before it.

We want to find out the historically important voter issues that Americans are most focused on today and if that has changed from recent election years. We also want to look other historically non-important topics and see how consumer demand for media relating to these ancillary topics has been effected. For this project we will use the New York Times API to retrieve data that is assumed to be representative of media content the average voter is consuming. We will focus on data from Mar, Apr, May, Jun and Jul in each of the previous four election years (2008,2012,2016,2020) during our analysis.

### Questions We Want To Answer
1. Which historically important voter issues are becoming more or less frequent in media publications when compared to recent election years?
2. Which historically non-important topics are becoming more or less frequent in media publications when compared to recent election years?
3. Assuming the New York Times publishes news content based on the average voter's preference, how has the average voter's content preference changed over time?

### Data Source
The New York Times API provides us with raw data related to all published articles by month and year. We used API requests to pull information of all articles published in March - July of 2008, 2012, 2016 and 2020. Collecting the individual keywords and calculating their counts overtime allowed us to plot these keywords in a way that will give the reader a visual representation of the average American voter's media consumption habits.

### If We Had More Time...
We would like to use Natural Language Processsing to analyze these same questions. Part of the returned data from a NYT API call is the lead paragraph of each article. We would like to use the Natural Language Toolkit to complete our own keyword analysis instead of relying on NYT's keywords. In this manner, using NLP algorithms we will be able to analyze for ourselves what people are talking about most.