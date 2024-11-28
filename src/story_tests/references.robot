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
    Input Text  number  3
    Input Text  pages_from  3
    Input Text  pages_to  3
    Input Text  doi  testDoi
    Input Text  url  https://example.com
    Click Button  Add an article
    Title Should Be  References
    Page Should Contain  Total references: 1
    Page Should Contain  Articles:

After adding inproceedings, there is one reference
    Go To  ${HOME_URL}/new_inproceedings_reference
    Title Should Be  Create new inproceedings reference
    Input Text  author  Testi
    Input Text  title  testing
    Input Text  year  2024
    Input Text  booktitle  test
    Click Button  Add inproceedings
    Title Should Be  References
    Page Should Contain  Total references: 1
    Page Should Contain  Inproceedings:

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

After adding an article and inproceedings, there is two references
    Go To  ${HOME_URL}/new_article_reference
    Title Should Be  Create a new article reference
    Input Text  author  Testi
    Input Text  title  testing
    Input Text  year  2024
    Input Text  journal  test
    Input Text  volume  3
    Click Button  Add an article
    Title Should Be  References
    Go To  ${HOME_URL}/new_inproceedings_reference
    Title Should Be  Create new inproceedings reference
    Input Text  author  Testi
    Input Text  title  testing
    Input Text  year  2024
    Input Text  booktitle  test
    Click Button  Add inproceedings
    Title Should Be  References
    Page Should Contain  Total references: 2
    Page Should Contain  Articles:
    Page Should Contain  Inproceedings:

After deleting a book, it no longer appears in the references list
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
    Click Button    id=delete_book
    Page Should Contain  Total references: 1
    Page Should Not Contain  Books:
    Page Should Contain  Articles:

After deleting an article, it no longer appears in the references list
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
    Click Button    id=delete_article
    Page Should Contain  Total references: 1
    Page Should Contain  Books:
    Page Should Not Contain  Articles:

After deleting inproceedings, it no longer appears in the references list
    Go To  ${HOME_URL}/new_inproceedings_reference
    Title Should Be  Create new inproceedings reference
    Input Text  author  Testi
    Input Text  title  testing
    Input Text  year  2024
    Input Text  booktitle  test
    Click Button  Add inproceedings
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
    Click Button    id=delete_inproceedings
    Page Should Contain  Total references: 1
    Page Should Contain  Books:
    Page Should Not Contain  Inproceedings:

Editing a reference with valid information
    Go To  ${HOME_URL}/new_book_reference
    Title Should Be  Create a new book reference
    Input Text  author  Testi
    Input Text  title  testing
    Input Text  year  2024
    Input Text  publisher  test
    Click Button  Add a book
    Title Should Be  References
    Page Should Contain  Total references: 1
    Page Should Contain  2024
    Click Button  edit
    Title Should Be  Edit reference
    Input Text  year  2002
    Click Button  Save changes
    Title Should Be  References
    Page Should Contain  Total references: 1
    Page Should Contain  2002

Editing a reference with missing author field
    Go To  ${HOME_URL}/new_book_reference
    Title Should Be  Create a new book reference
    Input Text  author  Testi
    Input Text  title  testing
    Input Text  year  2024
    Input Text  publisher  test
    Click Button  Add a book
    Title Should Be  References
    Page Should Contain  Total references: 1
    Page Should Contain  Testi
    Click Button  edit
    Title Should Be  Edit reference
    Clear Element Text  author
    Click Button  Save changes
    Title Should Be  Edit reference
    Page Should Contain  None of the fields can be empty

Editing a reference with invalid year
    Go To  ${HOME_URL}/new_book_reference
    Title Should Be  Create a new book reference
    Input Text  author  Testi
    Input Text  title  testing
    Input Text  year  2024
    Input Text  publisher  test
    Click Button  Add a book
    Title Should Be  References
    Page Should Contain  Total references: 1
    Page Should Contain  Testi
    Click Button  edit
    Title Should Be  Edit reference
    Input Text  year  20
    Click Button  Save changes
    Title Should Be  Edit reference
    Page Should Contain  Year length must be 4
