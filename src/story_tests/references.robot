*** Settings ***
Resource  resource.robot
Suite Setup      Open And Configure Browser
Suite Teardown   Close Browser
Test Setup       Reset References


*** Test Cases ***
At Start There Are No References
    Go To  ${HOME_URL}/references
    Title Should Be  References
    Page Should Contain  Total references: 0
    Page Should Not Contain  Articles:
    Page Should Not Contain  Books:

After adding a book, there is one reference
    Go To  ${HOME_URL}/new_book_reference
    Title Should Be  Create a new book reference
    Input Text  author  Testi
    Input Text  title  testing
    Input Text  year  2024
    Input Text  publisher  test
    Click Button  Add a book
    Title Should Be  References
    Page Should Contain  Total references: 1
    Page Should Contain  Books:
    Page Should Not Contain  Articles:


After adding an article, there is one reference
    Go To  ${HOME_URL}/new_article_reference
    Title Should Be  Create a new article reference
    Input Text  author  Testi
    Input Text  title  testing
    Input Text  year  2024
    Input Text  journal  test
    Input Text  volume  3
    Click Button  Add an article
    Title Should Be  References
    Page Should Contain  Total references: 1
    Page Should Contain  Articles:

After adding an article and a book, there is two references
    Go To  ${HOME_URL}/new_article_reference
    Title Should Be  Create a new article reference
    Input Text  author  Testi
    Input Text  title  testing
    Input Text  year  2024
    Input Text  journal  test
    Input Text  volume  3
    Click Button  Add an article
    Title Should Be  References
    Go To  ${HOME_URL}/new_book_reference
    Title Should Be  Create a new book reference
    Input Text  author  Testi
    Input Text  title  testing
    Input Text  year  2024
    Input Text  publisher  test
    Click Button  Add a book
    Title Should Be  References
    Page Should Contain  Total references: 2
    Page Should Contain  Books:
    Page Should Contain  Articles:

Trying to add book with no author and failing
    Go To  ${HOME_URL}/new_book_reference
    Title Should Be  Create a new book reference
    Input Text  title  testing
    Input Text  year  2024
    Input Text  publisher  test
    Click Button  Add a book
    Title Should Be  Create a new book reference
    Page Should Contain  None of the fields can be empty

Trying to add book with invalid year and failing
    Go To  ${HOME_URL}/new_book_reference
    Title Should Be  Create a new book reference
    Input Text  author  Testi
    Input Text  title  testing
    Input Text  year  20
    Input Text  publisher  test
    Click Button  Add a book
    Title Should Be  Create a new book reference
    Page Should Contain  Year length must be 4

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