# Backend of Korean Skin Care Ecommerce site
This backend is of version-1.0.

## Setup
First set your path to `scr` directory
`cd src`
Now you must setup environment.
`python -m venv .env`
then you start the environtment
`.\env\Scripts\activate.bat` (remember this is for windows CMD terminal.)

then install all the required dependencies
`pip install -r requirements.txt`

you can install all dependencies seperately:
FastAPI -
`pip install fastapi[standard]`
MySQL -
`pip install mysql-connector-python`
MongoDB -
`python -m pip install pymongo`

## Database
You can setup your database in your PC. the database files are given in the database folder. there is MySQL SQL file and there is also mongoDB collections files that you can import which is in json format.

## API
check swagger for api doc---- 

The backend api routes are given below:
1. get **all users**: `/users`
2. get **one user**: `/user/[user_id]`
3. get user **wishlist**: `/user/[user_id]/wishlist`
4. get user **all orders**: `user/[user_id]/orders`
5. get user **one order** details: `user/[user_id]/orders/[order_id]`