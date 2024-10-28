# Banking_Website
The Online Bank System has the following functionalities :
  1. Login/Logout
       Login as existing user or new user .
       Existing user logs in with username and password.
       While new user creates a username and password.

  2. Account Management
       Create or delete accounts ,View account details , account balance , view number of accounts of each user and their respective details.
       For new users , on account creation - a random account number is generated and provided.

  3. Transaction Management
       Withdraw, Deposit

  4. Statement Generation 
       based on specified criteria (credit transactions, debit transactions over the given period)


## Technologies used : 
  1. Django 3.x
  2. Mysql

## Steps to execute the code :


### 1. Set up the database

Change the password of the database in final/bank/settings.py which you have used for mysql

--Use the command to create the database

>> mysql -u root -p
>> Enter the password
>> create database Bank_DB;

### 2. Create the migration for the database

 >>python manage.py makemigrations
 >>python manage.py migrate

### 3. Run the Project

>>python manage.py runserver

( This will start the webapp in localhost )




