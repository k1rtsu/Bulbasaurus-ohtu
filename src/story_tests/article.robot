*** Settings ***
Resource  resource.robot
Suite Setup      Open And Configure Browser
Suite Teardown   Close Browser
Test Setup       Reset References


*** Test Cases ***

After an article is added, it will appear in the list of references.
    Go To  ${HOME_URL}/new_article_reference
    Title Should Be  Create a new article reference
    Input Text  author  Testi
    Input Text  title  testing
    Input Text  year  2024
    Input Text  journal  test
    Input Text  volume  3
    Input Text  number  3
    Input Text  pages_from  3
    Input Text  pages_to  3
    Input Text  doi  testDoi
    Input Text  url  https://example.com
    Click Button  Add an article
    Title Should Be  References
    Page Should Contain  Articles:
    Page Should Contain  Testi

Trying to add article with no author and failing
    Go To  ${HOME_URL}/new_article_reference
    Title Should Be  Create a new article reference
    Input Text  title  testing
    Input Text  year  2024
    Input Text  journal  test
    Input Text  volume  3
    Click Button  Add an article
    Title Should Be  Create a new article reference
    Page Should Contain  Missing required fields: author

Trying to add article with invalid pages input
    Go To  ${HOME_URL}/new_article_reference
    Title Should Be  Create a new article reference
    Input Text  author  Test
    Input Text  title  testing
    Input Text  year  2024
    Input Text  journal  test
    Input Text  volume  3
    Input Text  pages_from  3
    Input Text  pages_to  2
    Click Button  Add an article
    Title Should Be  Create a new article reference
    Page Should Contain  The starting page number cannot be greater than the ending page number.

Trying to add article with invalid year input
    Go To  ${HOME_URL}/new_article_reference
    Title Should Be  Create a new article reference
    Input Text  author  Test
    Input Text  title  testing
    Input Text  year  aaaa
    Input Text  journal  test
    Input Text  volume  3
    Input Text  pages_from  2
    Input Text  pages_to  3
    Click Button  Add an article
    Title Should Be  Create a new article reference
    Page Should Contain  Year can only consist of numbers

Trying to add article with invalid url input
    Go To  ${HOME_URL}/new_article_reference
    Title Should Be  Create a new article reference
    Input Text  author  Test
    Input Text  title  testing
    Input Text  year  2001
    Input Text  journal  test
    Input Text  volume  3
    Input Text  url  ww.test.fi
    Click Button  Add an article
    Title Should Be  Create a new article reference
    Page Should Contain  Please enter a valid URL