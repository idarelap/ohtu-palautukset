*** Settings ***
Resource  resource.robot
Test Setup  Input New Command and Create User

*** Test Cases ***
Register With Valid Username And Password
    Input Credentials  valle  salasana123
    Output Should Contain  New user registered

Register With Already Taken Username And Valid Password
    Input Credentials  kalle  uusisalasana123
    Output Should Contain  Username already taken

Register With Too Short Username And Valid Password
    Input Credentials  ka  salasana123
    Output Should Contain  Username must be at least 3 characters long

Register With Enough Long But Invalid Username And Valid Password
    Input Credentials  källe  salasana123
    Output Should Contain  Invalid username

Register With Valid Username And Too Short Password
    Input Credentials  ville  lyhyt1
    Output Should Contain  Password must be at least 8 characters long

Register With Valid Username And Long Enough Password Containing Only Letters
    Input Credentials  ville  salasana
    Output Should Contain  Password must contain at least one number or special character

*** Keywords ***
Input New Command and Create User
    Input New Command
    Create User  kalle  kalle123
