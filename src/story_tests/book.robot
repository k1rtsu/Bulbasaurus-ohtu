*** Settings ***
Resource  resource.robot
Suite Setup      Open And Configure Browser
Suite Teardown   Close Browser
Test Setup       Reset References


*** Test Cases ***

After a book is added, it will appear in the list of references.
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
    Page Should Contain  Testi

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
