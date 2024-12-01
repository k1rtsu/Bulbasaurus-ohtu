*** Settings ***
Resource  resource.robot
Suite Setup      Open And Configure Browser
Suite Teardown   Close Browser
Test Setup       Reset References


*** Test Cases ***

After an article is added, it will appear in the list of references.
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
    Page Should Contain  Total references: 1
    Page Should Contain  First-name Last-name
    Page Should Contain  Test title

Trying to add article with no author and failing
    Go To  ${HOME_URL}
    Title Should Be  App
    Select Article From The Dropdown Menu
    Set Title  Test title
    Set Volume  3
    Set Year  2024
    Click Button  Add an article
    Title Should Be  App
    Page Should Contain  Missing required fields: author

Trying to add article with invalid pages input
    Go To  ${HOME_URL}
    Title Should Be  App
    Select Article From The Dropdown Menu
    Set Author  First-name Last-name
    Set Title  Test title
    Set Journal  Test journal
    Set Volume  3
    Set Year  2024
    Set First Page  4
    Set Last Page  3
    Click Button  Add an article
    Title Should Be  App
    Page Should Contain  The starting page number cannot be greater than the ending page number.

Trying to add article with invalid year input
    Go To  ${HOME_URL}
    Title Should Be  App
    Select Article From The Dropdown Menu
    Set Author  First-name Last-name
    Set Title  Test title
    Set Journal  Test journal
    Set Volume  3
    Set Year  aaaa
    Set First Page  3
    Set Last Page  4
    Click Button  Add an article
    Title Should Be  App
    Page Should Contain  Year can only consist of numbers

Trying to add article with invalid url input
    Go To  ${HOME_URL}
    Title Should Be  App
    Select Article From The Dropdown Menu
    Set Author  First-name Last-name
    Set Title  Test title
    Set Journal  Test journal
    Set Volume  3
    Set Year  2024
    Set Url  ww.test.fi
    Click Button  Add an article
    Title Should Be  App
    Page Should Contain  Please enter a valid URL


*** Keywords ***


Select Article From The Dropdown Menu
    Select From List By Value  id=new-reference-form-selector  new-article-form-container
    Wait Until Element Is Visible  id=new-article-form-container

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
