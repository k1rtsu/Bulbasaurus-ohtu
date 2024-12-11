*** Settings ***
Resource  resource.robot
Suite Setup      Open And Configure Browser
Suite Teardown   Close Browser
Test Setup       Reset References


*** Test Cases ***
Searching a reference with valid information
    Add A Book With Test Values
    Add An Article With Test Values
    Page Should Contain  book author
    Page Should Contain  article author
    Input Text  search-author  book author
    Input Text  search-title  book title
    Input Text  search-year  2024
    Input Text  search-year_from  2020
    Input Text  search-year_to  2026
    Select From List By Value  id=search-references-by-type-selector  books
    Click Button  search
    Title Should Be  App
    Page Should Contain  Total references: 1
    Page Should Contain  book author
    Page Should Not Contain  article author

Searching a reference with valid author
    Add A Book With Test Values
    Add An Article With Test Values
    Page Should Contain  book author
    Page Should Contain  article author
    Input Text  search-author  book author
    Click Button  search
    Title Should Be  App
    Page Should Contain  Total references: 1
    Page Should Contain  book author
    Page Should Not Contain  article author

Searching a reference with valid author with regex $ symbol
    Add A Book With Test Values
    Add An Article With Test Values
    Page Should Contain  book title
    Page Should Contain  title article
    Input Text  search-title  title$
    Click Button  search
    Title Should Be  App
    Page Should Contain  Total references: 1
    Page Should Contain  book title
    Page Should Not Contain  title article

Searching a reference with valid title with regex .. symbol
    Add A Book With Test Values
    Add An Article With Test Values
    Page Should Contain  book title
    Page Should Contain  title article
    Input Text  search-title  a..icle
    Click Button  search
    Title Should Be  App
    Page Should Contain  Total references: 1
    Page Should Contain  title article
    Page Should Not Contain  book title

Searching a reference with valid title with regex ^ symbol
    Add A Book With Test Values
    Add An Article With Test Values
    Page Should Contain  book title
    Page Should Contain  title article
    Input Text  search-title  ^title
    Click Button  search
    Title Should Be  App
    Page Should Contain  Total references: 1
    Page Should Contain  title article
    Page Should Not Contain  book title

Searching a reference with valid title with regex * symbol
    Add A Book With Test Values
    Add An Article With Test Values
    Page Should Contain  book title
    Page Should Contain  title article
    Input Text  search-title  b*k
    Click Button  search
    Title Should Be  App
    Page Should Contain  Total references: 1
    Page Should Contain  book title
    Page Should Not Contain  title article

Searching a reference with valid title with AND operation
    Add A Book With Test Values
    Add An Article With Test Values
    Add Misc With Test Values
    Page Should Contain  book title
    Page Should Contain  title article
    Page Should Contain  misc title
    Input Text  search-title  book AND title
    Click Button  search
    Title Should Be  App
    Page Should Contain  Total references: 1
    Page Should Contain  book title
    Page Should Not Contain  title article
    Page Should Not Contain  misc title

Searching a reference with valid title with OR operation
    Add A Book With Test Values
    Add An Article With Test Values
    Add Misc With Test Values
    Page Should Contain  book title
    Page Should Contain  title article
    Page Should Contain  misc title
    Input Text  search-title  book OR misc
    Click Button  search
    Title Should Be  App
    Page Should Contain  Total references: 2
    Page Should Contain  book title
    Page Should Contain  misc title
    Page Should Not Contain  title article

Searching a reference with valid title with AND and OR operations
    Add A Book With Test Values
    Add An Article With Test Values
    Add Misc With Test Values
    Page Should Contain  book title
    Page Should Contain  title article
    Page Should Contain  misc title
    Input Text  search-title  (misc OR book) AND title
    Click Button  search
    Title Should Be  App
    Page Should Contain  Total references: 2
    Page Should Contain  book title
    Page Should Contain  misc title
    Page Should Not Contain  title article

Searching a reference without search terms
    Add A Book With Test Values
    Add An Article With Test Values
    Page Should Contain  book author
    Page Should Contain  article author
    Click Button  search
    Title Should Be  App
    Page Should Contain  Enter at least one search term
    Page Should Contain  book author
    Page Should Contain  article author

Searching a reference with invalid year range
    Add A Book With Test Values
    Add An Article With Test Values
    Page Should Contain  book author
    Page Should Contain  article author
    Input Text  search-year_from  2000
    Click Button  search
    Title Should Be  App
    Page Should Contain  Please enter the whole year range.


*** Keywords ***
Add A Book With Test Values
    Go To  ${HOME_URL}
    Title Should Be  App
    Select Book From The Dropdown Menu
    Input Text  author  book author
    Input Text  title  book title
    Input Text  year  2024
    Input Text  publisher  test publisher
    Click Button  Add a book
    Title Should Be  App

Add An Article With Test Values
    Go To  ${HOME_URL}
    Title Should Be  App
    Select Article From The Dropdown Menu
    Input Text  article-author  article author
    Input Text  article-title  title article
    Input Text  article-journal  test journal
    Input Text  article-volume  3
    Input Text  article-year  2024
    Click Button  Add an article
    Title Should Be  App

Add An Inproceeding With Test Values
    Go To  ${HOME_URL}
    Title Should Be  App
    Select Inproceedings From The Dropdown Menu
    Input Text  inproceedings-author  inproceeding author
    Input Text  inproceedings-title  inproceeding title
    Input Text  inproceedings-year  2024
    Input Text   inproceedings-booktitle  test booktitle
    Click Button  Add inproceedings
    Title Should Be  App

Add Misc With Test Values
    Go To  ${HOME_URL}
    Title Should Be  App
    Select Misc From The Dropdown Menu
    Input Text  misc-author  misc author  
    Input Text  misc-title  misc title
    Input Text  misc-year  2003
    Input Text  misc-note  This is a test misc note.
    Click Button  Add a misc reference
    Title Should Be  App
