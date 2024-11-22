*** Settings ***
Resource  resource.robot
Suite Setup      Open And Configure Browser
Suite Teardown   Close Browser
Test Setup       Reset References


*** Test Cases ***
Main page can be opened
    Go To  ${HOME_URL}
    Title Should Be  Reference app

Click Create New Book Reference Link
    Go To  ${HOME_URL}
    Click Link  Create a new book reference
    Title Should Be  Create a new book reference

Click Create New Article Reference Link
    Go To  ${HOME_URL}
    Click Link  Create a new article reference
    Title Should Be  Create a new article reference

Click See All References Link
    Go To  ${HOME_URL}
    Click Link  See all references
    Title Should Be  References
