#### Device Magic - DM ####

# modules and libraries:
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import pandas as pd, time

# main class for Selenium and Device Magic:
class DeviceMagic():

    # class variable and exact location
    # of a gecko driver for a Firefox:
    wdpath = Service("\\gecko_driver_location_path\\")
    
    # constructor:
    def __init__(self, headless = False, kiosk = False):

        self.headless = headless
        self.kiosk = kiosk
        self.driver = None

    # setup method:
    def setup(self):

        options = webdriver.FirefoxOptions()
        if self.headless:
            options.add_argument("--headless")
        if self.kiosk:
            options.add_argument("--kiosk")
        self.driver = webdriver.Firefox(service=DeviceMagic.wdpath,
                                        options=options)
        return self
    
    # login method:
    def login(self, form_path, email, pswd):

        # main call:
        self.driver.get(form_path)

        # username:
        WebDriverWait(self.driver, 15).until(
            EC.presence_of_element_located((By.ID, "user_remember_me_1")))
        self.driver.find_element(By.ID, 'user_remember_me_1').click()
        mail = email
        mail_enter = self.driver.find_element(By.ID, 'user_email')
        mail_enter.send_keys(mail)
        WebDriverWait(self.driver, 15).until(
            EC.presence_of_element_located((By.NAME, "commit")))
        self.driver.find_element(By.NAME, 'commit').click()

        # password:
        WebDriverWait(self.driver, 15).until(
            EC.presence_of_element_located((By.ID, "user_password")))
        passw = pswd
        pswd_enter = self.driver.find_element(By.ID, 'user_password')
        pswd_enter.send_keys(passw)
        WebDriverWait(self.driver, 15).until(
            EC.presence_of_element_located((By.NAME, "commit")))
        self.driver.find_element(By.NAME, 'commit').click()
        return self
    
    # method for sleep:
    def sleep_time(self, seconds):

        time.sleep(seconds)
        return self
    
    # method to quit a browser:
    def close_browser(self):

        if self.driver:
            self.driver.quit()
        return self
    
    # method to remove destination:
    def rem_dest(self):

        # click on destination:
        try:
            WebDriverWait(self.driver, 15).until(
                EC.presence_of_element_located((By.CSS_SELECTOR,
                                                "span.fas.fa-cog")))
            self.driver.find_element(By.CSS_SELECTOR, 
                                    "span.fas.fa-cog").click()
            
            # remove destination:
            WebDriverWait(self.driver, 15).until(
                EC.presence_of_element_located((By.XPATH,
                '//a[@data-confirm="Are you sure?" \
                and @data-remote="true" and @rel="nofollow" \
                and @data-method="delete"]')))
            self.driver.find_element(By.XPATH,
            '//a[@data-confirm="Are you sure?" \
            and @data-remote="true" and @rel="nofollow"  \
            and @data-method="delete"]').click()
            
            # switch to pop up window with js
            # and press enter/return:
            alert = self.driver.switch_to.alert
            alert.accept()
        except:
            pass
            print("Destination not located, no need to be deleted!")
        return self
    
    # method to add destination:
    def add_destination(self):
            
            WebDriverWait(self.driver, 15).until(
                EC.presence_of_element_located((By.ID, "create_destination_link")))
            self.driver.find_element(By.ID, 'create_destination_link').click()
        
            WebDriverWait(self.driver, 15).until(
                EC.presence_of_element_located((By.ID, "sql_transport-list-item")))
            self.driver.find_element(By.ID, 'sql_transport-list-item').click()
            
            WebDriverWait(self.driver, 15).until(
                EC.presence_of_element_located((By.ID, "xml_format-list-item")))
            self.driver.find_element(By.ID, 'xml_format-list-item').click()
            
            WebDriverWait(self.driver, 15).until(
                EC.presence_of_element_located((By.ID, "destination_description")))
            dstn = self.driver.find_element(By.ID, 'destination_description')
            dstn.send_keys('xxx')
            dstn.send_keys(Keys.RETURN)
            
            WebDriverWait(self.driver, 15).until(
                EC.presence_of_element_located((By.ID, "sql_transport_host")))
            host = self.driver.find_element(By.ID, 'sql_transport_host')
            host.send_keys('xxx')
            host.send_keys(Keys.RETURN)
            
            WebDriverWait(self.driver, 15).until(
                EC.element_to_be_clickable((By.ID, "sql_transport_username")))
            usrnm = self.driver.find_element(By.ID, 'sql_transport_username')
            usrnm.send_keys('xxx')
            usrnm.send_keys(Keys.RETURN)
            
            WebDriverWait(self.driver, 15).until(
                EC.presence_of_element_located((By.ID, "sql_transport_password")))
            pswd1 = 'xxx'
            pswd_enter1 = self.driver.find_element(By.ID, 'sql_transport_password')
            pswd_enter1.send_keys(pswd1)
            
            WebDriverWait(self.driver, 15).until(
                EC.presence_of_element_located((By.ID, "sql_transport_port")))
            port = self.driver.find_element(By.ID, 'sql_transport_port')
            port.send_keys('xxx')
            port.send_keys(Keys.RETURN)
            
            #### Database name:
            WebDriverWait(self.driver, 15).until(
                EC.presence_of_element_located((By.ID, "sql_transport_database_name")))
            dbnm = self.driver.find_element(By.ID, 'sql_transport_database_name')
            dbnm.send_keys('xxx')
            dbnm.send_keys(Keys.RETURN)

            ##### SQL table:
            WebDriverWait(self.driver, 15).until(
                EC.element_to_be_clickable((By.ID, "fetch-table-names")))
            self.driver.find_element(By.ID, 'fetch-table-names').click()
            WebDriverWait(self.driver, 15).until(
                EC.element_to_be_clickable((By.XPATH, '//*[@id="sql_transport_table_name"]'))).click()
            select = Select(self.driver.find_element(By.XPATH, '//*[@id="sql_transport_table_name"]'))
            select.select_by_visible_text('multi_dm')

            ##### mapping:
            path0 = 'C:\\...'
            df0 = pd.read_csv(path0, header = None)    
            list0 = df0[0].to_list()
            dm_table_id_list = list0

            path1 = 'C:\\Users\\...'
            df1 = pd.read_csv(path1, header = None)    
            list1 = df1[0].to_list()
            sql_table_id_list = list1

            # main for loop:
            time.sleep(2)

            for x, y in zip (dm_table_id_list, sql_table_id_list):
                field_enter = self.driver.find_element(By.ID, y)
                field_enter.send_keys(x)

            self.driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
            WebDriverWait(self.driver, 15).until(
                EC.presence_of_element_located((By.ID, "create_new_destination_button")))
            self.driver.find_element(By.ID, 'create_new_destination_button').click()

            print('xxx')
            return self