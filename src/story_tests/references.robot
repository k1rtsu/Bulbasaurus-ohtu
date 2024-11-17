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

After adding a book, there is one
    Go To  ${HOME_URL}/new_reference
    Title Should Be  Create a new reference
    Input Text  author  Testi
    Input Text  title  testing
    Input Text  year  2024
    Input Text  publisher  test
    Click Button  Lisää kirja
    Title Should Be  References
    Page Should Contain  Total references: 1
