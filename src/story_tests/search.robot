*** Settings ***
Resource  resource.robot
Suite Setup      Open And Configure Browser
Suite Teardown   Close Browser
Test Setup       Reset References


*** Test Cases ***
Searching a reference with valid information
    Add A Book With Test Values
    Add An Article With Test Values
    Page Should Contain  Test author
    Page Should Contain  First-name Last-name
    Input Text  search-author  Test author
    Input Text  search-title  testing title
    Input Text  search-year  2024
    Input Text  search-year_from  2020
    Input Text  search-year_to  2026
    Select From List By Value  id=search-references-by-type-selector  books
    Click Button  search
    Title Should Be  App
    Page Should Contain  Total references: 1
    Page Should Contain  Test author
    Page Should Not Contain  First-name Last-name

Searching a reference with valid author
    Add A Book With Test Values
    Add An Article With Test Values
    Page Should Contain  Test author
    Page Should Contain  First-name Last-name
    Input Text  search-author  Test author
    Click Button  search
    Title Should Be  App
    Page Should Contain  Total references: 1
    Page Should Contain  Test author
    Page Should Not Contain  First-name Last-name

Searching a reference with valid author with regex symbols
    Add A Book With Test Values
    Add An Article With Test Values
    Page Should Contain  Test author
    Page Should Contain  First-name Last-name
    Input Text  search-author  author$
    Click Button  search
    Title Should Be  App
    Page Should Contain  Total references: 1
    Page Should Contain  Test author
    Page Should Not Contain  First-name Last-name

Searching a reference without search terms
    Add A Book With Test Values
    Add An Article With Test Values
    Page Should Contain  Test author
    Page Should Contain  First-name Last-name
    Click Button  search
    Title Should Be  App
    Page Should Contain  Enter at least one search term
    Page Should Contain  Test author
    Page Should Contain  First-name Last-name

Searching a reference with invalid year range
    Add A Book With Test Values
    Add An Article With Test Values
    Page Should Contain  Test author
    Page Should Contain  First-name Last-name
    Input Text  search-year_from  2000
    Click Button  search
    Title Should Be  App
    Page Should Contain  Please enter the whole year range.


*** Keywords ***
Add A Book With Test Values
    Go To  ${HOME_URL}
    Title Should Be  App
    Select Book From The Dropdown Menu
    Input Text  author  Test author
    Input Text  title  testing title
    Input Text  year  2024
    Input Text  publisher  test publisher
    Click Button  Add a book
    Title Should Be  App

Add An Article With Test Values
    Go To  ${HOME_URL}
    Title Should Be  App
    Select Article From The Dropdown Menu
    Input Text  article-author  First-name Last-name
    Input Text  article-title  Test title
    Input Text  article-journal  Test journal
    Input Text  article-volume  3
    Input Text  article-year  2024
    Click Button  Add an article
    Title Should Be  App
