*** Settings ***
Resource  resource.robot
Test Setup  Input New Command And Create User

*** Test Cases ***
Register With Valid Username And Password
    Input Credentials  pekka  pekka123
    Output Should Contain  New user registered

Register With Already Taken Username And Valid Password
    Input Credentials  kalle  kalle123
    Output Should Contain  Username is already taken

Register With Too Short Username And Valid Password
    Input Credentials  ab  salasana1
    Output Should Contain  Username is too short

Register With Enough Long But Invalid Username And Valid Password
    Input Credentials  pekka1  salasana1
    Output Should Contain  Username must contain only letters a-z

Register With Valid Username And Too Short Password
    Input Credentials  pekka  sala1
    Output Should Contain  Password is too short

Register With Valid Username And Long Enough Password Containing Only Letters
    Input Credentials  pekka  salasanaa
    Output Should Contain  Password cannot contain only letters

*** Keywords ***
Input New Command And Create User
    Create User  kalle  kalle123
    Input New Command