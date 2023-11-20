*** Settings ***
Resource  resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Go To Register Page

*** Test Cases ***
Register With Valid Username And Password
    Set Username  yuusuf
    Set Password  yuusuf1234
    Set Password Confirmation  yuusuf1234
    Submit Credentials
    Register Should Succeed     



Register With Too Short Username And Valid Password
    Set Username  y
    Set Password  yuusuf123
    Set Password confirmation  yuusuf123
    Submit Credentials
    Page Should Contain  Username shorter than 3


Register With Valid Username And Invalid Password
    Set Username  yusuboyy
    Set Password  yusuboyyy
    Set Password confirmation  yusuboyyy
    Submit Credentials
    Page Should Contain  Password cannot consists only of letters


Register With Nonmatching Password And Password Confirmation
    Set Username  yusufboy
    Set Password  yuboss123
    Set Password confirmation  yusuboss1234
    Submit Credentials
    Page Should Contain  Password and password confirmation do not match


Login After Successful Registration
    Go To Login Page
    Set Username  yuusuf
    Set Password  yuusuf1234
    Submit Login
    Page Should Contain  Ohtu Application main page


Login After Failed Registration
    Go To Login Page
    Set Username  yuusuf1234
    Set Password  yuusuf123
    Submit Login
    Page Should Contain  Invalid username or password





*** Keywords ***
Register Should Succeed
    start Page Should Be Open
Login Should Succeed
    Main Page Should Be Open

Set Username
    [Arguments]  ${username}
    Input Text  username  ${username}

Set Password
    [Arguments]  ${password}
    Input Password  password  ${password}

Set Password confirmation
    [Arguments]  ${password confirmation}
    Input Password  password_confirmation  ${password confirmation}


Submit Credentials
    Click Button  Register

Submit Login
    Click Button  Login

