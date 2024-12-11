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
    Input Text  article-title  article title
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

