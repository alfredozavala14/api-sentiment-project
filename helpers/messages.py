from mongoConnection import *
from check import *
from bson import ObjectId

def list_messages():
    '''
    Gives a list of all messages in the messages collection.

    Takes: nothing
    Returns: all mesages in the messages collection
    '''
    res = read_coll("messages",{})
    response = [m["character"] + ": " + m["line"] for m in res]
    return response

def get_message(obj):
    '''
    For a given season & episode, gives a list of all messages in the episode.

    Takes: season and episode numbers
    Returns: all mesages in the episode
    '''
    if not check_params(obj,["season", "episode"]):
        return {"response":400,"message":"Bad Request: 'season' and 'episode' are obligatory parameters"}
    q = {"season": int(obj["season"]), "episode": int(obj["episode"])}
    if not check_exists(q,"messages"):
        return {"response":400,"message":"Bad Request: season & episode do not exist"}
    res = read_coll("messages",q)
    return [m["name"] + ": " + m["line"] for m in res]

def get_message_from_char(obj):
    '''
    For a given season & episode and a character name gives a list of all messages in the episode from that character.

    Takes: season & episode numbers and character name
    Returns: all mesages in the episode from that character
    '''
    if not check_params(obj,["season", "episode", "name"]):
        return {"response":400,"message":"Bad Request: 'season', 'episode' and 'name' are obligatory parameters"}
    q = {"season": int(obj["season"]), "episode": int(obj["episode"]), "name": obj["name"]}
    if not check_exists(q,"messages"):
        return {"response":400,"message":"Bad Request: season & episode do not exist"}
    res = read_coll("messages",q)
    return [m["name"] + ": " + m["line"] for m in res]

def insert_message(obj):
    '''
    Given a season & episode number, a character name and a line, generates a new document in the messages collection

    Takes: season & episode number, character name and line
    Returns: "_id" of new message
    '''
    if not check_params(obj,["season", "episode", "name", "line"]):
        return {"response":400,"message":"Bad Request: 'season' 'episode', 'name' and 'line' are obligatory parameters"}
    q1 = {"season": int(obj["season"]), "episode": int(obj["episode"])}
    if not check_exists(q1,"episodes"):
        return {"response":204,"message":"No content: there is no season & episode with those numbers in the espisodes collection"}
    q2 = {"name": obj["name"]}
    if not check_exists(q2,"characters"):
        return {"response":204,"message":"No content: there is no character with that name in the characters collection"}
    res = write_coll("messages",obj)
    return res.inserted_id

def delete_message(obj):
    '''
    Given a message ID deletes the line from the messages collection

    Takes: message ID
    Returns: nothing
    '''
    if not check_params(obj,["id"]):
        return {"response":400,"message":"Bad Request: 'id' is an obligatory parameter"}
    q = {"_id":ObjectId(obj["id"])}
    if not check_exists(q,"messages"):
        return {"response":400,"message":"Bad Request: line with given 'id 'does not exist"}
    delete_coll("messages",q)
    return {"response":200,"message":"Message successfully deleted"}

def update_message(obj):
    '''
    Given a message ID and new attributes, updates the message from the messages collection
 
    Takes: message ID
    Returns: nothing
    '''
    if not check_params(obj, ["id"],["season", "episode", "name", "line"]):
        return {"response":400,"message":"Bad Request: 'id' and at least one of ['season', 'episode', 'name' and 'line'] are obligatory parameters"}
    q = {"_id":ObjectId(obj["id"])}
    if not check_exists(q,"messages"):
        return {"response":400,"message":"Bad Request: message with given ID does not exist"}
    # check if character name exists in characters collection
    if "name" in obj:
        q_check = {"name": obj["name"]}
        if not check_exists(q_check,"characters"):
            return {"response":400,"message":"Bad Request: character with given name does not exist in characters collection"}
    # check if given season and episode exist in episodes collection
    # from given message ID, first check season and episode
    q_seas_n_epis = {"_id":ObjectId(obj["id"])}
    res = read_coll("messages",q_seas_n_epis)
    original_season = res[0]["season"]
    original_episode = res[0]["episode"]
    if "season" and "episode" in obj:
        q_check = {"season": int(obj["season"]), "episode": int(obj["episode"])}
        if not check_exists(q_check,"episodes"):
            return {"response":400,"message":"Bad Request: new season and episode do not exist in episodes collection"}
    elif "season" in obj:
        # find given episode with message ID
        q_check = {"season": int(obj["season"]), "episode": int(original_episode)}
        if not check_exists(q_check,"episodes"):
            return {"response":400,"message":"Bad Request: given season and episode do not exist in episodes collection"}
    elif "episode" in obj:
        # find given season with message ID
        q_check = {"season": int(original_season), "episode": int(obj["episode"])}
        if not check_exists(q_check,"episodes"):
            return {"response":400,"message":"Bad Request: given season and episode do not exist in episodes collection"}
    obj.pop("id")
    for a in ["season", "episode"]:
        if a in obj:
            obj[a] = int(obj[a])
    update_coll("messages",q,obj)
    return {"response":200,"message":"Message successfully updated"}

