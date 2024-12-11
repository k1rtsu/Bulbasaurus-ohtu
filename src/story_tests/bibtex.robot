*** Settings ***
Resource  resource.robot
Suite Setup      Open And Configure Browser
Suite Teardown   Close Browser
Test Setup       Reset References


*** Test Cases ***

After a book is added, it can be exported to bibtex format.
    Add A Book With Test Values
    Click Button    id=raw_bibtex
    Page Should Contain  book author
    Page Should Contain  book title
    Page Should Contain  2024
    Page Should Contain  test publisher

After an article is added, it can be exported to bibtex format.
    Go To  ${HOME_URL}
    Title Should Be  App
    Select Article From The Dropdown Menu
    Set Author  First-name Last-name
    Set Title  Test title
    Set Journal  Test journal
    Set Volume  3
    Set Number  3
    Set Year  2024
    Set First Page  3
    Set Last Page  4
    Set Doi  testDoi
    Set Url  https://example.com
    Click Button  Add an article
    Title Should Be  App
    Click Button    id=raw_bibtex
    Page Should Contain  Total references: 1
    Page Should Contain  First-name Last-name
    Page Should Contain  Test title

After a misc is added, it can be exported to bibtex format.
    Add Misc With Test Values
    Click Button  Add a misc reference
    Click Button    id=raw_bibtex
    Page Should Contain  misc author
    Page Should Contain  misc title
    Page Should Contain  2003
    Page Should Contain  This is a test misc note.

After inproceedings is added, it can be exported to bibtex format.
    Add An Inproceeding With Test Values
    Click Button    id=raw_bibtex
    Page Should Contain  inproceeding author
    Page Should Contain  inproceeding title
    Page Should Contain  2024
    Page Should Contain  test booktitle


*** Keywords ***


Set Author
    [Arguments]  ${Author}
    Input Text  article-author  ${Author}

Set Title
    [Arguments]  ${Title}
    Input Text  article-title  ${Title}

Set Journal
    [Arguments]  ${Journal}
    Input Text  article-journal  ${Journal}

Set Volume
    [Arguments]  ${Volume}
    Input Text  article-volume  ${Volume}

Set Number
    [Arguments]  ${Number}
    Input Text  article-number  ${Number}

Set Year
    [Arguments]  ${Year}
    Input Text  article-year  ${Year}

Set First Page
    [Arguments]  ${Page}
    Input Text  article-pages_from  ${Page}

Set Last Page
    [Arguments]  ${Page}
    Input Text  article-pages_to  ${Page}

Set Doi
    [Arguments]  ${Doi}
    Input Text  article-doi  ${Doi}

Set Url
    [Arguments]  ${URL}
    Input Text  article-url  ${URL}
