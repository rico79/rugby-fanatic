# Rugby Fanatic

Rugby board game

## Installation

First, install python > 3.6 : https://wiki.python.org/moin/BeginnersGuide/Download

After, you have to install Flask and gunicorn to make it work locally (if you use Ubuntu, you should probably replace pip by pip3):

```
$ pip install Flask
$ pip install gunicorn
```

Then, clone the repo:

```
$ git clone https://github.com/rico79/rugby-fanatic.git
```

And that's it !! You can now develop...

## Run the app locally

If you use Ubuntu, you should probably replace python by python3:

```
$ python app.py
```

see localhost:5000

## Deploy the app

```
$ git push heroku master
```

[![Deploy](https://www.herokucdn.com/deploy/button.png)](https://heroku.com/deploy)