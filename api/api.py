from flask import Flask, request
from bson import json_util

import sys
sys.path.append('../helpers')

from mongoConnection import *
from characters import *
from episodes import *
from messages import *

app = Flask('south_park_api')

@app.route("/characters")
def return_chars():
    return json_util.dumps(list_characters())

@app.route("/messages")
def  return_messages():
    return json_util.dumps(list_messages())

@app.route("/episodes")
def  return_episodes():
    return json_util.dumps(list_episodes())

@app.route("/seasons")
def  return_seasons():
    return json_util.dumps(list_seasons())

@app.route("/messages/episode")
def  return_messages_in_episode():
    args = dict(request.args)
    return json_util.dumps(get_message(args))

@app.route("/messages/episode/character")
def  return_messages_from_char_in_episode():
    args = dict(request.args) 
    return json_util.dumps(get_message_from_char(args))

@app.route("/episodes/new")
def  episodes_new():
    args = dict(request.args)
    id = insert_episode(args)
    return json_util.dumps({"_id":id})

@app.route("/characters/new")
def  characters_new():
    args = dict(request.args)
    id = insert_character(args)
    return json_util.dumps({"_id":id})

@app.route("/messages/new")
def  messages_new():
    args = dict(request.args)
    id = insert_message(args)
    return json_util.dumps({"_id":id})

@app.route("/episodes/delete")
def  episodes_delete():
    args = dict(request.args)
    return json_util.dumps(delete_episode(args))

@app.route("/characters/delete")
def  characters_delete():
    args = dict(request.args)
    return json_util.dumps(delete_character(args))

@app.route("/messages/delete")
def  messages_delete():
    args = dict(request.args)
    return json_util.dumps(delete_message(args))

@app.route("/episodes/edit")
def episodes_edit():
    args = dict(request.args)
    return json_util.dumps(update_episode(args))

@app.route("/characters/edit")
def characters_edit():
    args = dict(request.args)
    return json_util.dumps(update_character(args))

@app.route("/messages/edit")
def messages_edit():
    args = dict(request.args)
    return json_util.dumps(update_message(args))

app.run(debug=True)