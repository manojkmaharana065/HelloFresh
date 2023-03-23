import datetime as dt
from data_sources.logical import Carbon
import os
import logging
import pandas as pd
import json
import time
import math



logging.basicConfig(level=logging.INFO, format='[%(asctime)s] [%(name)s] [%(levelname)s] [%(message)s]',)
logger=logging.getLogger(__name__)


if __name__ == '__main__':
    carbon = Carbon()
    engine = carbon.carbon.engine()


    schema = os.environ["SCHEMA"]
    staging_table = "staging_" + os.environ["TABLE_NAME"]
    recipe_files = json.loads(content)

# Example usage
#process_json_files('/json/recipe_files')

def process_json_files(directory):
    for filename in os.listdir(directory):
        if filename.endswith('.json'):
            filepath = os.path.join(directory, filename)
            with open(filepath, 'r') as f:
                data = json.load(f)
                # Process the JSON data here
                results = data["results"]
            df = pd.DataFrame(results)
            df.to_sql(name=staging_table, schema=schema, con = Carbon().engine(), if_exists='append', index=False, chunksize=10000)

                                                    


