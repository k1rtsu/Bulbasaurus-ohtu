*** Settings ***
Resource  resource.robot
Suite Setup      Open And Configure Browser
Suite Teardown   Close Browser
Test Setup       Reset References


*** Test Cases ***

After inproceedings is added, it will appear in the list of references
    Go To  ${HOME_URL}
    Title Should Be  App
    Select Inproceedings From The Dropdown Menu
    Set Author  Test author
    Set Title  Test title
    Set Year  2024
    Set Book Title  Test book-tite
    Click Button  Add inproceedings
    Page Should Contain  Test author
    Page Should Contain  Test title
    Page Should Contain  2024
    Page Should Contain  Test book-tite

Trying to add inproceedings with no author and failing
    Go To  ${HOME_URL}
    Title Should Be  App
    Select Inproceedings From The Dropdown Menu
    Set Title  Test title
    Set Year  2024
    Set Book Title  Test book-tite
    Click Button  Add inproceedings
    Page Should Contain  Missing required fields

Trying to add inproceedings with invalid year and failing
    Go To  ${HOME_URL}
    Title Should Be  App
    Select Inproceedings From The Dropdown Menu
    Set Author  Test author
    Set Title  Test title
    Set Year  202
    Set Book Title  Test book-tite
    Click Button  Add inproceedings
    Page Should Contain  Year length must be 4


*** Keywords ***


Set Author
    [Arguments]  ${Author}
    Input Text  inproceedings-author  ${Author}

Set Title
    [Arguments]  ${Title}
    Input Text  inproceedings-title  ${Title}

Set Year
    [Arguments]  ${Year}
    Input Text  inproceedings-year  ${Year}

Set Book Title
    [Arguments]  ${Book-title}
    Input Text  inproceedings-booktitle  ${Book-title}
