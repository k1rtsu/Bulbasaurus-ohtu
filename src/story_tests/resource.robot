*** Settings ***
Library  SeleniumLibrary

*** Variables ***
${SERVER}     localhost:5001
${DELAY}      0.5 seconds
${HOME_URL}   http://${SERVER}
${RESET_URL}  http://${SERVER}/reset_db
${BROWSER}    chrome
${HEADLESS}   false

*** Keywords ***
Open And Configure Browser
    IF  $BROWSER == 'chrome'
        ${options}  Evaluate  sys.modules['selenium.webdriver'].ChromeOptions()  sys
    ELSE IF  $BROWSER == 'firefox'
        ${options}  Evaluate  sys.modules['selenium.webdriver'].FirefoxOptions()  sys
    END
    IF  $HEADLESS == 'true'
        Set Selenium Speed  0
        Call Method  ${options}  add_argument  --headless
    ELSE
        Set Selenium Speed  ${DELAY}
    END
    Open Browser  browser=${BROWSER}  options=${options}

Reset References
    Go To  ${RESET_URL}

Select Book From The Dropdown Menu
    Select From List By Value  id=new-reference-form-selector  new-book-form-container
    Wait Until Element Is Visible  id=new-book-form-container

Select Article From The Dropdown Menu
    Select From List By Value  id=new-reference-form-selector  new-article-form-container
    Wait Until Element Is Visible  id=new-article-form-container

Select Inproceedings From The Dropdown Menu
    Select From List By Value  id=new-reference-form-selector  new-inproceedings-form-container
    Wait Until Element Is Visible  id=new-inproceedings-form-container

Select Misc From The Dropdown Menu
    Select From List By Value  id=new-reference-form-selector  new-misc-form-container
    Wait Until Element Is Visible  id=new-misc-form-container
