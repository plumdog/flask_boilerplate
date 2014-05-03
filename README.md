Flask Boilerplate
=================

Delightfully slim and light Flask is, especially with regards set-up,
I found that there were some things that needed sorting out for
several apps, such as logins or migrations.

There are several branches, each at different stages of progress. By
doing a checkout to get the branch that you want, you can the use the
rename.sh script and off you go. At that stage you'll probably want to
nuke the git history too, and other files that won't be relevant to
your project, such as this one.

Branches (stepping-off points)
==============================

simple
------

Just the Flask "Hello World" app, with some config files.

templates
---------

Includes a standard base template, plus a page that uses that
template. Also, a token css file.

logins
------

Adds Flask-Logins. Adds a login page, and a secret page that is only
visible once logged in. Does not include a database, the username and
password are stored in the config file.

database
--------

Adds SQLAlchemy and Alembic for migrations. Add your models,
autogenerate your migration with alembic, and you're golden. Uses
MySQL and PyMySQL, and init.sh creates a database and a user in
MySQL. If you want to do it differently, change the configs and
remove/replace the database setup from init.sh.

HowTo
=====

The init script assumes that you have python3.4 installed, and that
this is what you'll be using for your project.

```
git clone https://github.com/plumdog/flask_boilerplate.git
cd flask_boilerplate
git checkout <branch>
./init.sh
./bin/python runserver
```
