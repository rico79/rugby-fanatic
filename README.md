# Rugby Fanatic

Rugby board game

## Installation

### Python

First, install python > 3.6 : https://wiki.python.org/moin/BeginnersGuide/Download

After, you have to install Flask and gunicorn to make it work locally (if you use Ubuntu, you should probably replace pip by pip3):

```
$ pip install Flask
$ pip install gunicorn
```

### Nodejs ecosystem

You will need to install :
- nodejs: https://nodejs.org/en/download/package-manager/
- npm (should be installed with nodejs)
- yarn: https://yarnpkg.com/lang/en/docs/install/

Check that everything is OK:

```
$ node --version
$ npm --version
$ yarn --version
```

### Get Started

Clone the repo:

```
$ git clone https://github.com/rico79/rugby-fanatic.git
```

Then install the frontend dependencies:

```
$ cd rugby-fanatic
$ cd front
$ yarn install
```

To rebundle the frontend with webpack (each time the code is changed):

```
$ yarn run build
```

And that's it !! You can now develop...

## Run the app locally

From rugby-fanatic main directory run the app (if you use Ubuntu, you should probably replace python by python3):

```
$ python app.py
```

see localhost:5000

## Deploy the app

From rugby-fanatic main directory:

```
$ git push heroku master
```

[![Deploy](https://www.herokucdn.com/deploy/button.png)](https://heroku.com/deploy)