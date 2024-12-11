*** Settings ***
Resource  resource.robot
Suite Setup      Open And Configure Browser
Suite Teardown   Close Browser
Test Setup       Reset References


*** Test Cases ***
At Start There Are No References
    Go To  ${HOME_URL}
    Title Should Be  App
    Page Should Contain  Total references: 0

After adding a book, there is one reference
    Add A Book With Test Values
    Page Should Contain  Total references: 1
    Page Should Contain  book author
    Page Should Contain  book title

After adding an article and a book, there is two references
    Add An Article With Test Values
    Add A Book With Test Values
    Page Should Contain  Total references: 2
    Page Should Contain  book author
    Page Should Contain  article author

After adding an article, book, misc and inproceedings, there is four references
    Add An Article With Test Values
    Add An Inproceeding With Test Values
    Add A Book With Test Values
    Add Misc With Test Values
    Page Should Contain  Total references: 4
    Page Should Contain  book author
    Page Should Contain  article author
    Page Should Contain  misc author
    Page Should Contain  inproceeding author

Title is placed before author in references list
    Add A Book With Test Values
    ${book_title}=  Get Text  xpath=//div[contains(@class, 'reference-box book')]//strong
    ${book_author}=  Get Text  xpath=//div[contains(@class, 'reference-box book')]//em
    Log  Book Title: ${book_title}
    Log  Book Author: ${book_author}
    ${comparison_result}=  Evaluate  '${book_title}' > '${book_author}'
    Should Be True  ${comparison_result}

After deleting an article, it no longer appears in the references list
    Add An Article With Test Values
    Add A Book With Test Values
    Page Should Contain  Total references: 2
    Click Button    id=delete_article
    Page Should Contain  Total references: 1
    Page Should Contain  book author
    Page Should Not Contain  article author

After deleting book, misc and inproceeding they no longer appears in the references list
    Add An Article With Test Values
    Add A Book With Test Values
    Add An Inproceeding With Test Values
    Add Misc With Test Values
    Page Should Contain  Total references: 4
    Click Button    id=delete_book
    Page Should Contain  Total references: 3
    Click Button    id=delete_misc
    Page Should Contain  Total references: 2
    Click Button    id=delete_inproceedings
    Page Should Contain  Total references: 1
    Page Should Not Contain  book author
    Page Should Not Contain  misc author
    Page Should Not Contain  inproceeding author
    Page Should Contain  article author

Editing a reference with valid information
    Add A Book With Test Values
    Page Should Contain  Total references: 1
    Page Should Contain  2024
    Click Button  edit
    Title Should Be  App
    Input Text  edit-year  2002
    Click Button  Save Changes
    Title Should Be  App
    Page Should Contain  Total references: 1
    Page Should Contain  2002

Editing a reference with missing author field
    Add A Book With Test Values
    Page Should Contain  Total references: 1
    Page Should Contain  book author
    Click Button  edit
    Title Should Be  App
    Clear Element Text  edit-author
    Click Button  Save Changes
    Title Should Be  App
    Page Should Contain  None of the fields can be empty

Editing a reference with invalid year
    Add A Book With Test Values
    Page Should Contain  Total references: 1
    Page Should Contain  2024
    Click Button  edit
    Title Should Be  App
    Input Text  edit-year  20
    Click Button  Save Changes
    Title Should Be  App
    Page Should Contain  Year length must be 4


