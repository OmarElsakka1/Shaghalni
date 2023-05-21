
import pytest
from Functions import login_action_testing, signup_testing


def test_sign_up():
    succes_msg = "Account created Successfully!\n×"
    fail_passmatch_msg = "Passwords don't match!\n×"
    fail_pass_length_msg = "Password must be at least"
    #fail_emailformat_msg = "Email has Invalid format!\n×"
    fail_emailexist_msg = "Email already exists!\n×"
    fail_fistlength_msg = "First name must be at least"
    fail_lastlength_msg = "Last name must be at least"
    fail_jobdes_length_msg = "Job Description must be at least"
    fail_nogender_msg = "You have to choose a Gender!\n×"
    fail_nousertype_msg = "You have to choose a User Type!\n×"

    path = "http://localhost/sign-up"

    # Testing Good account
    assert signup_testing(path).apply_signup(msg= succes_msg,
                                                        email="1111110@hello.com",
                                                        firstname="Mahrous",
                                                        lastname="Nour",
                                                        pass1 = "1234567", pass2 = "1234567",
                                                        jobdes="I am a frontend developer",gender = "Male",
                                                        usertype="Freelancer") == True
    ## Testing not typical passwords formatting
    assert signup_testing(path).apply_signup(msg = fail_passmatch_msg,
                                                        email="1111111@hello.com",
                                                        firstname="Mahrous",
                                                        lastname="Nour",
                                                        pass1 = "123", pass2 = "1234567",
                                                        jobdes="I am a frontend developer",gender = "Male",
                                                        usertype="Freelancer") == True
    # Testing Small Password formatting
    assert signup_testing(path).apply_signup(msg = fail_pass_length_msg,
                                                        email="1111112@hello.com",
                                                        firstname="Mahrous",
                                                        lastname="Nour",
                                                        pass1 = "123", pass2 = "123",
                                                        jobdes="I am a frontend developer",gender = "Male",
                                                        usertype="Freelancer") == True
    # Testing Small First name formatting
    assert signup_testing(path).apply_signup(msg =fail_fistlength_msg,
                                                        email="1111113@hello.com",
                                                        firstname="M",
                                                        lastname="Nour",
                                                        pass1 = "123", pass2 = "123",
                                                        jobdes="I am a frontend developer",gender = "Male",
                                                        usertype="Freelancer") == True
    # Testing Small Last name formatting
    assert signup_testing(path).apply_signup(msg =fail_lastlength_msg,
                                                        email="1111114@hello.com",
                                                        firstname="Mahrous",
                                                        lastname="N",
                                                        pass1 = "1234567", pass2 = "1234567",
                                                        jobdes="I am a frontend developer",gender = "Male",
                                                        usertype="Freelancer") == True
    
    # Testing good account
    assert signup_testing(path).apply_signup(msg= succes_msg,
                                                        email="1111115@hello.com",
                                                        firstname="Ali",
                                                        lastname="Mohsen",
                                                        pass1 = "1234567", pass2 = "1234567",
                                                        jobdes="I am a manger",gender = "Male",
                                                        usertype="Business Owner") == True



    # Testing good account
    assert signup_testing(path).apply_signup(msg = succes_msg,
                                                        email="1111116@hello.com",
                                                        firstname="hanan",
                                                        lastname="Abdelrahman",
                                                        pass1 = "sdfghjk", pass2 = "sdfghjk",
                                                        jobdes="I am a manger",gender = "Female",
                                                        usertype="Both") == True
    
    # Testing sign up with alread existing account
    assert signup_testing(path).apply_signup(msg = fail_emailexist_msg,
                                                        email="1111116@hello.com",
                                                        firstname="hanan",
                                                        lastname="Abdelrahman",
                                                        pass1 = "sdfghjk", pass2 = "sdfghjk",
                                                        jobdes="I am a manger",gender = "Female",
                                                        usertype="Both") == True
    # Testing Small job description formatting
    assert signup_testing(path).apply_signup(msg = fail_jobdes_length_msg,
                                                        email="1111117@hello.com",
                                                        firstname="hanan",
                                                        lastname="Abdelrahman",
                                                        pass1 = "sdfghjk", pass2 = "sdfghjk",
                                                        jobdes="I",gender = "Female",
                                                        usertype="Both") == True

    # Testing No gender providing
    assert signup_testing(path).apply_signup(msg = fail_nogender_msg,
                                                        email="1111118@hello.com",
                                                        firstname="hanan",
                                                        lastname="Abdelrahman",
                                                        pass1 = "sdfghjk", pass2 = "sdfghjk",
                                                        jobdes="I am a student",
                                                        usertype="Both") == True
    
    # Testing No user type providing
    assert signup_testing(path).apply_signup(msg = fail_nousertype_msg,
                                                        email="1111119@hello.com",
                                                        firstname="hanan",
                                                        lastname="Abdelrahman",
                                                        pass1 = "sdfghjk", pass2 = "sdfghjk",
                                                        jobdes="I am a student",
                                                        gender="Female") == True
  
    # Testing invalid usertype account
    assert signup_testing(path).apply_signup(msg = fail_nousertype_msg,
                                                        email="1111120@hello.com",
                                                        firstname="hanan",
                                                        lastname="Abdelrahman",
                                                        pass1 = "sdfghjk", pass2 = "sdfghjk",
                                                        jobdes="I am a manger",gender = "Female",
                                                        usertype="Ok") == True
    
    # Testing invalid gender account
    assert signup_testing(path).apply_signup(msg = fail_nogender_msg,
                                                        email="1111121@hello.com",
                                                        firstname="hanan",
                                                        lastname="Abdelrahman",
                                                        pass1 = "sdfghjk", pass2 = "sdfghjk",
                                                        jobdes="I am a manger",gender = "prefer not to say",
                                                        usertype="Freelancer") == True
    
    # Testing good account
    assert signup_testing(path).apply_signup(msg = succes_msg,
                                                        email="3456789@hello.com",
                                                        firstname="Omar",
                                                        lastname="ElSakka",
                                                        pass1 = "sdfghjk", pass2 = "sdfghjk",
                                                        jobdes="I am a manger",gender = "Male",
                                                        usertype="Both") == True
 



