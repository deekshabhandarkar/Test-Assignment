*** Settings ***
Library  SeleniumLibrary
Library  DependencyLibrary

*** Variables ***
${appURL}  http://deeksha-test-system:8080
${browser}     Chrome
${tablexpath}  xpath://table[@id="content"]
${username}  admin
${password}  admin1234
${firstname}  Deeksha
${lastname}  Pai
${phone}   46678657

*** Test Cases ***
LoginTest
     [Tags]   Smoke
     Open Browser  ${appURL}   ${browser}
     Maximize Browser Window
     Click Link    link=Log In
     Enter Username
     Enter Password
     Click on Login Button
     Verify endpoint user after login

ReviewUserInfoTest
    [Tags]   Regression
    Depends On Test    LoginTest
    Check username
    Check firstname
    Check lastname
    Check phone number
    Click Link    link=Log Out
    [Teardown]  Close Browser

*** Keywords ***
Enter Username
     Input Text    id:username    ${username}

Enter Password
     Input Text    id:password    ${password}

Click on Login Button
     Click Button  xpath:/html/body/section/form/input[3]

Verify endpoint user after login
     ${user-url}   Get Location
     Log To Console    ${user-url}
     Location Should Contain    user

Check username
    ${read-username}  Get Table Cell    ${tablexpath}    2    2
    Should Be Equal  ${read-username}   ${username}

Check firstname
    ${read-firstname}  Get Table Cell    ${tablexpath}    3    2
    Should Be Equal  ${read-firstname}   ${firstname}

Check lastname
    ${read-lastname}  Get Table Cell    ${tablexpath}    4    2
    Should Be Equal  ${read-lastname}   ${lastname}

Check phone number
    ${read-phone}  Get Table Cell    ${tablexpath}    5    2
    Should Be Equal  ${read-phone}   ${phone}
