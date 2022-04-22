# Benfords Law Twitter

## Objective
This project aims to analyze if [Benford's Law](https://en.wikipedia.org/wiki/Benford%27s_law) holds in the context of Twitter followers. 

## Experiment
The script fetches the list of users that the user is following. We find out the `follower_count` of all such users and bucket them
based on the first digit of the follower count. The program draws a bar plot of the total number of `follower_count` starting with each digit.

## Observation
We observe that the bar plot mostly fits Benford's Law prediction.

Note: I've used twitter's personal access token to retrieve data which could be against Twitter's rule. Please use this script with caution if you try to use your token to run the code.
