FastAPI Server

This code defines a FastAPI server that exposes a set of routes for managing transactions and spent points.

Dependencies

The following dependencies are required to run this code:

datetime: Provides date and time functionality.
sqlite3: Provides functionality for working with SQLite databases.
FastAPI: A web framework for building APIs with Python.
pydantic: A library for defining and validating data models.

The following routes are exposed by this server:

/add-transaction/
This route allows for new transactions to be added to the system. It expects a TransactionRequest payload in the request body and returns a 200 response on success.

/get-transactions
This route returns a list of all transactions that have been added to the system.

/spend-points/
This route allows for points to be spent from the system. It expects a SpendRequest payload in the request body and returns a list of PayerPoints objects representing the points spent by each payer.

/points-balance/
This route returns a list of PayerPoints objects representing the current balance of points for each payer.

In-Memory Storage

The following variables are used to store data in memory:

transactions (list): A list of transaction objects.
ls (list): A list of payer points objects.
spent_total (list): A list of spent points objects.
payer_totals (dict): A dictionary mapping payers to their total points.
Note that this data is not persisted between server restarts and is only available for the duration of the server's runtime. If you want to persist the data, you will need to store it in a more permanent storage solution, such as a database.


To run this code, you will need to have the required dependencies installed and have a Python environment set up. You can install the dependencies by running the following command:

pip install fastapi pydantic sqlite3

Once the dependencies are installed, you can start the server by running the following command:

uvicorn spend_points:app --reload

Now go to http://127.0.0.1:8000/docs.

You will see the automatic interactive API documentation

In the interactive API documentation

Click on the button "Try it out" for the API that you wish to run, it allows you to fill the parameters and directly interact with the API

Then click on the "Execute" button, the user interface will communicate with your API, send the parameters, get the results and show them on the screen





