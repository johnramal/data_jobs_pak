# Data Job Market Analysis: Pakistan and Comparative Countries

This project analyzes the data job market in Pakistan and compares it with other countries of similar GDP levels, including Egypt, Nigeria, Turkey, and Bangladesh. The analysis includes exploratory data analysis (EDA), a comparative study, a detailed focus on Pakistan's job market, and an in-depth skills trend analysis.

## Table of Contents
1. [Introduction](#introduction)
2. [Exploratory Data Analysis (EDA)](#exploratory-data-analysis-eda)
3. [Comparative Analysis](#comparative-analysis)
4. [Detailed Analysis of Pakistan's Data Job Market](#detailed-analysis-of-pakistans-data-job-market)
5. [Skills Trend Analysis in Pakistan](#skills-trend-analysis-in-pakistan)
6. [Conclusions](#conclusions)
7. [Data Source](#data-source)
8. [Getting Started](#getting-started)
9. [Acknowledgements](#acknowledgements)
10. [License](#license)

## Introduction
This repository contains a comprehensive analysis of the data job market, focusing on Pakistan and several comparative countries. The analysis is divided into four notebooks, each covering a different aspect of the study.

## Exploratory Data Analysis (EDA)
In this notebook, we import the dataset from Luke Barousse's Hugging Face repository and filter for data-related jobs. The filtered datasets are saved as `df_pak.csv` and `df_comparison_countries.csv`. Unfortunately, due to a lack of salary information in most postings, we were unable to perform a statistically significant numerical analysis on salary data.

![EDA Visualization](path_to_your_image)

## Comparative Analysis
This notebook compares job postings in Pakistan with those in Egypt, Nigeria, Turkey, and Bangladesh. The analysis shows that most data-related jobs are posted by non-local companies such as Vodafone, Data2Bots, and JP Morgan Chase. Additionally, we observe that a significant number of job postings do not explicitly mention degree requirements, and there is a lack of health insurance benefits across the board, with Egypt offering the least work-from-home opportunities.

![Comparative Analysis Visualization](path_to_your_image)

## Detailed Analysis of Pakistan's Data Job Market
This notebook provides a deeper look into Pakistan's data job market, revealing that technical roles like Data Engineer and Data Scientist are more prevalent than business analyst and senior roles. This could indicate the early stages of a data-driven trend in Pakistan. Notably, most job postings are from foreign companies or contractors for foreign companies, with Lahore leading in the number of postings, followed by Karachi and Islamabad.

![Pakistan Job Market Visualization](path_to_your_image)

## Skills Trend Analysis in Pakistan
In this notebook, we focus on the skill requirements for data jobs in Pakistan, analyzing the distribution of the top 10 skills across various job titles. The analysis includes a blob chart for skill distribution and a radar chart for visualization. Python, SQL, AWS, and Tableau emerge as the top skills. We also perform a time analysis from January to December, finding no significant fluctuations in skill requirements.

![Skills Trend Visualization](path_to_your_image)

## Conclusions
The analysis provides insights into the emerging data job market in Pakistan and offers a comparative perspective with other countries of similar GDP. The findings highlight the growing demand for technical skills and the role of foreign companies in shaping the job landscape.

## Data Source
The dataset used in this project is sourced from [Luke Barousse's Hugging Face repository](https://huggingface.co/datasets/lukebarousse/data_jobs). The data includes job postings from various countries and was instrumental in performing the analyses presented in this project.

## Getting Started
To clone this repository and get started with the analysis:

```bash
git clone https://github.com/johnramal/data-job-analysis.git
cd data-job-analysis
