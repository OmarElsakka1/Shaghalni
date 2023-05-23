from time import sleep  
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
    



class Adapter():
    def __init__(self,pathlogin,pathform):
        self.pathlogin = pathlogin
        self.pathform = pathform

    def do_login_add_admin(self, email = None, password = None, msg = None,newemail = None,firstname = None,
               lastname = None, pass1 = None, pass2 = None):
        driver = LoginTesting(self.pathlogin).do_login(email,password)
        driver.find_element(By.ID, "adminadd_admin").click()
        return SignupTesting(self.pathform, driver).apply_signup(msg = msg, email = newemail,firstname = firstname,
                                                   lastname= lastname,pass1 = pass1, pass2= pass2)

class SignupTesting():
    def __init__(self, path, driver = None):
        self.path = path
        if (driver == None):
            options = Options()
            options.add_experimental_option("excludeSwitches",["enable-logging"])
            driver = webdriver.Chrome(options = options)
            driver.get(self.path)
            self.driver = driver
        else:
            self.driver = driver
    def __put_email(self, email):
        self.driver.find_element(By.ID, "email").send_keys(email)
    def __put_first_name(self, firstname):
        self.driver.find_element(By.ID, "firstName").send_keys(firstname)
    def __put_last_name(self, lastname):
        self.driver.find_element(By.ID, "lastName").send_keys(lastname)
    def __put_password(self, password):
        self.driver.find_element(By.ID, "password1").send_keys(password)
    def __put_confirm_password(self, confirmpassword):
        self.driver.find_element(By.ID, "password2").send_keys(confirmpassword)
    def __put_job_des(self, job_des):
        self.driver.find_element(By.ID, "job_description").send_keys(job_des)
    def __put_gender(self, gender):
        self.driver.find_element(By.ID, "gender").send_keys(gender)
    def __put_usertype(self, usertype):
        self.driver.find_element(By.ID, "usertype").send_keys(usertype)
    def apply_signup(self,msg,email=None,firstname=None,lastname=None,pass1 = None,pass2 = None, jobdes = None, gender = None, usertype = None):
    
        if (email != None):
            self.__put_email(email)
        if (firstname != None):
            self.__put_first_name(firstname)
        if (lastname != None):
            self.__put_last_name(lastname)
        if (pass1 != None):
            self.__put_password(pass1)
        if (pass2 != None):
            self.__put_confirm_password(pass2)
        if (jobdes != None):
            self.__put_job_des(jobdes)
        if (gender != None):
            self.__put_gender(gender)
        if (usertype != None):
            self.__put_usertype(usertype)
        
        self.driver.find_element(By.ID, "submit").click()
        element = self.driver.find_element(By.XPATH, "/html/body")
        if msg in element.text:
            CloseDriver().do_quit(self.driver)
            return True
        else:
            return False


class LoginActionTesting():
    def __init__(self,path, email, password):
        self.path = path
        self.driver = LoginTesting(self.path).do_login(email, password)

    def __Make_sure_log_in(self):
        msg = "Logged in successfully!\n×"
        if (msg in self.driver.find_element(By.XPATH, "/html/body").text):
            return True
        else:
            print("Failed to Login")
            return False
        
    def do_change_password_action(self, oldpass, newpass, msg,page, button):
        if (self.__Make_sure_log_in()):
            return ChangePassword().do_change_password(self.driver, oldpass, newpass,msg,page, button)
        else:
            return False
        
    def do_change_profile_action(self, newemail=None,firstname=None,lastname=None, jobdes = None, gender = None, usertype = None):
        if (self.__Make_sure_log_in()):
            return ChangeProfile().do_apply(self.driver, newemail,firstname,lastname, jobdes, gender, usertype)
        else:
            return False
    
    def do_logout_action(self):
        if (self.__Make_sure_log_in()):
            return logout_testing().do_logout(self.driver) #action
        else:
            return False
        

class ChangePassword():
    def __init__(self):
        pass
    def do_change_password(self,driver,oldpass,newpass, msg,page, button):
        try:
            driver.find_element(By.ID, page).click()
            driver.find_element(By.ID, "password").send_keys(oldpass)
            driver.find_element(By.ID, "password1").send_keys(newpass)
            driver.find_element(By.ID, "password2").send_keys(newpass)
            driver.find_element(By.ID, button).click()
            element = driver.find_element(By.XPATH, "/html/body")
            #driver.quit()
            if msg in element.text: 
                CloseDriver().do_quit(driver)
                return True
            else:
                CloseDriver().do_quit(driver)
                return False 
        except:
            CloseDriver().do_quit(driver)
            return False


class LoginTesting():
    def __init__(self,path):
        self.path = path  

    def do_login(self,email, password):
        options = Options()
        options.add_experimental_option("excludeSwitches",["enable-logging"])
        driver = webdriver.Chrome(options = options)
        driver.get(self.path) 
        driver.find_element(By.ID, "email").send_keys(email)
        driver.find_element(By.ID, "password").send_keys(password)
        driver.find_element(By.ID, "submitlogin").click()
        return driver

class ChangeProfile():
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
            list_msgs = []
            if (newemail != None):
                self.change_email(driver,newemail)
                list_msgs.append("Email changed Successfully!\n×")
            if (firstname != None):
                self.change_first_name(driver,firstname)
                list_msgs.append("First name changed Successfully!\n×")
            if (lastname != None):
                self.change_last_name(driver,lastname)
                list_msgs.append("Last name changed Successfully!\n×")
            if (jobdes != None):
                self.change_job_des(driver,jobdes)
                list_msgs.append("Job Description updated Successfully!\n×")
            if (gender != None):
                self.change_gender(driver,gender)
                list_msgs.append("Gender updated Successfully!\n×")
            if (usertype != None):
                self.change_user_type(driver,usertype)
                list_msgs.append("User Type updated Successfully!\n×")

            try:
                driver.find_element(By.ID, "changeprofilesubmit").click()
                element = driver.find_element(By.XPATH, "/html/body")
                print(element)
                is_all_changed = True
                for i in range(len(list_msgs)):
                    if (list_msgs[i] not in element.text): 
                        is_all_changed = False

                CloseDriver().do_quit(driver)
                return is_all_changed
            except:
                CloseDriver().do_quit(driver)
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
            CloseDriver().do_quit(driver)
            return True
        else:
            return False
    
class CloseDriver():
    def __init__(self):
        pass
    def do_quit(self,driver):
        driver.quit()

    
