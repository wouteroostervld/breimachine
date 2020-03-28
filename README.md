# breimachine

The best knitting bot for your all men knitting circle.

## requirements

Python 3.7.x

## deployment on AWS Lambda

Add token to config.py (see config.py.example).

Create a virtualenv (eg. using virtualenvwrapper). Install requirements:

    mkvirtualenv breiwerkje
    pip install -r requirements.txt
    pip install zappa

Init (if deploying separate/own instance):

    rm zappa_settings.json
    zappa init

Deploy:

    zappa deploy
    
Or update:

    zappa update

Zappa shows the url it is deployed to.

Set webhook url:

    ./setwebhook URL
    
## Smoke testing

python ./breimachine.py

## Available morbid commands

 *   /stats (show covid-19 stats for Netherlands)
