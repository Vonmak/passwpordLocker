# Password Locker

Simple Python App that creates new credentials with properties. Touches on Test Driven Development using unittest (Python test framework).

## Technologies Used

Python3.10
unittest (Python test framework)
random password generator

### Setup Instructions and Installation

Clone this repository to a location in your file system. git clone https://github.com/Vonmak/passwordlocker.git
Open terminal command line then navigate to the root folder of the application. cd passwordLocker
Run ./main.py

## Behavior Driven Development

#### Displays Intro Message to user

OUTPUT: Hello! I hope you've been good.
Welcome to your Password Locker.
Choose what you want to do:
su - signup, li - login

INPUT: ""
OUTPUT: "Hello victor. what would you like to do?"

#### Hi victor!, What would you like to do?

#### Enter short code

INPUT: "ca"
INPUT: "account", "account username", "account password"
OUTPUT: "New credential victor created" - Create new credential by providing required properties

#### Enter Short Code

INPUT: "dc"
OUTPUT: "Enter the number you want to search for" - Prompts user to enter number to search for
OUTPUT: 'twitter' "victor" '123456' - Displays existing credentials

#### Enter Short Code

INPUT: "fc"
INPUT: "twitter" - Search by account
OUTPUT: "account.......twitter, account username....... victor - Returns credential if exists

## Development

Want to contribute? Great!

To fix a bug or enhance an existing module, follow these steps:

    Fork the repo
    Create a new branch (git checkout -b improve-feature)
    Make the appropriate changes in the files
    Add changes to reflect the changes made
    Commit your changes (git commit -am 'Improve feature')
    Push to the branch (git push origin improve-feature)
    Create a Pull Request

## Known Bugs

If you find a bug (the website couldn't handle the query and or gave undesired results), kindly open an issue here by including your search query and the expected result.

If you'd like to request a new function, feel free to do so by opening an issue here. Please include sample queries and their corresponding results.
