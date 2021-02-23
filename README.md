![South-Park-image](https://cnet4.cbsistatic.com/img/9MbycUhBYwyOxNK7SAv6LaUooPc=/1200x675/2019/05/10/274dd528-b38a-4029-a0e3-52c3d0061600/south-park.jpg)

# api-sentiment-project

## Introduction

For this week's Irnhack project, we are creating an API that can both receive data from users through post requests and serve data to users through get requests. The data will be stored in a MongoDB and the API will be created using Flask. As a bonus, we will perform sentiment analysis on the conversations stored in the DB. 

For this exercise, I have used a dataset from kaggle that has more than 70,000 lines of South Park dialogue by season, episode, and character. [Here](https://www.kaggle.com/tovarischsukhov/southparklines) is a link to the dataset. 

## Libraries used

During the project, I have used the following libraries:
- [Pandas](https://pandas.pydata.org/)
- [Pymongo](https://pymongo.readthedocs.io/en/stable/)
- [Numpy](https://numpy.org/doc/)
- [nltk](https://www.nltk.org)
- [Seaborn](https://seaborn.pydata.org)
- [Matplotlib](https://matplotlib.org/stable/contents.html)
- [Os](https://docs.python.org/3/library/os.html)
- [Json](https://docs.python.org/3/library/json.html)
- [bson](https://pymongo.readthedocs.io/en/stable/api/bson/index.html)
- [regex](https://docs.python.org/3/library/re.html)
- [tqdm](https://pypi.org/project/tqdm/)

## Work done

- I designed a database in Mongo to store the data to be served by the API.
- I included the data from the Kaggle dataset in the MongoDB through pymongo, to use as a test for the API. The Mongo DB has three collections:
    - characters: includes the names of all caracters in the show
    - episodes: includes all seasons and episodes in the show
    - messages: includes all lines said in the show, with the corresponding character name and season & esisode numbers
- I wrote an API using flask that stores and serves data from the MongoDB through various endpoints. The endpoints I defined are the following:
    - `/characters` : returns the name of all characters in the database
    - `/messages` : returns all the messages in the database with the name of the character who spoke the line
    - `/episodes` : returns all seasons and episodes in the database
    - `/seasons` : returns all seasons in the database
    - `/messages/episode` : for a given season & episode, gives a list of all messages in the episode. Takes season and episode numbers
    - `/messages/episode/character` : for a given season & episode and a character name gives a list of all messages in the episode from that character
    - `/episodes/new` : given a season & episode number, generates a new document in the episodes collection. Returns id of the new episode
    - `/characters/new` : given a character name, generates a new document in the characters collection. Returns id of the new character
    - `/messages/new` : given a season & episode number, a character name and a line, generates a new document in the messages collection. Returns id of the new message
    - `/episodes/delete` : given a season & episode, deletes the season & episode from the episodes collection and its messages from the messages collection
    - `/characters/delete` : given a character name, deletes the character from the characters collection and its messages from the messages collection
    - `/messages/delete` : given a message ID deletes the line from the messages collection
    - `/episodes/edit` : given a season & episode number and a new number, updates the season & episode number from the episodes collection and the messages collection
    - `/characters/edit` : given a character name and a new name, updates the character's name from the characters collection and the messages collection
    - `/messages/edit` : given a message ID and new attributes (season, episode, character name and / or line), updates the message from the messages collection

- I extracted the emotional value of messages per user through sentiment analysis and used visualization libraries to find trends in the data


## Deliverables

The project has three main deliverables:
- A jupyter notebook where I used pymongo to populate a Mongo DB that can be served through the API
- A working API that can be used to store and serve data
- A jupyter notebook where I used sentiment analysis libraries and visualization libraries to analyze the sentiment of the dialogue in South Park