# Landing Page Boilerplate

Create and deploy a landing page in less than 5 minutes, thanks to Flask and Heroku.

## Installation

First step: make it working on your computer

```sh
git clone

# create a virtual environment
python -m venv venv
source venv/bin/activate

# install the dependencies
python -m pip install -r requirements.txt

export FLASK_APP=landing_page.py
export FLASK_ENV=development

flask run
```

Second step: deploy on Heroku
```sh
heroku login

# create and configure a new Heroku app
heroku apps:create my_app_name
heroku config:set FLASK_APP=landing_page.py

# deploy on Heroku
git push heroku master

# make sure you have allocated enough dynos
heroku ps:scale web=1
```

## Usage

Describe the expected result in the file `app/routes.py`. The template will adapt automatically.