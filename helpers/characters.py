from mongoConnection import *
from check import *

def list_characters():
    '''
    Gives a list of all characters in the characters  collection.

    Takes: nothing
    Returns: all characters in the characters  collection
    '''
    res = read_coll("characters",{})
    response = {c["name"] for c in res}
    return response

def insert_character(obj):
    '''
    Given a character name, generates a new document in the characters collection

    Takes: character name
    Returns: "_id" of new character
    '''
    if not check_params(obj,["name"]):
        return {"response":400,"message":"Bad Request: 'name' is an obligatory parameter"}
    q = {"name": obj["name"]}
    if check_exists(q,"characters"):
        return {"response":400,"message":"Bad Request: there is already a character with that name"}
    res = write_coll("characters",obj)
    return res.inserted_id

def delete_character(obj):
    '''
    Given a character name, deletes the character from the characters collection
    and its messages from the messages collection

    Takes: character name
    Returns: nothing
    '''
    if not check_params(obj,["name"]):
        return {"response":400,"message":"Bad Request: 'name' is an obligatory parameter"}
    q = {"name": obj["name"]}
    if not check_exists(q,"characters"):
        return {"response":400,"message":"Bad Request: character with given name does not exist"}
    delete_coll("characters",q) # delete character from characters collection
    delete_coll("messages",q) # delete character's messages from messages collection
    return {"response":200,"message":"Character successfully deleted"}

def update_character(obj):
    '''
    Given a character name and a new name, updates the character's name from the characters collection
    and the messages collection

    Takes: character name
    Returns: nothing
    '''
    if not check_params(obj,["name", "new_name"]):
        return {"response":400,"message":"Bad Request: 'name' ane 'new_name' are obligatory parameters"}
    q = {"name": obj["name"]}
    if not check_exists(q,"characters"):
        return {"response":400,"message":"Bad Request: character with given name does not exist"}
    obj.pop("name")
    obj["name"] = obj["new_name"]
    obj.pop("new_name")
    update_coll("characters",q,obj) # update character in characters collection
    update_coll("messages",q,obj) # update character's messages in messages collection
    return {"response":200,"message":"Character successfully updated"}