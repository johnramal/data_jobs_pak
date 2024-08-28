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
8. [Setup and Installation](#setup-and-installation)
9. [Running the Project](#running-the-project)
10. [Prerequisites](#prerequisites)
11. [Acknowledgements](#acknowledgements)
12. [License](#license)

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

## Setup and Installation

This project uses a Conda environment. You can set it up using either the `environment.yml` file or the `requirements.txt` file.

### Option 1: Using `environment.yml` (recommended for Conda users)
1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/data_jobs_pak.git
    cd data_jobs_pak
    ```

2. Create and activate the Conda environment:
    ```bash
    conda env create -f environment.yml
    conda activate data_jobs_pk
    ```

### Option 2: Using `requirements.txt`
1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/data_jobs_pak.git
    cd data_jobs_pak
    ```

2. Create and activate a new Conda environment:
    ```bash
    conda create --name data_jobs_pk python=3.12
    conda activate data_jobs_pk
    ```

3. Install the required packages:
    ```bash
    pip install -r requirements.txt
    ```

## Running the Project
After setting up the environment using either method:

1. Launch Jupyter Notebook:
    ```bash
    jupyter notebook
    ```

2. Open and run the notebooks in the `notebooks/` directory.

**Note:** If you encounter any issues with package versions, please refer to the `environment.yml` file for the specific versions used in this project.

## Prerequisites
- Python 3.x
- Jupyter Notebook
- Required Python libraries are listed in `requirements.txt`.

## Acknowledgements
Special thanks to Luke Barousse for providing the dataset on Hugging Face, which served as the foundation for this analysis.

## License

MIT License

Copyright (c) 2024 John Ailia Ramal

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software, associated documentation files, and analysis results (the "Work"),
to deal in the Work without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Work, and to permit persons to whom the Work is furnished to do so,
subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Work.
Any use of this Work must include appropriate credit to the original author.
This license applies only to the analysis code, documentation, and results
produced by the author. The dataset used in this project, sourced from
Luke Barousse's Hugging Face repository, is subject to its own separate
license terms and is not covered by this license.

THE WORK IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE WORK OR THE USE OR OTHER DEALINGS IN THE WORK.
