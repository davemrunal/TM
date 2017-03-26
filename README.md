Big Data 2016 Project - Understanding NYC Taxi Usage

This repository contains Python scripts to analyse NYC Yellow and Green Taxi trips taken during year the 2015 using Hadoop streaming and MapReduce on Amazon EMR cluster


The repository has been structured as follows:
 > Under the 'Analysis' folder, there are sub folders for different type of analysis over the data like monthlyAnalysis,    quarterlyAnalysis, dailyAnalysis, etc.
 > Each of these sub directories contain the source codes for Map and Reduce and each of the source files are named accordingly and are self explanaory. That is, if a file in dailyAnalysis folder says 'dailyTotalRevenueMap' and 'dailyTotalRevenue', then it means that these two files will calculate daily total revenue and the output file will have 365 lines.
 > Under the AWSResults folder, there are output files when all of the above codes were run on AWS with all data hosted on S3 bucket. Again, the file names are self explanatory.
