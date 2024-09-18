*** Settings ***
Resource    ../resources/common.resource
Library    SeleniumLibrary
Library    ../resources/utils/process_data_file/csv_reader.py

*** Variables ***
${CSV_FILE_PATH}    ${CURDIR}/../data/csv/login.csv

*** Test Cases ***
Login Test
    ${login_data}    read_login_csv    ${CSV_FILE_PATH}
    FOR    ${user}    IN    @{login_data}
        Run Keyword And Continue On Failure    Test Login    ${user}
    END

*** Keywords ***
Test Login
    [Arguments]    ${user}
    Open Browser To Login Page
    
    Input Text    name=username    ${user}[username]
    Input Text    name=pass        ${user}[password]
    Click Element    xpath://div[@objname='jBtnLogin' and contains(@class, 'login-form-btn')]
    ${is_valid}    Convert To Boolean    ${user}[valid]
    Run Keyword If    ${is_valid}
    ...    Page Should Contain    Đăng nhập MISA AMIS
    ...    ELSE
    ...    Page Should Contain    Tên đăng nhập hoặc mật khẩu không đúng
    Close Browser