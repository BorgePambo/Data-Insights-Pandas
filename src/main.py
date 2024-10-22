import pandas as pd
import glob 
import os

def processing_data():
    try:
        path = 'raw/*.csv'
        files = glob.glob(path)

        df_list = []
        if not files:
            print('No csv found in the specified directory')

        else:
        
            df_temp = []
            for file in files:

                df_temp = pd.read_csv(file)

                file_name = os.path.basename(file)
                if 'brazil' in file_name.lower():
                    df_temp['Country'] =  'Brazil'

                elif 'france' in file_name.lower():   
                    df_temp['Country'] = 'France'  

                elif  'usa' in file_name.lower():
                    df_temp['Country'] = 'USA'

                df_list.append(df_temp)

        
        if df_list:
            df_combined = pd.concat(df_list, ignore_index=True)
            df_combined['sale_date'] = pd.to_datetime(df_combined['sale_date'])
            return df_combined  # Retornar o DataFrame combinado
        else:
            return None

        

    except Exception as ex:
        print('Error found it: ', ex)



