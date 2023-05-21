
import pytest
from Functions import login_action_testing

def initializing_parameters(email, password):
    login_action_testing("http://localhost/login",
            email, password).do_change_Profile_action(firstname= "Omar",
                                                      lastname= "ElSakka",
                                                      jobdes= "I am Initializer",
                                                      gender= "Male",
                                                      usertype="Freelancer")

def test_change_profile():
    email = "3456789@hello.com"
    password = "sdfghjk"
    initializing_parameters(email, password)
    assert login_action_testing("http://localhost/login",
            email, password).do_change_Profile_action(newemail ="3456789@asljhflksdfjb.com",
                                                      firstname= "Ali",
                                                      lastname= "ElSakka2",
                                                      jobdes= "I am Engineer") == True
    
    assert login_action_testing("http://localhost/login",
            "3456789@asljhflksdfjb.com", password).do_change_Profile_action(firstname= "Omar",
                                                      jobdes= "I am C Programmer") == True
    
    assert login_action_testing("http://localhost/login",
            "3456789@asljhflksdfjb.com", password).do_change_Profile_action(newemail =email,
                                                      jobdes= "I am Python Programmer") == True
        
    assert login_action_testing("http://localhost/login",
            email, password).do_change_Profile_action(firstname= "Mahmoud",
                                                      jobdes= "I am C Programmer",
                                                      gender = "Female") == True
    
    assert login_action_testing("http://localhost/login",
            email, password).do_change_Profile_action(firstname= "Ali",
                                                      jobdes= "I am python Programmer",
                                                      gender = "Haha") == False
    
    assert login_action_testing("http://localhost/login",
            email, password).do_change_Profile_action(newemail="3456789@asljhflksdfjb.com",
                                                      lastname= "Omar",
                                                      jobdes= "I am a data analyst",
                                                      gender= "Male",
                                                      usertype= "BusinessOwner") == True
    
    assert login_action_testing("http://localhost/login",
            "3456789@asljhflksdfjb.com", password).do_change_Profile_action(lastname= "Medhat",
                                                      jobdes= "I am an Engineer",
                                                      usertype= "haha") == False
    
    assert login_action_testing("http://localhost/login",
            "3456789@asljhflksdfjb.com", password).do_change_Profile_action(newemail =email,
                                                      firstname= "Omar",
                                                      lastname= "ElSakka",
                                                      jobdes= "I am C Programmer") == True

def test_change_password():
    email = "3456789@hello.com"
    password = "sdfghjk"
    success_msg = "Password Changed Successfully!"
    assert login_action_testing("http://localhost/login",
                                     email, password).do_change_Password_action("sdfghjk","sdfghjk",success_msg) == True
    assert login_action_testing("http://localhost/login",
                                     email, password).do_change_Password_action("sdfghjk","1234",success_msg) == False
    assert login_action_testing("http://localhost/login",
                                     email, password).do_change_Password_action("1234","sdfghjk",success_msg) == False

def test_log_out():
    email = "3456789@hello.com"
    password = "sdfghjk"
    assert login_action_testing("http://localhost/login",email, password).do_logout_action()
    