import pandas as pd

def read_aeronet(filename):
    
    dateparse = lambda x: pd.datetime.strptime(x, "%d:%m:%Y %H:%M:%S")
    aeronet = pd.read_csv(filename, skiprows=6, na_values=['N/A'],
                          parse_dates={'Date_and_Time':[0,1]},
                          date_parser=dateparse)
    aeronet = aeronet.set_index('Date_and_Time')
    del aeronet['Day_of_Year']
    del aeronet['Day_of_Year(Fraction)']
    

    an = (aeronet.dropna(axis=1, how='all')
                .dropna(axis=0, how='all')
                .rename(columns={'Last_Processing_Date(dd/mm/yyyy)': 'Last_Processing_Date'})
                .sort_index())

    return an
