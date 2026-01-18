import pandas as pd
import os

def normalize_data_sc(
        df_acc_hist_0,
        df_bal_sheet_0,
        df_cash_stat_0,
        df_inco_stat_0,
        ):

    #################################################################################################################
    ########### Recuerde Agregar los nuevos archvos CSV descargados a la carpeta temp ###############################
    #################################################################################################################

    # Normalizar Columna de Fechas
    df_acc_hist_0['Timestamp'] = pd.to_datetime(df_acc_hist_0['Timestamp']).dt.strftime('%Y-%m-%d %H:%M:%S')
    df_bal_sheet_0['Timestamp'] = pd.to_datetime(df_bal_sheet_0['Timestamp']).dt.strftime('%Y-%m-%d %H:%M:%S')
    df_cash_stat_0['Timestamp'] = pd.to_datetime(df_cash_stat_0['Timestamp']).dt.strftime('%Y-%m-%d %H:%M:%S')
    df_inco_stat_0['Timestamp'] = pd.to_datetime(df_inco_stat_0['Timestamp']).dt.strftime('%Y-%m-%d %H:%M:%S')

    # Actuality.......

    # Cargar los archivos CSV nuevos
    df_acc_hist = pd.read_csv(r'C:\Users\pc\OneDrive\Escritorio\data_sim_company\temp\sim-companies-account-history-Kalesshia.csv')
    df_bal_sheet = pd.read_csv(r'C:\Users\pc\OneDrive\Escritorio\data_sim_company\temp\sim-companies-balance-sheet.csv')
    df_cash_stat = pd.read_csv(r'C:\Users\pc\OneDrive\Escritorio\data_sim_company\temp\sim-companies-cashflow-statement.csv')
    df_inco_stat = pd.read_csv(r'C:\Users\pc\OneDrive\Escritorio\data_sim_company\temp\sim-companies-income-statement.csv')

    # Normalizar Columna de Fechas
    df_bal_sheet['Timestamp'] = pd.to_datetime(df_bal_sheet['Timestamp']).dt.strftime('%Y-%m-%d %H:%M:%S')
    df_acc_hist['Timestamp'] = pd.to_datetime(df_acc_hist['Timestamp']).dt.strftime('%Y-%m-%d %H:%M:%S')
    df_cash_stat['Timestamp'] = pd.to_datetime(df_cash_stat['Timestamp']).dt.strftime('%Y-%m-%d %H:%M:%S')
    df_inco_stat['Timestamp'] = pd.to_datetime(df_inco_stat['Timestamp']).dt.strftime('%Y-%m-%d %H:%M:%S')

    # Unificar los archivos CSV nuevos con los viejos
    df_acc_hist = pd.concat([df_acc_hist_0, df_acc_hist], ignore_index=True).drop_duplicates()
    df_bal_sheet = pd.concat([df_bal_sheet_0, df_bal_sheet], ignore_index=True).drop_duplicates()
    df_cash_stat = pd.concat([df_cash_stat_0, df_cash_stat], ignore_index=True).drop_duplicates()
    df_inco_stat = pd.concat([df_inco_stat_0, df_inco_stat], ignore_index=True).drop_duplicates()

    # Actualizar los archivos CSV con los nuevos datos
    df_acc_hist.to_csv(r'C:\Users\pc\OneDrive\Escritorio\data_sim_company\temp\sim-companies-account-history-Kalesshia.csv', index=False)
    df_bal_sheet.to_csv(r'C:\Users\pc\OneDrive\Escritorio\data_sim_company\temp\sim-companies-balance-sheet.csv', index=False)
    df_cash_stat.to_csv(r'C:\Users\pc\OneDrive\Escritorio\data_sim_company\temp\sim-companies-cashflow-statement.csv', index=False)
    df_inco_stat.to_csv(r'C:\Users\pc\OneDrive\Escritorio\data_sim_company\temp\sim-companies-income-statement.csv', index=False)

    # Eliminar un archivo específico
    os.remove(r'C:\Users\pc\OneDrive\Escritorio\data_sim_company\temp\sim-companies-account-history-Kalesshia_V0.csv')
    os.remove(r'C:\Users\pc\OneDrive\Escritorio\data_sim_company\temp\sim-companies-balance-sheet_V0.csv')
    os.remove(r'C:\Users\pc\OneDrive\Escritorio\data_sim_company\temp\sim-companies-cashflow-statement_V0.csv')
    os.remove(r'C:\Users\pc\OneDrive\Escritorio\data_sim_company\temp\sim-companies-income-statement_V0.csv')

    # Renombrar un archivo específico
    os.rename(r'C:\Users\pc\OneDrive\Escritorio\data_sim_company\temp\sim-companies-account-history-Kalesshia.csv', r'C:\Users\pc\OneDrive\Escritorio\data_sim_company\temp\sim-companies-account-history-Kalesshia_V0.csv')
    os.rename(r'C:\Users\pc\OneDrive\Escritorio\data_sim_company\temp\sim-companies-balance-sheet.csv', r'C:\Users\pc\OneDrive\Escritorio\data_sim_company\temp\sim-companies-balance-sheet_V0.csv')
    os.rename(r'C:\Users\pc\OneDrive\Escritorio\data_sim_company\temp\sim-companies-cashflow-statement.csv', r'C:\Users\pc\OneDrive\Escritorio\data_sim_company\temp\sim-companies-cashflow-statement_V0.csv')
    os.rename(r'C:\Users\pc\OneDrive\Escritorio\data_sim_company\temp\sim-companies-income-statement.csv', r'C:\Users\pc\OneDrive\Escritorio\data_sim_company\temp\sim-companies-income-statement_V0.csv')