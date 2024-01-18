import os
import requests
import pandas as pd
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from typing import Tuple
from datetime import datetime


def api_request(
    api_endpoint: str,
) -> dict:
    """
    This function makes a request to the products API endpoint and returns all
    products.

    Args:
        api_endpoint(str): The endpoint to make the request to.

    Returns:
        dict: A dictionary of all products.
    """
    try:
        response = requests.get(
            url=api_endpoint,
            timeout=10
        )

        if response.status_code == 200:
            return response.json()
        else:
            msg = f'API call failed with status code: {response.status_code}'
            print(msg)
            raise
    except Exception as e:
        error_msg(
            method_name=sys._getframe().f_code.co_name,
            exception=e
        )
        raise


def create_df(
    dict: dict
) -> pd.DataFrame:
    """
    This function creates a dataframe from a dictionary and adds the load_date.

    Args:
        dict_products(dict): A dictionary of products.

    Returns:
        pd.DataFrame: A dataframe with added load_date.
    """
    day, month, year = date_today()

    try:
        
        df = pd.json_normalize(dict)
        df['load_date'] = f'{year}-{month}-{day}'
        return df
    except Exception as e:
        error_msg(
            method_name=sys._getframe().f_code.co_name,
            exception=e
        )
        raise


def export_df(
        out_path: str,
        df: pd.DataFrame,
) -> None:
    """
    This function exports a dataframe to the datalake as json file.

    Args:
        out_path(str): The path to export the json file to.
        df(pd.DataFrame): The dataframe to export.
    """
    day, month, year = date_today()

    out_file = f'products_{year}{month}{day}.json'
    out_location = f'{out_path}/products/{year}/{month}/{day}/'

    try:
        if not os.path.exists(out_location):
            os.makedirs(out_location)
        
        df.to_json(out_location + out_file, orient='records', mode='w')
    except Exception as e:
        error_msg(
            method_name=sys._getframe().f_code.co_name,
            exception=e
        )
        raise


def date_today(
        dt=datetime.now()
) -> Tuple[str, str, str]:
    """
    This function uses the datetime object to split and create respective 
    time parts.

    Args:
        dt (timestamp): Timestamp value which will be initialized with
            datetime.now()

    Returns:
        time_parts (tuple): Tuple with respective time parts to get
    """
    try:
        time_parts = (
            str(dt.day).zfill(2),
            str(dt.month).zfill(2),
            str(dt.year)
        )

        return time_parts

    except Exception as e:
        error_msg(
                method_name=sys._getframe().f_code.co_name,
                exception=e
            )
        raise


def error_msg(
        method_name: str,
        exception: Exception
) -> str:
    """Wrapping the exception information and method name into an error message

    Args:
        method_name (str): Method name which called the function
        exception (Exception): Information about the exception

    Returns:
        error_msg (str): Error message with method name and exception
    """
    error_msg = (
        f'===> ERROR in method: {method_name}'
        f'{os.linesep} Exception: {exception}'
    )
    return error_msg


def ml_tokenize(
        text: str
) -> list:
    """
    This function tokenizes a text.

    Args:
        text(str): The text to tokenize.

    Returns:
        list: A list of tokens.
    """
    try:
        tokens = word_tokenize(text)
        tokens = [word.lower() for word in tokens if word.isalpha()]
        stop_words = set(stopwords.words('english'))
        tokens = [word for word in tokens if word not in stop_words]

        return tokens

    except Exception as e:
        error_msg(
            method_name=sys._getframe().f_code.co_name,
            exception=e
        )
        raise


def ml_stemming(
        text: str
) -> list:
    """
    This function for stemming a text.

    Args:
        text(str): The text for stemming.

    Returns:
        list: A list of stemmed words.
    """
    try:
        tokens = word_tokenize(text)
        tokens = [word.lower() for word in tokens if word.isalpha()]
        stop_words = set(stopwords.words('english'))
        tokens = [word for word in tokens if word not in stop_words]

        porter_stemmer = PorterStemmer()
        stemmed_tokens = [porter_stemmer.stem(word) for word in tokens]

        return ' '.join(stemmed_tokens)

    except Exception as e:
        error_msg(
            method_name=sys._getframe().f_code.co_name,
            exception=e
        )
        raise
