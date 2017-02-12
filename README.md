# HoNNeT-web
Website for my HoNNeT deep learning side-project

It contains the files required to run the web inside Heroku. I use Vue.js,
Bulma.io and Flask as web technology stack.

## Requirements
- Python 3
- virtualenv (`pip install virtualenv`)

## Running on local host (your machine)
1. Clone this repository and `cd` into it.
2. Create a development environment dedicated for this repository because we are
   going to install something here: run `virtualenv venv`
3. Tell python to use the environment recently created by running `source
   activate venv` (or `activate venv` if you are on Windows).
4. Install dependencies: `pip install -r requirements.txt` (`gunicorn` is
   unnecessary, don't worry if there is an error installing it, it's required for
   the real Linux web server only)
   This will install some libraries into that `venv` directory.
5. Run `python app.py` to run the application
6. Open web browser and go to http://127.0.0.1:5000/
7. Play with the application.

Have fun!
