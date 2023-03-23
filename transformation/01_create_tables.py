import os
import HELLOFRESH.schema_config.recipe_schema as config
import logging


logging.basicConfig(level=logging.INFO, format='[%(asctime)s] [%(name)s] [%(levelname)s] [%(message)s]',)
logger=logging.getLogger(__name__)


if __name__ == '__main__':

    carbon = Carbon()
    engine = carbon.engine()

    schema = os.environ["SCHEMA"]
    table = os.environ["TABLE_NAME"]


    # Drop staging table if exist - helps in recovering from failures
    logger.info("Drop Stging Table")
    create_carbon_table_command = """IF Object_ID('{schema}.staging_{table}') IS NOT NULL DROP TABLE {schema}.staging_{table}""".format(schema=schema, table=table)
    with engine.begin() as conn:
        conn.execute(create_carbon_table_command)



    # Create Staging Table
    logger.info("Create Staging Table")
    columnstringlist = [f'{col[0]} {col[1]}' for col in config.TABLE_COLUMNS]
    columnstring = ','.join(columnstringlist)
    create_carbon_table_command = """IF Object_ID('{schema}'.staging_{table}') IS NULL CREATE TABLE {schema}.staging_{table} ({columns_and_types})""".format(schema=schema, columns_and_types=columnstring, table=table)
    logger.info(create_carbon_table_command)
    with engine.begin() as conn:
        conn.execute(create_carbon_table_command)


    # create main table
    logger.info("Create Main Table")
    columnstringlist = [f'{col[0]} {col[1]}' for col in config.TABLE_COLUMNS]
    columnstring = ','.join(columnstringlist)
    create_carbon_table_command = """IF Object_ID('{schema}'.{table}') IS NULL CREATE TABLE {schema}.{table} ({columns_and_types})""".format(schema=schema, columns_and_types=columnstring, table=table)
    logger.info(create_carbon_table_command)
    with engine.begin() as conn:
        conn.execute(create_carbon_table_command)
        


