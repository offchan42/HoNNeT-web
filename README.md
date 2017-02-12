# HoNNeT-web
Website for my HoNNeT deep learning side-project

It contains the files required to run the web inside Heroku. I use Vue.js, Bulma.io and Flask as web technology stack.

## Requirements
- Python 3
- virtualenv (`pip install virtualenv`)

## Running on local host (your machine)
1. Clone this repository and `cd` into it.
2. Create a development environment dedicated for this repository because we are
   going to install something there: run `virtualenv venv`.
3. Install dependencie: `pip install -r requirements.txt` (`gunicorn` is
   unnecessary, don't worry if there is an error installing it, it's required for
   the real Linux web server)
   This will install some libraries into that `venv` directory.
4. Run `python app.py` to run the application
5. Open web browser and go to http://127.0.0.1:5000/
6. Play with the application.

Have fun!
