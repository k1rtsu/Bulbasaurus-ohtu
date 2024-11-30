*** Settings ***
Resource  resource.robot
Suite Setup      Open And Configure Browser
Suite Teardown   Close Browser
Test Setup       Reset References


*** Test Cases ***

After an article is added, it will appear in the list of references.
    Go To  ${HOME_URL}
    Title Should Be  App
    Select From List By Value  id=new-reference-form-selector  new-article-form-container
    Wait Until Element Is Visible  id=new-article-form-container
    Input Text  id=author  Testi
    Input Text  id=title  testing
    Input Text  id=journal  test
    Input Text  id=volume  3
    Input Text  id=number  3
    Input Text  id=year  2024
    Input Text  id=pages_from  3
    Input Text  id=pages_to  3
    Input Text  id=doi  testDoi
    Input Text  id=url  https://example.com
    Click Button  Add an article
    Title Should Be  App
    Page Should Contain  Articles:
    Page Should Contain  Testi

Trying to add article with no author and failing
    Go To  ${HOME_URL}
    Title Should Be  App
    Select From List By Value  id=new-reference-form-selector  new-article-form-container
    Wait Until Element Is Visible  id=new-article-form-container
    Input Text  id=title  testing
    Input Text  id=year  2024
    Input Text  id=journal  test
    Input Text  id=volume  3
    Click Button  Add an article
    Title Should Be  App
    Page Should Contain  Missing required fields: author

Trying to add article with invalid pages input
    Go To  ${HOME_URL}
    Title Should Be  App
    Select From List By Value  id=new-reference-form-selector  new-article-form-container
    Wait Until Element Is Visible  id=new-article-form-container
    Input Text  id=author  Test
    Input Text  id=title  testing
    Input Text  id=year  2024
    Input Text  id=journal  test
    Input Text  id=volume  3
    Input Text  id=pages_from  3
    Input Text  id=pages_to  2
    Click Button  Add an article
    Title Should Be  App
    Page Should Contain  The starting page number cannot be greater than the ending page number.

Trying to add article with invalid year input
    Go To  ${HOME_URL}
    Title Should Be  App
    Select From List By Value  id=new-reference-form-selector  new-article-form-container
    Wait Until Element Is Visible  id=new-article-form-container
    Input Text  id=author  Test
    Input Text  id=title  testing
    Input Text  id=year  aaaa
    Input Text  id=journal  test
    Input Text  id=volume  3
    Input Text  id=pages_from  2
    Input Text  id=pages_to  3
    Click Button  Add an article
    Title Should Be  App
    Page Should Contain  Year can only consist of numbers

Trying to add article with invalid url input
    Go To  ${HOME_URL}
    Title Should Be  App
    Select From List By Value  id=new-reference-form-selector  new-article-form-container
    Wait Until Element Is Visible  id=new-article-form-container
    Input Text  id=author  Test
    Input Text  id=title  testing
    Input Text  id=year  2001
    Input Text  id=journal  test
    Input Text  id=volume  3
    Input Text  id=url  ww.test.fi
    Click Button  Add an article
    Title Should Be  App
    Page Should Contain  Please enter a valid URL