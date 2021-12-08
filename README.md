# CS 410 Course Project: Pop Punk Song Search

## Configuring your environment

This repo has a YAML file that you can use to instantiate a virtual environment for this project, called env.yml. In the terminal, navigate to the CourseProject directory. Then, run the following command:

`conda env create -f env.yml`

After the environment has been created, run this command to activate it:

`conda activate pop_punk_search`

## Running the flask app

The user interface that collects a query from a user, runs the Python script to compare it to the VSM, and returns the best matches was built using the Flask Python library. There are a few commands you will need to run in the command line in order to activate the application. From the CourseProject directory, run the following three commands:

Specify the flask app name:

`export FLASK_APP=pop_punk_gui`

Specify the flask environment:

`export FLASK_ENV=development`

Run the application:

`flask run`

After executing the final command, you will see a few lines printed in the terminal, including `* Running on http://127.0.0.1:5000/`. Once the application starts running, you will be able to go into your browser, go to  http://127.0.0.1:5000/, and you will see the search application!