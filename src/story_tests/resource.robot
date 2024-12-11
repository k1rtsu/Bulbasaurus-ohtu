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
    Input Text  article-title  title article
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


