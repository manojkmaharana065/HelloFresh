from data_sources.logical import Carbon
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



    # Delete data from main table
    logger.info("Drop Staging Table")
    create_carbon_table_command = """DROP TABLE {schema}.staging_{table}""".format(schema=schema, table=table)
    with engine.begin() as conn:
        conn.execute(create_carbon_table_command)





            