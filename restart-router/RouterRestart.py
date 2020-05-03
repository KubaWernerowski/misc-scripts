import platform 
import subprocess 
import os
from dotenv import load_dotenv
from time import sleep 
from selenium import webdriver
from selenium.webdriver.common.keys import Keys 


class WifiChecker(object):
    def __init__(self):
        load_dotenv()

        self.google_url = "8.8.8.8"
        self.router_url = "http://192.168.1.1/Main_Login.asp"
        self.username = os.getenv("USERNAME")
        self.password = os.getenv("PASSWORD")
        self.driver = webdriver.Firefox()


    # https://stackoverflow.com/questions/2953462/pinging-servers-in-python
    def ping(self, host):
        """
        Returns True if host (str) responds to a ping request.
        Remember that a host may not respond to a ping (ICMP) 
        request even if the host name is valid.
        """
        # Option for the number of packets as a function of param
        param = '-n' if platform.system().lower()=='windows' else '-c'

        # Building the command. Ex: "ping -c 1 google.com"
        command = ['ping', param, '1', host]

        return subprocess.call(command) == 0
    

    def login(self):
        """
        Logs into the router.
        """
        self.driver.get(self.router_url)

        username_field = self.driver.find_element_by_name("login_username")
        password_field = self.driver.find_element_by_name("login_passwd")

        username_field.send_keys(self.username)
        password_field.send_keys(self.password)
        password_field.send_keys(Keys.RETURN)


    def restart_router(self):
        """
        Restart the router iff wifi is down.
        """
        sleep(5)
        reboot = self.driver.find_element_by_xpath("//span[text()='Reboot']")
        reboot.click()

        alert = self.driver.switch_to_alert()
        alert.accept()
        
if __name__ == "__main__":
    wifi_checker = WifiChecker()
    wifi_checker.login()
    wifi_checker.restart_router()
