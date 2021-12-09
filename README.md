# CS 410 Course Project: Pop Punk Song Search 

- [Project Proposal](https://github.com/kellycosgrove/CourseProject/blob/main/CS_410_Project_Proposal.pdf)
- [Progress Report](https://github.com/kellycosgrove/CourseProject/blob/main/CS_410_Progress_Report.pdf)
- [Self Evaluation]()
- [Demo]()
- Documentation below

# Documentation

This project has two parts: The code used to create the vector space model and the code used to get a query from a user and compare it to the VSM. This documentation will cover all of the code/artifacts produced to accomplish both of these.

## Creating the VSM

### Script: pop_punk_create_vsm.py

This Python script contains all the code necessary to gather the Pop Punk song lyric corpus and use it to create a Vector Space Model.

The bands leveraged for the corpus were selected based on [this article](https://indiepanda.net/best-pop-punk-bands/) which lists the most popular pop-punk bands. Two were excluded:

- Buzzcocks - this band was active between 1976 and 1981, and therefore does not fall into the 30-year range as was specified in the project proposal
- Lit - this band was originally included in the corpus; however, the API leveraged to pull lyrics was changing the artist name from "Lit" to "Lil Wayne", therefore there was no way to pull in lyrics from Lit songs.

In total 37 bands were used. The [lyricsgenius](https://lyricsgenius.readthedocs.io/en/master/) Python library was used to interact with the Genius.com API to pull lyrics and store the lyric information in JSON files. The Genius API does seem to have an issue with erroring out periodically, so for this reason, the code provides a limit of only the 20 most popular songs per artist.

Once all the lyric JSONs are created, the code combines these into one data dictionary, and then leverages the [Gensim](https://radimrehurek.com/gensim/) Python library to create the Vector Space Model, which is based on Bag-of-Words and was transformed with TF-IDF.

All artifacts produced for the VSM are stored in the artifacts library of this repo.

## Interacting with the VSM

### Script: pop_punk_song_search.py

The **main** function in this script is what is called to compare the VSM against a query, which is taken as input. The script loads all components of the VSM that were saved to the artifacts folder, runs the query vector through the model, and pulls the top four songs/artists to return along with the original query.

### Script: pop_punk_gui.py

This Python script contains the Flask application that forms the connection between a front-end HTML GUI and the back-end pop_punk_song_search.py Python script. It renders an HTML script that contains a search bar, waits for a search term to be submitted, runs that search term through the **main** function from pop_punk_song_search.py, and then renders the "results" HTML script with the information returned from the VSM.

### Script: tempates/pop_punk_gui.html

This is the HTML page initially rendered from the flask app. It contains a search bar where the user enters some song lyrics to be compared to the VSM.

### Script: templates/pop_punk_gui_results.html

This is the HTML page that is rendered once the user's query is run through the VSM and results are returned. It contains a search bar, so the user can search more lyrics if they wish. Underneath, it lists the query that the user just entered, the most similar match, and the subsequent three matches.

### File: env.yml

This YAML configuration file can be used to create a virtual environment with all libraries necessary to interact with the VSM. More information can be found below on how to configure your environment with it.

## Testing the VSM

Within the **test** folder, **test_cases.md** lists out 10 lyric queries that were run through the VSM, the results, and the Mean Reciprocal Rank score for each. The average MRR was 0.7.

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
