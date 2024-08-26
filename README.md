# Engvocab

A website to use during idle moments to learn the Italian translation of some English terms and expressions.

Created with Django and MySQL.

## Local installation

1. Clone the repository
2. Install the dependencies
3. Setup environment variables file `template.env`
5. Setup MySQL database
6. Run the server

### 2) Dependencies

You need to install the following packages:

**Debian**

- Python

		$ sudo apt install python3 python3-pip

- MySQL

		$ sudo apt install default-libmysqlclient-dev build-essential pkg-config mysql-server mysql-client

- Python packages
	Go in the root directory of the project and run
	
		$ pip3 install -r requirements.txt

	If you get an error involving metadata warning like
	"WARNING: Generating metadata for package mysqlclient produced metadata for project name unknown."
	or
	"Requested unknown from https://... has inconsistent name: filename has 'mysqlclient', but metadata has 'unknown'"

	then you need to update pip:

		$ pip install --upgrade pip

**Fedora**

- Python

		$ sudo dnf install python3 python3-pip python3-devel

- MySQL

		$ sudo dnf install community-mysql-server community-mysql-devel

- Python packages
	Go to the root directory of the project and run
	
		$ pip3 install -r requirements.txt
	
### 3) Environment variables file

Fill the `template.env` file.
This is an example:
```txt
DB_ENGINE=django.db.backends.mysql
DB_NAME=mydatabase
DB_USER=django
DB_PASSWORD=''
DB_HOST=127.0.0.1
DB_PORT=3306
DB_SECRET_KEY="i02$0g@6q!3gx%v2zzorh#7k&5!vk=&%k$jm!jr^a7e8d)e*0%9"
DB_DEBUG=1
```
Note that the value given to `DB_NAME`, `DB_USER`, `DB_PASSWORD` must match with the corresponding field when we will configure the database.

Rename `template.env` to simply `.env`

### 4) Setup MySQL database

Start the MySQL server with one of the following command based on your system:

- op1:
	
		$ sudo systemctl start mysqld

- op2:

		$ sudo service mysql start

Then open a MySQL monitor with the following command:

	$ sudo mysql -u root -p

and enter your root password.

Now in the MySQL command line run the following three commands:

	> create user '<username>'@'localhost' identified by '<password>';
	
Note: the username and the password must be the same as the ones specified the the environment variables file, in this case, for example must be:

	> create user 'django'@'localhost' identified by '';

then grant all the privileges to the user just created:

	> grant usage on *.* to 'django'@'localhost';
	> grant all privileges on *.* to 'django'@'localhost';

always remember to use the right username.

Now let's create the database:

	> create database mydatabase;

Even in this case the may must match the one given in the environment variables file.

Make Django create the tables:
Go to the root directory of the project and run:

	$  python3 manage.py migrate

Finally fill the tables with some stuff from the `db_example.sql` file:

	$ sudo mysql -u root -p mydatabase < db_example.sql

### 5) Run the server

Run the server with the following command:

	$ python3 manage.py runserver

## Future updates (if time permits)

- make the shell interactive
- add the possibility to change username and password
- Provide more data in the progress page
- Show confidence progress for each expressions