def initializing_parameters(email, password):
    login_action_testing("http://localhost/login",
            email, password).do_change_Profile_action(firstname= "Omar",
                                                      lastname= "ElSakka",
                                                      jobdes= "I am Initializer",
                                                      gender= "Male",
                                                      usertype="Freelancer")

def test_change_password():
    email = "3456789@hello.com"
    password = "sdfghjk"
    success_msg = "Password Changed Successfully!\n×"
    page = "changepassword"
    button = "changepasssubmit"
    path = "http://localhost/login"

    assert login_action_testing(path,
                                     email, password).do_change_Password_action("sdfghjk","sdfghjk",success_msg,page, button) == True
    assert login_action_testing(path,
                                     email, password).do_change_Password_action("sdfghjk","1234",success_msg) == False
    assert login_action_testing(path,
                                     email, password).do_change_Password_action("1234","sdfghjk",success_msg) == False



def test_change_profile():
    email = "3456789@hello.com"
    password = "sdfghjk"
    initializing_parameters(email, password)
    path = "http://localhost/login"

    assert login_action_testing(path,
            email, password).do_change_Profile_action(newemail ="3456789@asljhflksdfjb.com",
                                                      firstname= "Ali",
                                                      lastname= "ElSakka2",
                                                      jobdes= "I am Engineer") == True
    
    assert login_action_testing(path,
            "3456789@asljhflksdfjb.com", password).do_change_Profile_action(firstname= "Omar",
                                                      jobdes= "I am C Programmer") == True
    
    assert login_action_testing(path,
            "3456789@asljhflksdfjb.com", password).do_change_Profile_action(newemail =email,
                                                      jobdes= "I am Python Programmer") == True
        
    assert login_action_testing(path,
            email, password).do_change_Profile_action(firstname= "Mahmoud",
                                                      jobdes= "I am C Programmer",
                                                      gender = "Female") == True
    
    assert login_action_testing(path,
            email, password).do_change_Profile_action(firstname= "Ali",
                                                      jobdes= "I am python Programmer",
                                                      gender = "Haha") == False
    
    assert login_action_testing(path,
            email, password).do_change_Profile_action(newemail="3456789@asljhflksdfjb.com",
                                                      lastname= "Omar",
                                                      jobdes= "I am a data analyst",
                                                      gender= "Male",
                                                      usertype= "BusinessOwner") == True
    
    assert login_action_testing(path,
            "3456789@asljhflksdfjb.com", password).do_change_Profile_action(lastname= "Medhat",
                                                      jobdes= "I am an Engineer",
                                                      usertype= "haha") == False
    
    assert login_action_testing(path,
            "3456789@asljhflksdfjb.com", password).do_change_Profile_action(newemail =email,
                                                      firstname= "Omar",
                                                      lastname= "ElSakka",
                                                      jobdes= "I am C Programmer") == True




def test_log_out():
    email = "3456789@hello.com"
    password = "sdfghjk"
    assert login_action_testing("http://localhost/login",email, password).do_logout_action()




    