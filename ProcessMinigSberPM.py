from sberpm import DataHolder
import pandas as pd

path = 'running-example.csv'
data_holder = DataHolder(data=path,
                         id_column='case_id',
                         activity_column='activity',
                         start_timestamp_column='timestamp',
                         user_column='resource',
                         text_column="costs",
                         time_format='%Y-%m-%d %H:%M:%S', sep='|')

data_holder.check_or_calc_duration()
