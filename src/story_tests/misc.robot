*** Settings ***
Resource  resource.robot
Suite Setup      Open And Configure Browser
Suite Teardown   Close Browser
Test Setup       Reset References

*** Test Cases ***

After a misc is added, it will appear in the list of references.
    Go To  ${HOME_URL}
    Title Should Be  App
    Select Misc From The Dropdown Menu
    Set Author  Test Author
    Set Title  Test Title
    Set Year  2024
    Set Note  This is a test misc note.
    Click Button  Add a misc reference
    Page Should Contain  Test Author
    Page Should Contain  Test Title
    Page Should Contain  2024
    Page Should Contain  This is a test misc note.


*** Keywords ***


Set Author
    [Arguments]  ${author}
    Input Text  misc-author  ${author}

Set Title
    [Arguments]  ${title}
    Input Text  misc-title  ${title}

Set Year
    [Arguments]  ${year}
    Input Text  misc-year  ${year}

Set Note
    [Arguments]  ${note}
    Input Text  misc-note  ${note}
