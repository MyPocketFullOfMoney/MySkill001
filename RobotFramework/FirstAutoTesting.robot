*** Settings ***
Library           E:/Python/Lib/site-packages/Selenium2Library/

*** Test Cases ***
baidu
    Open Browser    https://www.baidu.com    Firefox
    Sleep    5s
    Maximize Browser Window
    Input Text    id=kw    自动化测试
    sleep    5s
    Close Browser

UseMyKeyword
    Open baidu    https://www.baidu.com

*** Keywords ***
Open baidu
    [Arguments]    ${url}
    Open Browser    ${url}    Firefox
    Sleep    5s
    Maximize Browser Window
    Sleep    5s
    Close Browser

UseerKeyword
