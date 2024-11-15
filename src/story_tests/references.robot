*** Settings ***
Resource  resource.robot
Suite Setup      Open And Configure Browser
Suite Teardown   Close Browser
Test Setup       Reset References


*** Test Cases ***
Main page can be opened
    Go To  ${HOME_URL}
    Title Should Be  Reference app

