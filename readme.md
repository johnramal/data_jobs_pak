# Data Job Market Analysis: Pakistan

This project provides an in-depth analysis of the data job market in Pakistan for the year 2023, with a comparative overview of similar GDP-level countries: Egypt, Nigeria, Turkey, and Bangladesh. The study includes exploratory data analysis (EDA), a brief comparative analysis, a detailed examination of Pakistan’s job market, and a comprehensive skills trend analysis.
 

## Table of Contents
1. [Introduction](#1-introduction)
2. [Analysis](#2-analysis)
   1. [Exploratory Data Analysis (EDA)](#21-exploratory-data-analysis-eda)
   2. [Comparative Analysis](#22-comparative-analysis)
   3. [Detailed Analysis of Pakistan's Data Job Market](#23-detailed-analysis-of-pakistans-data-job-market)
   4. [Skills Trend Analysis in Pakistan](#24-skills-trend-analysis-in-pakistan)
3. [Conclusions](#3-conclusions)
4. [Recreate this project](#4-recreate-this-project)
5. [Acknowledgements](#5-acknowledgements)
6. [License](#6-license)


## 1. Introduction
This repository contains a comprehensive analysis of the data job market, focusing on Pakistan. The analysis is divided into four notebooks, each covering a different aspect of the study.

## 2. Analysis
### 2.1. Exploratory Data Analysis (EDA)

In this [notebook](https://github.com/johnramal/data_jobs_pak/blob/main/notebooks/1_eda.ipynb), the dataset from Luke Barousse's Hugging Face repository was processed to focus on data-related jobs.

The analysis involved cleaning the data by removing duplicate job postings and correcting data types. The `job_skills` column was converted from a string to a list for a more detailed skill analysis. Two filtered datasets were created: `df_pak.csv` for Pakistan only and `df_comparison_countries.csv` for Egypt, Nigeria, Turkey, Bangladesh, and Pakistan.

It's important to note that salary information was largely missing from the job postings, making a statistically significant salary analysis impossible.

### 2.2. Comparative Analysis

#### 1. Approach

In this [notebook](https://github.com/johnramal/data_jobs_pak/blob/main/notebooks/2_comaprative_analysis.ipynb), we compare job postings in Pakistan with those in Egypt, Nigeria, Turkey, and Bangladesh. The analysis focuses on identifying patterns in job postings across these countries, with particular attention to the companies offering these jobs, degree requirements, and available benefits such as health insurance and work-from-home options.

#### 2. Insights

- **Jobs Per Company**: The majority of data-related job postings are from non-local companies, including Vodafone, Data2Bots, and JP Morgan Chase, indicating a strong presence of international firms in the job markets of these countries.

  ![jobs per company](/insights_graphs/jobs_per_company.png)

- **Benefit Analysis**: A significant number of job postings do not explicitly mention degree requirements. Additionally, there is a noticeable lack of health insurance benefits across all countries, with Egypt offering the fewest work-from-home opportunities.

  ![benefit analysis](/insights_graphs/benefit_analysis.png)


### 2.3. Detailed Analysis of Pakistan's Data Job Market

#### 1. Approach

In this [notebook](https://github.com/johnramal/data_jobs_pak/blob/main/notebooks/3_detailed_analysis_pak.ipynb), weconducted an in-depth analysis of Pakistan's data job market using the `df_pak.csv` dataset. The focus was on understanding the distribution of job postings across various cities, the types of roles available, and the companies posting these jobs.

#### 2. Insights

- **Jobs Per Title**: Technical roles such as Data Engineer and Data Scientist are more common than business analyst and senior roles. This trend suggests that Pakistan is in the early stages of adopting data-driven practices, with a growing demand for technical expertise.

  ![jobs per title](/insights_graphs/jobs_per_title_pak.png)

- **Jobs Per Company**: Most job postings are from foreign companies or contractors for foreign companies, highlighting the influence of international businesses in Pakistan's data job market.

  ![jobs per company](/insights_graphs/jobs_per_company_pak.png)

- **Jobs Per City**: Lahore leads in the number of job postings, followed by Karachi and Islamabad. This distribution indicates that these cities are emerging as hubs for data-related jobs in Pakistan.

  ![jobs per city](/insights_graphs/job_count_by_city_and_title_pak.png)


### 2.4. Skills Trend Analysis in Pakistan

#### 1. Approach

In this [notebook](https://github.com/johnramal/data_jobs_pak/blob/main/notebooks/4_skills_trends_pak.ipynb), we analyze the skill requirements for data jobs in Pakistan. The analysis explores the distribution of the top 10 skills across various job titles using a blob chart and examines skill requirements through a radar chart. Additionally, a time-based analysis from January to December was conducted to observe any trends or fluctuations in skill demand.

#### 2. Insights

- **Top Skills**: Python, SQL, AWS, and Tableau are identified as the most sought-after skills in Pakistan's data job market. These skills are consistently required across various job titles, indicating their importance for data professionals in the country.

  ![blob chart](/insights_graphs/top_skills_distribution_blob.png)

- **Required Skills by Job Posting**: The radar chart illustrates the specific skill requirements as mentioned in job postings, reinforcing the prominence of Python, SQL, AWS, and Tableau. Data engineer postings were most demanding in terms of technical skills, while less than 50 percent of postings for data analysts, had any technical skills mentioned.

  ![required skills](/insights_graphs/job_requirement_radar.png)

- **Monthly Skill Trend**: A time-based analysis from January to December shows that there are no significant fluctuations in skill requirements throughout the year, indicating a stable demand for these core skills.

  ![radar chart for skill trend](/insights_graphs/skill_liklyhood_monthly_trend.png)


## 3. Conclusions

This project provides a detailed examination of the data job market in Pakistan, with a brief comparative analysis against Egypt, Nigeria, Turkey, and Bangladesh. The primary focus is on Pakistan, offering insights into job postings, skill demands, and geographic distribution.

1. **Pakistan's Data Job Market**:
   - **Role Distribution**: The analysis reveals a strong demand for technical roles such as Data Engineers and Data Scientists in Pakistan, surpassing business-focused roles. This indicates an emerging emphasis on technical expertise within the country’s data sector.
   - **Skill Demand**: Key skills in demand include Python, SQL, AWS, and Tableau. These skills are consistently required across various job titles, highlighting their significance in Pakistan's data job market.
   - **Geographic Distribution**: Major cities like Lahore, Karachi, and Islamabad are prominent centers for data job postings. This concentration suggests these urban areas are crucial hubs for data-related opportunities in Pakistan.
   - **Company Distribution**: Many job postings are from foreign companies or contractors, emphasizing the impact of international businesses on Pakistan's data job market.

2. **Comparative Analysis**:
   - **Scope**: The comparative analysis, which constitutes less than 10% of the overall analysis, provides a brief overview of job markets in Egypt, Nigeria, Turkey, and Bangladesh. While insightful, this comparison is secondary to the primary focus on Pakistan.

3. **Data Limitations**:
   - **Dataset Size**: The analysis is based on 1,370 job postings for the year 2023. This limited dataset may not fully capture the entire job market and could affect the generalizability of the findings.
   - **Dataset Accuracy**: The accuracy of the insights is dependent on the dataset obtained from the mentioned source. Individual postings have not been verified firsthand, which may impact the reliability of specific data points.

In summary, this project underscores the growing significance of technical roles and core skills in Pakistan's data job market, with a clear focus on major urban centers. The limited comparative analysis provides additional context but does not overshadow the primary insights related to Pakistan's job market. Future research could enhance understanding by incorporating a larger and more verified dataset.

## 4. Recreate This Project

If you wish to recreate this project, follow the steps below to set up the environment, install necessary dependencies, and run the notebooks.

### Data Source and Prerequisites

The dataset used in this project is sourced from [Luke Barousse's Hugging Face repository](https://huggingface.co/datasets/lukebarousse/data_jobs). The data includes job postings from various countries and was instrumental in performing the analyses presented in this project.

#### Prerequisites
- Python 3.x
- Jupyter Notebook
- Required Python libraries (listed in `requirements.txt`)

### Setup, Installation, and Running the Project

This project uses a Conda environment. You can set it up using either the `environment.yml` file or the `requirements.txt` file.

#### Option 1: Using `environment.yml` (recommended for Conda users)
1. Clone the repository:
    ```bash
    git clone https://github.com/johnramal/data_jobs_pak.git
    cd data_jobs_pak
    ```

2. Create and activate the Conda environment:
    ```bash
    conda env create -f environment.yml
    conda activate data_jobs_pk
    ```

#### Option 2: Using `requirements.txt`
1. Clone the repository:
    ```bash
    git clone https://github.com/johnramal/data_jobs_pak.git
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

### Running the Project
After setting up the environment using either method:

1. Launch Jupyter Notebook:
    ```bash
    jupyter notebook
    ```

2. Open and run the notebooks in the `notebooks/` directory.

**Note:** If you encounter any issues with package versions, please refer to the `environment.yml` file for the specific versions used in this project.

## 5. Acknowledgements
Special thanks to [Luke Barousse](https://www.youtube.com/@LukeBarousse) for providing the dataset on Hugging Face, which served as the foundation for this analysis.

## 6. License

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
