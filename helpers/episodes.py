from mongoConnection import *
from check import *

def list_episodes():
    '''
    Gives a list of all seasons and episodes in the episodes collection.

    Takes: nothing
    Returns: all seasons and episodes in the episodes collection
    '''
    res = read_coll("episodes",{})
    response = {}
    response = ["Season " + str(e["season"]) + ": episode " + str(e["episode"]) for e in res]
    return response

def list_seasons():
    '''
    Gives a list of all seasons in the episodes collection.

    Takes: nothing
    Returns: all seasons in the episodes collection
    '''
    res = read_coll("episodes",{})
    response = {"Season " + str(e["season"]) for e in res}
    return response

def insert_episode(obj):
    '''
    Given a season & episode number, generates a new document in the episodes collection

    Takes: season number & episode number
    Returns: "_id" of new season & episode
    '''
    if not check_params(obj,["season", "episode"]):
        return {"response":400,"message":"Bad Request: 'season' and 'episode' are obligatory parameters"}
    q = {"season": int(obj["season"]), "episode": int(obj["episode"])}
    if check_exists(q,"episodes"):
        return {"response":400,"message":"Bad Request: there is already a season & episode with that number"}
    obj = q # to make sure season and episode are int
    res = write_coll("episodes",obj)
    return res.inserted_id

def delete_episode(obj):
    '''
    Given a season & episode, deletes the season & episode from the episodes collection
    and its messages from the messages collection

    Takes: season number & episode number
    Returns: nothing
    '''
    if not check_params(obj,["season", "episode"]):
        return {"response":400,"message":"Bad Request: 'season' and 'episode' are obligatory parameters"}
    q = {"season": int(obj["season"]), "episode": int(obj["episode"])}
    if not check_exists(q,"episodes"):
        return {"response":400,"message":"Bad Request: season and episode with given number do not exist"}
    delete_coll("episodes",q) # delete episodes from episodes collection
    delete_coll("messages",q) # delete episode's messages from messages collection
    return {"response":200,"message":"Episode successfully deleted"}

def update_episode(obj):
    '''
    Given a season & episode number and a new number, updates the season & episode number from the episodes collection
    and the messages collection

    Takes: season number & episode number and new season number & episode number
    Returns: nothing
    '''
    if not check_params(obj,["season", "episode", "new_season", "new_episode"]):
        return {"response":400,"message":"Bad Request: 'season', 'episode', 'new_season' and 'new_episode' are obligatory parameters"}
    q = {"season": int(obj["season"]), "episode": int(obj["episode"])}
    if not check_exists(q,"episodes"):
        return {"response":400,"message":"Bad Request: season and episode with given number do not exist"}
    for e in ["season", "episode"]:
        obj.pop(e)
    obj["season"] = int(obj["new_season"])
    obj["episode"] = int(obj["new_episode"])
    for f in ["new_season", "new_episode"]:
        obj.pop(f)
    update_coll("episodes",q,obj) # update season & episode in episodes collection
    update_coll("messages",q,obj) # update season & episode in messages collection
    return {"response":200,"message":"Episode successfully updated"}

