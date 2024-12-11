*** Settings ***
Resource  resource.robot
Suite Setup      Open And Configure Browser
Suite Teardown   Close Browser
Test Setup       Reset References


*** Test Cases ***

After a book is added, it will appear in the list of references.
    Add A Book With Test Values
    Page Should Contain  Total references: 1
    Page Should Contain  book author
    Page Should Contain  book title
    Page Should Contain  2024
    Page Should Contain  test publisher

Trying to add book with no author and failing
    Go To  ${HOME_URL}
    Title Should Be  App
    Set Title  Test title
    Set Year  2024
    Set Publisher  Test publisher
    Click Button  Add a book
    Title Should Be  App
    Page Should Contain  None of the fields can be empty

Trying to add book with invalid year and failing
    Go To  ${HOME_URL}
    Title Should Be  App
    Set Author  Test Author
    Set Title  Test title
    Set Year  202
    Set Publisher  Test publisher
    Click Button  Add a book
    Title Should Be  App
    Page Should Contain  Year length must be 4

*** Keywords ***


Set Author
    [Arguments]  ${author}
    Input Text  book-author  ${Author}

Set Title
    [Arguments]  ${title}
    Input Text  book-title  ${title}

Set Year
    [Arguments]  ${year}
    Input Text  book-year  ${year}

Set Publisher
    [Arguments]  ${publisher}
    Input Text  book-publisher  ${publisher}
