# Python-projects
Practical Python Projects Repository: A Collection of Useful Python Projects for Everyday Use
# Password Checker Project

This project allows you to check whether a password has ever been compromised using the "Have I Been Pwned" API.

## Description

The Password Checker Project is a Python script that uses the "Have I Been Pwned" API to check if a password has been involved in any data breaches. It hashes the password and queries the API to determine if it exists in the database of compromised passwords.

## Features

- Check if a password has been compromised in data breaches.
- Securely hash passwords before querying the API.
- Easy integration with other projects and applications.

## Prerequisites

Before running the project, make sure you have the following dependencies installed:

- Python 3.x
- requests library
- hashlib library

## Installation

1. Clone the repository:
    ```CMD
   git clone https://github.com/DoneKan/password-checker.git
  2. Change into the project directory
     cd passwordchecker
  3.  Install the required dependencies:
      pip install -r requirements.txt
   
   Usage
 To check if a password has been compromised, call the pwned_api_check() function in the password_checker.py file with the password as an   argument:

from password_checker import pwned_api_check

pwned_api_check('your-password')


