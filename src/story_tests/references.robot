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
    Page Should Not Contain  Articles:
    Page Should Not Contain  Books:

After adding a book, there is one reference
    Go To  ${HOME_URL}
    Title Should Be  App
    Select Book From The Dropdown Menu
    Input Text  author  Testi
    Input Text  title  testing
    Input Text  year  2024
    Input Text  publisher  test
    Click Button  Add a book
    Title Should Be  App
    Page Should Contain  Total references: 1
    Page Should Contain  Testi
    Page Should Contain  testing

After adding an article and a book, there is two references
    Go To  ${HOME_URL}
    Title Should Be  App
    Select Article From The Dropdown Menu
    Input Text  article-author  First-name Last-name
    Input Text  article-title  Test title
    Input Text  article-journal  Test journal
    Input Text  article-volume  3
    Input Text  article-year  2024
    Click Button  Add an article
    Title Should Be  App
    Select Book From The Dropdown Menu
    Input Text  author  Test author
    Input Text  title  testing title
    Input Text  year  2024
    Input Text  publisher  test publisher
    Click Button  Add a book
    Title Should Be  App
    Page Should Contain  Total references: 2
    Page Should Contain  First-name Last-name
    Page Should Contain  Test author

After adding an article and inproceedings, there is two references
    Go To  ${HOME_URL}
    Title Should Be  App
    Select Article From The Dropdown Menu
    Input Text  article-author  First-name Last-name
    Input Text  article-title  Test title
    Input Text  article-journal  Test journal
    Input Text  article-volume  3
    Input Text  article-year  2024
    Click Button  Add an article
    Title Should Be  App
    Select Inproceedings From The Dropdown Menu
    Input Text  inproceedings-author  Test author
    Input Text  inproceedings-title  testing title
    Input Text  inproceedings-year  2024
    Input Text   inproceedings-booktitle  test booktitle
    Click Button  Add inproceedings
    Title Should Be  App
    Page Should Contain  Total references: 2
    Page Should Contain  Test title
    Page Should Contain  Test author

After deleting an article, it no longer appears in the references list
    Go To  ${HOME_URL}
    Title Should Be  App
    Select Article From The Dropdown Menu
    Input Text  article-author  First-name Last-name
    Input Text  article-title  Test title
    Input Text  article-journal  Test journal
    Input Text  article-volume  3
    Input Text  article-year  2024
    Click Button  Add an article
    Title Should Be  App
    Select Book From The Dropdown Menu
    Input Text  author  Test author
    Input Text  title  testing title
    Input Text  year  2024
    Input Text  publisher  test publisher
    Click Button  Add a book
    Title Should Be  App
    Page Should Contain  Total references: 2
    Click Button    id=delete_article
    Page Should Contain  Total references: 1
    Page Should Contain  Test author
    Page Should Not Contain  Test title

After deleting a book, it no longer appears in the references list
    Go To  ${HOME_URL}
    Title Should Be  App
    Select Article From The Dropdown Menu
    Input Text  article-author  First-name Last-name
    Input Text  article-title  Test title
    Input Text  article-journal  Test journal
    Input Text  article-volume  3
    Input Text  article-year  2024
    Click Button  Add an article
    Title Should Be  App
    Select Book From The Dropdown Menu
    Input Text  author  Test author
    Input Text  title  testing title
    Input Text  year  2024
    Input Text  publisher  test publisher
    Click Button  Add a book
    Title Should Be  App
    Page Should Contain  Total references: 2
    Click Button    id=delete_book
    Page Should Contain  Total references: 1
    Page Should Not Contain  Test author
    Page Should Contain  Test title

After deleting inproceedings, it no longer appears in the references list
    Go To  ${HOME_URL}
    Title Should Be  App
    Select Inproceedings From The Dropdown Menu
    Input Text  inproceedings-author  Test author
    Input Text  inproceedings-title  testing title
    Input Text  inproceedings-year  2024
    Input Text   inproceedings-booktitle  test booktitle
    Click Button  Add inproceedings
    Title Should Be  App
    Select Book From The Dropdown Menu
    Input Text  author  Test author
    Input Text  title  testing title
    Input Text  year  2024
    Input Text  publisher  test publisher
    Click Button  Add a book
    Title Should Be  App
    Page Should Contain  Total references: 2
    Click Button    id=delete_inproceedings
    Page Should Contain  Total references: 1
    Page Should Contain  Test author
    Page Should Not Contain  Testi

Editing a reference with valid information
    Go To  ${HOME_URL}
    Title Should Be  App
    Select Book From The Dropdown Menu
    Input Text  author  Test author
    Input Text  title  testing title
    Input Text  year  2024
    Input Text  publisher  test publisher
    Click Button  Add a book
    Title Should Be  App
    Page Should Contain  Total references: 1
    Page Should Contain  2024
    Click Button  edit
    Title Should Be  Edit reference
    Input Text  year  2002
    Click Button  Save changes
    Title Should Be  App
    Page Should Contain  Total references: 1
    Page Should Contain  2002

Editing a reference with missing author field
    Go To  ${HOME_URL}
    Title Should Be  App
    Select Book From The Dropdown Menu
    Input Text  author  Test author
    Input Text  title  testing title
    Input Text  year  2024
    Input Text  publisher  test publisher
    Click Button  Add a book
    Title Should Be  App
    Page Should Contain  Total references: 1
    Page Should Contain  Test author
    Click Button  edit
    Title Should Be  Edit reference
    Clear Element Text  author
    Click Button  Save changes
    Title Should Be  Edit reference
    Page Should Contain  None of the fields can be empty

Editing a reference with invalid year
    Go To  ${HOME_URL}
    Title Should Be  App
    Select Book From The Dropdown Menu
    Input Text  author  Test author
    Input Text  title  testing title
    Input Text  year  2024
    Input Text  publisher  test publisher
    Click Button  Add a book
    Title Should Be  App
    Page Should Contain  Total references: 1
    Page Should Contain  2024
    Click Button  edit
    Title Should Be  Edit reference
    Input Text  year  20
    Click Button  Save changes
    Title Should Be  Edit reference
    Page Should Contain  Year length must be 4
