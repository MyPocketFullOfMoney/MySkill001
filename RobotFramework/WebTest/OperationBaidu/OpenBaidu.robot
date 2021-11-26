*** Settings ***
Library           Selenium2Library

*** Test Cases ***
Open
    Open Browser    https://www.baidu.com    Firefox
    Sleep    5s
    log    tuichu
    Close Browser
    ${a}    Set variable    1
    log    ${a}
