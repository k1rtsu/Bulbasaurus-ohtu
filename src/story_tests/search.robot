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

Searching a reference with long search term
    Go To  ${HOME_URL}
    Input Text  search-title  titletitletitletitletitletitletitletitletitletitle
    Input Text  search-author  author
    ${computed_style}=  Execute JavaScript  return window.getComputedStyle(document.getElementById('search-title')).getPropertyValue('text-overflow')
    Should Contain  ${computed_style}  ellipsis

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


