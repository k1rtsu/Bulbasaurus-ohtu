*** Settings ***
Resource  resource.robot
Suite Setup      Open And Configure Browser
Suite Teardown   Close Browser
Test Setup       Reset References

*** Test Cases ***

After a misc is added, it will appear in the list of references.
    Go To  ${HOME_URL}/new_misc_reference
    Title Should Be  Create a new misc reference
    Input Text  author  TestAuthorMisc
    Input Text  title  TestTitleMisc
    Input Text  year  2024
    Input Text  note  This is a test misc note.
    Click Button  Add a misc reference
    Title Should Be  References
    Page Should Contain  TestAuthorMisc
    Page Should Contain  TestTitleMisc
    Page Should Contain  2024
    Page Should Contain  This is a test misc note.
