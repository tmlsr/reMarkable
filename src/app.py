from constants import (
    ENDPOINT, 
    LANDING_ZONE, 
    CURATED_ZONE
)

from tools import (
    api_request,
    create_df,
    export_df,
    ml_tokenize,
    ml_stemming
)


def lambda_handler(event, context):
    """
    Main function and used as the entrypoint for the Lambda function.

    Args:
        context: Provides methods and properties regarding the environment.
        event: Data for the lambda function from invoking the service.
    """

    # extracting data from API
    dict_products = api_request(
        api_endpoint=ENDPOINT
    )

    df_products = create_df(
        dict=dict_products
    )

    export_df(
        df=df_products,
        out_path=LANDING_ZONE,
    )

    # =======================================================================
    # preparing for ML 
    # =======================================================================

    # rename columns
    df_products.rename(
        columns={
          'rating.rate': 'rating_rate',
          'rating.count': 'rating_count'
        }
    )

    # drop duplicates
    df_products = df_products.drop_duplicates()

    # tokenize text
    df_products['title_tokenize'] = df_products['title'].apply(ml_tokenize)
    df_products['description_tokenize'] = df_products['description'].apply(ml_tokenize)

    # stemming text
    df_products['title_stemm'] = df_products['title'].apply(ml_stemming)
    df_products['description_stemm'] = df_products['description'].apply(ml_stemming)

    export_df(
        df=df_products,
        out_path=CURATED_ZONE,
    )


if __name__ == "__main__":
    lambda_handler(None, None)