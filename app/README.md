# Web Application

## Installation

@todo: Debian packaging.

## Development

1. Install dependencies from requirements.txt.

```
# Using pip
sudo pip install -r requirements.txt
```

```
# Using Debian packages (not recommended)
sudo apt-get install python-flask ...
```

2. Create a new PostgreSQL or MySQL database and user.
3. Run db.py with database connection string.

Example:

```
# PostgreSQL
python db.py --db postgresql://scott:tiger@localhost/wos --init --demo

# MySQL
python db.py --db mysql://scott:tiger@localhost/wos --init --demo
```

4. Make a copy of the sample config file and fill in values.

```
cp wos.ini.sample wos.ini
```

5. Start the web app.

```
# Ensure that the path given to --config is absolute!
python app.py --config /this/path/has/to/be/absolute/wos.ini
```

5. Visit http://localhost:8081 in a browser.
