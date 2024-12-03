*** Settings ***
Resource  resource.robot
Suite Setup      Open And Configure Browser
Suite Teardown   Close Browser
Test Setup       Reset References


*** Test Cases ***
Main Page Can Be Opened
    Go To  ${HOME_URL}
    Title Should Be  App
    Page Should Contain  References app

Select Book From The Dropdown Menu
    Go To  ${HOME_URL}
    Select Book From The Dropdown Menu
    Page Should Contain Button  add a book

Select Article From The Dropdown Menu
    Go To  ${HOME_URL}
    Select Article From The Dropdown Menu
    Page Should Contain Button  add an article

Select Inproceedings From The Dropdown Menu
    Go To  ${HOME_URL}
    Select Inproceedings From The Dropdown Menu
    Page Should Contain Button  add inproceedings

Select Misc From The Dropdown Menu
    Go To  ${HOME_URL}
    Select Misc From The Dropdown Menu
    Page Should Contain Button  add a misc

Main Page Contains References
    Go To  ${HOME_URL}
    Page Should Contain  Total references: 0
