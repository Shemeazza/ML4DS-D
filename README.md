# ML4DS-D

This is a GitHub repository for **Machine Learning for Data Science** course By IPB

This ML algorithm is supposed to predict a Customer "type" from a Sydney water bill usage data set provided for the assignment.

# Basic Info 

There are **7** types of customers:
* Rural commercial - mid-sized agro-production consumers
* industrial - industries
* construction - construction related companies and sites
* domestic - regular house consumers
* rural expansion - agro-production companies that don’t categorize as one of the previous
* low income families - families with social security support
* rural domestic - small companies or familiar agro-production consumers


The Dataset has 5 features 1 label 
* **Year** – the year of the record *(int)* - The Record are From 2013 to 2020 
 <font color="red"> **Year 2015 is missing** </font>
* **Month** – the month of the consumption record *(int)*
* **Consumer_type** – this is the **label**, corresponding to the type of the consumer *(string)*
* **Consumption** – water consumption in cubic meters *(int)*
* **Consumer_numer** – the ID of the consumer *(string)*
* **Installation_zone** – the area in the region where the water was consumed *(string)*

# Our Goal

Our Goal is to train an algorithm based on [train.csv](https://github.com/Shemeazza/ML4DS-D/blob/main/train.csv) and be able to predict a Customer_type (our **Label**) based on **features** of our data set and then using our testing dataset [competition.csv](https://github.com/Shemeazza/ML4DS-D/blob/main/competition.csv) assign a proper type. Then create a report of our results, and generate *.cvs* files from our algorithm using **3 different prediction models**( so 3 diffrent .csv files).

