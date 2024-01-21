# Assignment 2 (coding)

## Description
You work as a data platform engineer in reMarkable, and you are assigned importing data from a partner selling remarkable merchandise. We want the information about what products they sell in our data warehouse and we later want to fit machine learning models to the products data.

<u>Assignment</u>

**Code** a program which does the following:
- Imports all product data from the API into a storage of your own choice
- Then prepare the data for machine learning however you see fit

**Don't code but think** about the following and be prepared to answer questions about:
- How can you turn your program into a data pipeline which is scheduled daily for 
data retrieval to accommodate for changing product data over time.

The product data API can be found here: [https://fakestoreapi.com/](https://fakestoreapi.com/)

You are free to make any assumptions and take shortcuts where you see fit but please explain to us why.
Remember to bring the code to the interview and share the code with us preferably on github or similar.

## Explanation

 I recommend to create a new virtual python environment with [pyenv](https://github.com/pyenv/pyenv) to have a clean and isolated python to test the project.
 
 After the virtual environment is created:

 ### Clone repository
 ```shell
 $ git clone git@github.com:tmlsr/reMarkable.git
 ```

### Install dependencies
```shell
$ poetry install
```

It's necessary to download and install needed libraries for nltk:
```shell
$ python -m nltk.downloader all     
```

### Run the script:
Navigate to the remarkable root dir
```shell
$ python src/app.py
```

### datalake
Used as storage solution to store the data as in different zones.

landing_zone:
- RAW data
- Partitioned
- load_date added 

curated_zone:
- ML prepared data
- Partitioned 


### data_exploration
Jupyter notebook is used to do first and simple data exploration tasks.



