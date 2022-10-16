*** Settings ***
Library  SeleniumLibrary

*** Variables ***
${appURL}   http://deeksha-test-system:8080/
${browser}  Chrome
${username}   uiauto
${password}   admin123
${firstname}  Deeksha
${lastname}   Pai
${phone}      46678657

*** Test Cases ***
TestRegistration
     Open Browser  ${appURL}     ${browser}
     Click on Register link
     Enter Username
     Enter Password
     Enter Firstname
     Enter Family Name
     Enter Phone
     Click on Register
     Verify endpoint login after register
     [Teardown]    Close Browser

*** Keywords ***
Click on Register link
     Click Link    link=Register
     ${register-url}   Get Location
     Log To Console    ${register-url}
     Location Should Contain  register

Enter Username
     Input Text    id:username    ${username}

Enter Password
     Input Text    id:password    ${password}

Enter Firstname
     Input Text    id:firstname   ${firstname}

Enter Family Name
     Input Text    id:lastname    ${lastname}

Enter Phone
     Input Text    id:phone       ${phone}

Click on Register
     Click Button  xpath:/html/body/section/form/input[6]

Verify endpoint login after register
     ${login-url}   Get Location
     Location Should Contain    login
