import numpy as np
import pandas as pd
import datetime
import json

POST_CODES = {
    'NR1': [52.622186, 1.297853],
    'NR2': [52.630886, 1.273769],
    'NR3': [52.633333, 1.3],
    'NR4': [52.621, 1.264],
    'NR5': [52.633, 1.3]
}


CENTRES = [
    {
        'centre_id': 1,
        'centre_name': 'City College - Adult Learning',
        'address': 'City College, Ipswich Rd, Norwich',
        'postcode': 'NR2 2LJ',
        'webiste': 'https://www.ccn.ac.uk/adults/adult-learning/',
        'x_loc': 52.618144, 
        'y_loc': 1.286325
    },
    {
        'centre_id': 2,
        'centre_name': 'Workers Education Association',
        'address': 'Workers Education Association, 21 King St, Norwich',
        'postcode': 'NR1 1PH',
        'website': 'https://wea-norwich.org.uk/',
        'x_loc': 52.627371,
        'y_loc': 1.299934
    },
    {
        'centre_id': 3,
        'centre_name': 'Norwich International Youth Project',
        'address': '26 Pottergate, Norwich',
        'postcode': 'NR2 1DX',
        'website': 'https://niyp.org.uk/',
        'x_loc': 52.629969, 
        'y_loc': 1.291262
    },
    {
        'centre_id': 4,
        'centre_name': 'New Routes: Social Centre',
        'address': 'Catherine Wheel Opening, Norwich',
        'postcode': 'NR3 3BQ',
        'website': 'https://newroutes.org.uk/',
        'x_loc': 52.638544,
        'y_loc': 1.29169 
    },
    {
        'centre_id': 5,
        'centre_name': 'English+',
        'address': '110A Trinity Street, Norwich',
        'postcode': 'NR2 2BJ',
        'website': 'https://newroutes.org.uk/',
        'x_loc': 52.624777, 
        'y_loc': 1.279956
    }
]


N_CENTRES = len(CENTRES)

LEVELS = [
    'E1',
    'E2',
    'E3',
    'L1',
    'L2'
]

if __name__ == '__main__':

    N_entries = 100

    df = pd.DataFrame({
        'id': 1 + np.arange(N_entries),
        'centre_id': np.random.randint(1, N_CENTRES + 1, N_entries),
        'level': np.random.choice(LEVELS, N_entries),
        'time_start': pd.date_range(start=datetime.datetime.now().replace(hour=9, minute=0, second=0), periods=N_entries, freq='H')
    })

    df['time_end'] = df['time_start'] + pd.Timedelta(hours=1)
    df['is_full'] = np.random.choice([True, False], N_entries, p=[0.3, 0.7])

    df['time_start'] = df['time_start'].dt.strftime('%Y-%m-%d %H:%M:%S')
    df['time_end'] = df['time_end'].dt.strftime('%Y-%m-%d %H:%M:%S')

    df_centres = pd.DataFrame(CENTRES)

    df = df.merge(df_centres, how='left', on='centre_id')

    json_string = df.to_json(orient='records', indent=4)

    with open('../data/entries.json', 'w') as file:
        file.write(json_string)

    

