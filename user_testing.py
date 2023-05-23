from functions import LoginActionTesting, SignupTesting

BASE_URL = "https://python-test-dev-ezzat.azurewebsites.net"  # "http://localhost" #


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

    path = f"{BASE_URL}/sign-up"

    # Testing Good account
    assert SignupTesting(path).apply_signup(
        msg=succes_msg,
        email="1111110@hello.com",
        firstname="Mahrous",
        lastname="Nour",
        pass1="1234567",
        pass2="1234567",
        jobdes="I am a frontend developer",
        gender="Male",
        usertype="Freelancer")
    # Testing not typical passwords formatting
    assert SignupTesting(path).apply_signup(
        msg=fail_passmatch_msg,
        email="1111111@hello.com",
        firstname="Mahrous",
        lastname="Nour",
        pass1="123",
        pass2="1234567",
        jobdes="I am a frontend developer",
        gender="Male",
        usertype="Freelancer")
    # Testing Small Password formatting
    assert SignupTesting(path).apply_signup(
        msg=fail_pass_length_msg,
        email="1111112@hello.com",
        firstname="Mahrous",
        lastname="Nour",
        pass1="123",
        pass2="123",
        jobdes="I am a frontend developer",
        gender="Male",
        usertype="Freelancer")
    # Testing Small First name formatting
    assert SignupTesting(path).apply_signup(
        msg=fail_fistlength_msg,
        email="1111113@hello.com",
        firstname="M",
        lastname="Nour",
        pass1="123",
        pass2="123",
        jobdes="I am a frontend developer",
        gender="Male",
        usertype="Freelancer")
    # Testing Small Last name formatting
    assert SignupTesting(path).apply_signup(
        msg=fail_lastlength_msg,
        email="1111114@hello.com",
        firstname="Mahrous",
        lastname="N",
        pass1="1234567",
        pass2="1234567",
        jobdes="I am a frontend developer",
        gender="Male",
        usertype="Freelancer")

    # Testing good account
    assert SignupTesting(path).apply_signup(
        msg=succes_msg,
        email="1111115@hello.com",
        firstname="Ali",
        lastname="Mohsen",
        pass1="1234567",
        pass2="1234567",
        jobdes="I am a manger",
        gender="Male",
        usertype="Business Owner")

    # Testing good account
    assert SignupTesting(path).apply_signup(
        msg=succes_msg,
        email="1111116@hello.com",
        firstname="hanan",
        lastname="Abdelrahman",
        pass1="sdfghjk",
        pass2="sdfghjk",
        jobdes="I am a manger",
        gender="Female",
        usertype="Both")

    # Testing sign up with alread existing account
    assert SignupTesting(path).apply_signup(
        msg=fail_emailexist_msg,
        email="1111116@hello.com",
        firstname="hanan",
        lastname="Abdelrahman",
        pass1="sdfghjk",
        pass2="sdfghjk",
        jobdes="I am a manger",
        gender="Female",
        usertype="Both")
    # Testing Small job description formatting
    assert SignupTesting(path).apply_signup(msg=fail_jobdes_length_msg,
                                            email="1111117@hello.com",
                                            firstname="hanan",
                                            lastname="Abdelrahman",
                                            pass1="sdfghjk", pass2="sdfghjk",
                                            jobdes="I", gender="Female",
                                            usertype="Both")

    # Testing No gender providing
    assert SignupTesting(path).apply_signup(msg=fail_nogender_msg,
                                            email="1111118@hello.com",
                                            firstname="hanan",
                                            lastname="Abdelrahman",
                                            pass1="sdfghjk", pass2="sdfghjk",
                                            jobdes="I am a student",
                                            usertype="Both")

    # Testing No user type providing
    assert SignupTesting(path).apply_signup(msg=fail_nousertype_msg,
                                            email="1111119@hello.com",
                                            firstname="hanan",
                                            lastname="Abdelrahman",
                                            pass1="sdfghjk", pass2="sdfghjk",
                                            jobdes="I am a student",
                                            gender="Female")

    # Testing invalid usertype account
    assert SignupTesting(path).apply_signup(
        msg=fail_nousertype_msg,
        email="1111120@hello.com",
        firstname="hanan",
        lastname="Abdelrahman",
        pass1="sdfghjk",
        pass2="sdfghjk",
        jobdes="I am a manger",
        gender="Female",
        usertype="Ok")

    # Testing invalid gender account
    assert SignupTesting(path).apply_signup(
        msg=fail_nogender_msg,
        email="1111121@hello.com",
        firstname="hanan",
        lastname="Abdelrahman",
        pass1="sdfghjk",
        pass2="sdfghjk",
        jobdes="I am a manger",
        gender="prefer not to say",
        usertype="Freelancer")

    # Testing good account
    assert SignupTesting(path).apply_signup(
        msg=succes_msg,
        email="3456789@hello.com",
        firstname="Omar",
        lastname="ElSakka",
        pass1="sdfghjk",
        pass2="sdfghjk",
        jobdes="I am a manger",
        gender="Male",
        usertype="Both")


