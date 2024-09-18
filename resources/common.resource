*** Settings ***
Library    Browser

*** Variables ***
${BASE_URL}    https://amisapp.misa.vn

*** Keywords ***
Open Browser To Login Page
    Open Browser    ${BASE_URL}/login    chrome
    Maximize Browser Window

Close Browser
    [Documentation]    Closes the browser
    Close All Browsers
