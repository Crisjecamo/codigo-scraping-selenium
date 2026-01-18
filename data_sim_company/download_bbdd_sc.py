import unittest
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from act_bbdd_sim_company import normalize_data_sc
import time

#Yesterday....
    
# Cargar los archivos CSV viejos
df_acc_hist_0 = pd.read_csv(r'C:\Users\pc\OneDrive\Escritorio\data_sim_company\temp\sim-companies-account-history-Kalesshia_V0.csv')
df_bal_sheet_0 = pd.read_csv(r'C:\Users\pc\OneDrive\Escritorio\data_sim_company\temp\sim-companies-balance-sheet_V0.csv')
df_cash_stat_0 = pd.read_csv(r'C:\Users\pc\OneDrive\Escritorio\data_sim_company\temp\sim-companies-cashflow-statement_V0.csv')
df_inco_stat_0 = pd.read_csv(r'C:\Users\pc\OneDrive\Escritorio\data_sim_company\temp\sim-companies-income-statement_V0.csv')


path_driver = "/usr/local/bin/chromedriver"
url = "https://www.simcompanies.com/es/signin/"

correo = 'correo@gmail.com'
contraseña = "contraseña"

# --- Configuración para Headless ---
chrome_options = Options()
chrome_options.add_experimental_option("prefs", {
    "download.default_directory" : r"C:\Users\pc\OneDrive\Escritorio\data_sim_company\temp",
    "download.prompt_for_download": False,
    "download.directory_upgrade": True,
    "safebrowsing.enabled": True,
    "profile.default_content_setting_values.automatic_downloads": 1
})
# chrome_options.add_argument("--headless")  # Ejecuta Chrome sin interfaz gráfica
# chrome_options.add_argument("--window-size=1920,1080")
chrome_options.add_argument("--no-sandbox") # Necesario en entornos Linux/Docker sin entorno gráfico
chrome_options.add_argument("--disable-dev-shm-usage") # Ayuda a evitar problemas de memoria en Docker/servidores
# Puedes añadir más argumentos si es necesario, por ejemplo, para simular un navegador real
chrome_options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36")
        

service = Service()
driver = webdriver.Chrome(service=service, options=chrome_options)

class usando_unittest(unittest.TestCase):

    def setUp(self):
        self.driver = driver

    def test_conexion_cookies(self):
        driver.get(url)
        print("Conexion Realizada con Exito")
        time.sleep(10)

        try:
            boton_aceptar_cookies = driver.find_element(By.XPATH, "//button[text()='Aceptar todas']")

            # Haz clic en el botón
            boton_aceptar_cookies.send_keys(Keys.ENTER)
            print("¡Cookies aceptadas!")

        except Exception as e:
            print(f"No se pudo aceptar las cookies o iniciar sesión: {e}")
        time.sleep(3)
    
    ####def login_session():
        print("Ingresando Credenciales")
        usuario = driver.find_element(By.NAME, "email")
        usuario.send_keys(correo)

        clave = driver.find_element(By.NAME, "password")
        clave.send_keys(contraseña)
        clave.send_keys(Keys.ENTER)

        print("Inicio de Seccion Exitosamente")

        time.sleep(10)
    
    #####def select_options():
        try:
            print("Seleccionando Negocio")
            negocio = driver.find_element(By.CSS_SELECTOR, ".test-headquarters.css-1ufxp2j")

            negocio.click()
            print("Ingreso al Negocio Correctamente")

        except Exception as e:
            print(f"No se pudo ingresar al Negocio Correctamente {e}")
        
        time.sleep(3)

    ##### Selecionar el apartado de contabilidad
        try:
            print('Selecionando la Sección de Contabilidad')
            contabilidad = driver.find_element(By.CSS_SELECTOR, ".svg-inline--fa.fa-file-invoice-dollar.css-27s1e2")  

            contabilidad.click()
            print("Ingreso a Contabilidad Correctamente")
        
        except Exception as e:
            print(f"No se pudo ingresar a Contabilidad Correctamente {e}")
        
        time.sleep(5)

    ####Descargar Archivos

        try:
            print('Descargando Archivo de Historico')
            download_history= driver.find_element(By.XPATH, '//a[@href="/es/csv/account-history/4692348/"]')
            
            driver.execute_script("arguments[0].click();", download_history)
            print('Archivo de Historico Descargado Correctamente')

        except Exception as e:
            print(f"No se Pudo Descargar el Historico Correctamente {e}")

        time.sleep(5)

        # driver.execute_script("window.open('');")
        # time.sleep(40)
        # driver.switch_to.window(driver.window_handles[1])
        # driver.get("https://www.simcompanies.com/es/headquarters/accounting")

        try:
            print('Descargando Archivo de Income')
            download_income= driver.find_element(By.XPATH, '//a[@href="/es/csv/income-statement/"]')
            
            driver.execute_script("arguments[0].click();", download_income)
            print('Archivo de Income Descargado Correctamente')

        except Exception as e:
            print(f"No se Pudo Descargar el Income Correctamente {e}")

        time.sleep(5)

        # driver.execute_script("window.open('');")
        # time.sleep(40)
        # driver.switch_to.window(driver.window_handles[2])
        # driver.get("https://www.simcompanies.com/es/headquarters/accounting")

        try:
            print('Descargando Archivo de Balance')
            download_balance= driver.find_element(By.XPATH, '//a[@href="/es/csv/balance-sheet/"]')
            
            driver.execute_script("arguments[0].click();", download_balance)
            print('Archivo de Balance Descargado Correctamente')

        except Exception as e:
            print(f"No se Pudo Descargar el Balance Correctamente {e}")

        time.sleep(5)

        # driver.execute_script("window.open('');")
        # time.sleep(40)
        # driver.switch_to.window(driver.window_handles[3])
        # driver.get("https://www.simcompanies.com/es/headquarters/accounting")

        try:
            print('Descargando Archivo de Cashflow')
            download_cashflow= driver.find_element(By.XPATH, '//a[@href="/es/csv/cashflow-statement/"]')
            
            driver.execute_script("arguments[0].click();", download_cashflow)
            print('Archivo de Cashflow Descargado Correctamente')

        except Exception as e:
            print(f"No se Pudo Descargar el Cashflow Correctamente {e}")
            
        time.sleep(5)

        #### Normalizar datos actualizar y borrar datos viejos

        try:

            print("Normalizar datos actualizar y borrar datos viejos")
            normalize_data_sc(
            df_acc_hist_0,
            df_bal_sheet_0,
            df_cash_stat_0,
            df_inco_stat_0,
            )
            print("datos actualizados y borrado correctamente")

        except Exception as e:
            print(f"No se Pudo Normalizar los datos, actualizar y borrar datos viejos Correctamente {e}")
    

    def tearDown(self):
        self.driver.close()
        print("Conexion Cerrada Correctamente")

if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)