def initializing_parameters(email, password):
    LoginActionTesting(
        f"{BASE_URL}/login",
        email,
        password).do_change_profile_action(
        firstname="Omar",
        lastname="ElSakka",
        jobdes="I am Initializer",
        gender="Male",
        usertype="Freelancer")


def test_change_password():
    email = "owner1@example1.com"
    password = "password"
    success_msg = "Password Changed Successfully!\n×"
    page = "changepassword"
    button = "changepasssubmit"
    path = f"{BASE_URL}/login"

    assert LoginActionTesting(
        path, email, password).do_change_password_action(
        password, password, success_msg, page, button)
    assert LoginActionTesting(
        path,
        email,
        password).do_change_password_action(
        password,
        "1234",
        success_msg,
        page,
        button) == False
    assert LoginActionTesting(
        path,
        email,
        password).do_change_password_action(
        "1234",
        password,
        success_msg,
        page,
        button) == False


def test_change_profile():
    email = "owner1@example1.com"
    password = "password"
    initializing_parameters(email, password)
    path = f"{BASE_URL}/login"

    assert LoginActionTesting(
        path,
        email,
        password).do_change_profile_action(
        newemail="3456789@asljhflksdfjb.com",
        firstname="Ali",
        lastname="ElSakka2",
        jobdes="I am Engineer")

    assert LoginActionTesting(
        path,
        "3456789@asljhflksdfjb.com",
        password).do_change_profile_action(
        firstname="Omar",
        jobdes="I am C Programmer")

    assert LoginActionTesting(
        path,
        "3456789@asljhflksdfjb.com",
        password).do_change_profile_action(
        newemail=email,
        jobdes="I am Python Programmer")

    assert LoginActionTesting(path, email, password).do_change_profile_action(
        firstname="Mahmoud", jobdes="I am C Programmer", gender="Female")

    assert LoginActionTesting(path, email, password).do_change_profile_action(
        firstname="Ali", jobdes="I am python Programmer", gender="Haha") == False

    assert LoginActionTesting(
        path,
        email,
        password).do_change_profile_action(
        newemail="3456789@asljhflksdfjb.com",
        lastname="Omar",
        jobdes="I am a data analyst",
        gender="Male",
        usertype="BusinessOwner")

    assert LoginActionTesting(
        path,
        "3456789@asljhflksdfjb.com",
        password).do_change_profile_action(
        lastname="Medhat",
        jobdes="I am an Engineer",
        usertype="haha") == False

    assert LoginActionTesting(
        path,
        "3456789@asljhflksdfjb.com",
        password).do_change_profile_action(
        newemail=email,
        firstname="Omar",
        lastname="ElSakka",
        jobdes="I am C Programmer")


def test_log_out():
    email = "owner1@example1.com"
    password = "password"
    assert LoginActionTesting(
        f"{BASE_URL}/login",
        email,
        password).do_logout_action()
