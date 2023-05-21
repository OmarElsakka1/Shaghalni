from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep      

class signup_testing():
    def __init__(self, Path):
        self.Path = Path
    def __put_email(self,driver, email):
        driver.find_element(By.ID, "email").send_keys(email)
    def __put_first_name(self,driver, firstname):
        driver.find_element(By.ID, "firstName").send_keys(firstname)
    def __put_last_name(self,driver, lastname):
        driver.find_element(By.ID, "lastName").send_keys(lastname)
    def __put_password(self,driver, password):
        driver.find_element(By.ID, "password1").send_keys(password)
    def __put_confirm_password(self,driver, confirmpassword):
        driver.find_element(By.ID, "password2").send_keys(confirmpassword)
    def __put_job_des(self,driver, about):
        driver.find_element(By.ID, "job_description").send_keys(about)
    def __put_gender(self,driver, gender):
        driver.find_element(By.ID, "gender").send_keys(gender)
    def __put_usertype(self,driver, usertype):
        driver.find_element(By.ID, "usertype").send_keys(usertype)
    def apply_signup(self,msg,email=None,firstname=None,lastname=None,pass1 = None,pass2 = None, jobdes = None, gender = None, usertype = None):
        options = Options()
        options.add_experimental_option("excludeSwitches",["enable-logging"])
        driver = webdriver.Chrome(options = options)
        driver.get(self.Path)

        if (email != None):
            self.__put_email(driver,email)
        if (firstname != None):
            self.__put_first_name(driver,firstname)
        if (lastname != None):
            self.__put_last_name(driver,lastname)
        if (pass1 != None):
            self.__put_password(driver,pass1)
        if (pass2 != None):
            self.__put_confirm_password(driver,pass2)
        if (jobdes != None):
            self.__put_job_des(driver,jobdes)
        if (gender != None):
            self.__put_gender(driver,gender)
        if (usertype != None):
            self.__put_usertype(driver,usertype)
        
        driver.find_element(By.ID, "signupsubmit").click()
        element = driver.find_element(By.XPATH, "/html/body")
        if msg in element.text:
            close_driver().do_quit(driver)
            return True
        else:
            return False



class login_action_testing():
    def __init__(self,Path, email, password):
        self.Path = Path
        self.driver = login_testing(self.Path).do_login(email, password)

    def __Make_sure_log_in(self):
        if self.driver.current_url == "http://localhost/browse-jobs":
            return True
        else:
            print("Failed to Login")
            return False
        
    def do_change_Password_action(self, oldpass, newpass, msg):
        if (self.__Make_sure_log_in()):
            return change_Password().do_change_password(self.driver, oldpass, newpass,msg)
        else:
            return False
        
    def do_change_Profile_action(self, newemail=None,firstname=None,lastname=None, jobdes = None, gender = None, usertype = None):
        if (self.__Make_sure_log_in()):
            return change_Profile().do_apply(self.driver, newemail,firstname,lastname, jobdes, gender, usertype)
        else:
            return False
    
    def do_logout_action(self):
        if (self.__Make_sure_log_in()):
            return logout_testing().do_logout(self.driver) #action
        else:
            return False
        

class change_Password():
    def __init__(self):
        pass
    def do_change_password(self,driver,oldpass,newpass, msg):
        try:
            driver.find_element(By.ID, "changepassword").click()
            driver.find_element(By.ID, "password").send_keys(oldpass)
            driver.find_element(By.ID, "password1").send_keys(newpass)
            driver.find_element(By.ID, "password2").send_keys(newpass)
            driver.find_element(By.ID, "changepasssubmit").click()
            element = driver.find_element(By.XPATH, "/html/body")
            #driver.quit()
            if msg in element.text: 
                close_driver().do_quit(driver)
                return True
            else:
                close_driver().do_quit(driver)
                return False 
        except:
            close_driver().do_quit(driver)
            return False


class login_testing():
    def __init__(self,Path):
        self.Path = Path  

    def do_login(self,email, password):
        options = Options()
        options.add_experimental_option("excludeSwitches",["enable-logging"])
        driver = webdriver.Chrome(options = options)
        driver.get(self.Path) 
        driver.find_element(By.ID, "email").send_keys(email)
        driver.find_element(By.ID, "password").send_keys(password)
        driver.find_element(By.ID, "submitlogin").click()
        return driver

class change_Profile():
    def __init__(self):
        pass
    def __access_page(self,driver):
        try:
            driver.find_element(By.ID, "changeprofile").click()
            return True
        except:
            return False
        
    def change_email(self,driver,newemail):
        try:
            driver.find_element(By.ID, "email").send_keys(newemail)
            return True
        except:
            return False
        
    def change_first_name(self,driver,firstname):
        try:
            driver.find_element(By.ID, "firstName").send_keys(firstname)
            return True
        except:
            return False
        
    def change_last_name(self,driver,lastname):
        try:
            driver.find_element(By.ID, "lastName").send_keys(lastname)
            return True
        except:
            return False 

    def change_job_des(self,driver,jobdes):
        try:
            driver.find_element(By.ID, "job_description").send_keys(jobdes)
            return True
        except:
            return False
        
    def change_gender(self,driver,gender):
        try:
            driver.find_element(By.ID, "gender").send_keys(gender)
            return True
        except:
            return False

    def change_user_type(self,driver,usertype):
        try:
            driver.find_element(By.ID, "usertype").send_keys(usertype)
            return True
        except:
            return False

    def do_apply(self,driver,newemail=None,firstname=None,lastname=None, jobdes = None, gender = None, usertype = None):
        if (self.__access_page(driver)):
            List_msgs = []
            if (newemail != None):
                self.change_email(driver,newemail)
                List_msgs.append("Email changed Successfully!\n×")
            if (firstname != None):
                self.change_first_name(driver,firstname)
                List_msgs.append("First name changed Successfully!\n×")
            if (lastname != None):
                self.change_last_name(driver,lastname)
                List_msgs.append("Last name changed Successfully!\n×")
            if (jobdes != None):
                self.change_job_des(driver,jobdes)
                List_msgs.append("Job Description updated Successfully!\n×")
            if (gender != None):
                self.change_gender(driver,gender)
                List_msgs.append("Gender updated Successfully!\n×")
            if (usertype != None):
                self.change_user_type(driver,usertype)
                List_msgs.append("User Type updated Successfully!\n×")

            try:
                driver.find_element(By.ID, "changeprofilesubmit").click()
                element = driver.find_element(By.XPATH, "/html/body")
                print(element)
                Is_all_changed = True
                for i in range(len(List_msgs)):
                    if (List_msgs[i] not in element.text): 
                        Is_all_changed = False

                close_driver().do_quit(driver)
                return Is_all_changed
            except:
                close_driver().do_quit(driver)
                return False
        else:
            return False

class logout_testing():
    def __init__(self):
        pass
    def do_logout(self,driver):
        driver.find_element(By.ID, "logout").click()
        if(driver.current_url == "http://localhost/login"):
            sleep(1)
            close_driver().do_quit(driver)
            return True
        else:
            return False
    
class close_driver():
    def __init__(self):
        pass
    def do_quit(self,driver):
        driver.quit()

    
