*** Settings ***
Resource  resource.robot
Suite Setup      Open And Configure Browser
Suite Teardown   Close Browser
Test Setup       Reset References


*** Test Cases ***

After inproceedings is added, it will appear in the list of references
    Go To  ${HOME_URL}/new_inproceedings_reference
    Title Should Be  Create new inproceedings reference
    Input Text  author  Testi
    Input Text  title  testing
    Input Text  year  2024
    Input Text  booktitle  test
    Click Button  Add inproceedings
    Page Should Contain  Total references: 1
    Page Should Contain  Inproceedings:
    Page Should Contain  Testi

Trying to add inproceedings with no author and failing
    Go To  ${HOME_URL}/new_inproceedings_reference
    Title Should Be  Create new inproceedings reference
    Input Text  title  testing
    Input Text  year  2024
    Input Text  booktitle  test
    Click Button  Add inproceedings
    Title Should Be  Create new inproceedings reference
    Page Should Contain  Missing required fields

Trying to add inproceedings with invalid year and failing
    Go To  ${HOME_URL}/new_inproceedings_reference
    Title Should Be  Create new inproceedings reference
    Input Text  author  Testi
    Input Text  title  testing
    Input Text  year  20
    Input Text  booktitle  test
    Click Button  Add inproceedings
    Title Should Be  Create new inproceedings reference
    Page Should Contain  Year length must be 4