# auction
An entry for IIIT Bhubaneswar's Web Dev challenge.

### How to get it up and running?

* Install `python` (`python3` because it's 2019), `postgresql`
* Clone the repo
* Start `postgresql` service (or equivalent) and create a new database for use
  with this project.
* Create a new [python virtual
  environment](https://docs.python.org/3/library/venv.html) and activate it.
* Install `django`, `django-authtools`, `django-widget-tweaks` and `psycopg2`
  using `pip`. [Don't use `sudo` with `pip`](https://xkcd.com/1987/).
* `cd` into the cloned repo while still in the virtual environment.
* Copy `auction/sample.conf.py` to `auction/conf.py`. Add the required
  information to it: database name, username, password from the thrid step.
* Run the following: `python manage.py makemigrations`, `python manage.py
  migrate`. Create a "superuser" if you want.
* Start the development server: `python manage.py runserver`
* Let me know if you cannot get it to run on your machine.
