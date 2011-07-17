from facebook import GraphAPI
from  abstract_adapter import (AbstractAdapter,
                               AbstractPerson,
                               AbstractAlbum)

from factory import registerAdapter

class FacebookAdapter(AbstractAdapter):

    access_token = ""
    graph_api    = None

    def __init__(self, params):

        if "access_token" in params:
            self.access_token = params["access_token"]
            self.graph_api = GraphAPI(self.access_token)
        else:
            raise LookupError("access_token key was not found in parameter dictionary")
        pass

    def getAuthorizedPerson(self):
        user_object = self.graph_api.get_object("me")
        return FacebookPerson(self.graph_api, user_object)

    def getPerson(self, person_id):
        user_object = self.graph_api.get_object(person_id)
        return FacebookPerson(self.graph_api, user_object)

    def getServiceName(self):
        return "Facebook Social Network"

    def getServiceDescription(self):
        pass

    def getServiceUrl(self):
        pass


class FacebookPerson(AbstractPerson):

    graph_api = None
    
    def __init__(self, graph_api, user_object):
        self.graph_api = graph_api
        self.id = user_object["id"]
        self.user_name = user_object["username"]
        self.first_name = user_object["first_name"]
        self.last_name = user_object["last_name"]
        self.gender = user_object["gender"]

    
    def getId(self):
        return self.id

    def getUsername(self):
        return self.user_name

    def getFirstName(self):
        return self.first_name

    def getLastName(self):
        return self.last_name

    def getGender(self):
        return self.gender

    def getAlbums(self):
        albums_objects = self.graph_api.get_connections(self.id, "albums")["data"]
        albums_list = []

        for album_object in albums_objects:
            album = FacebookAlbum(self.graph_api, album_object)
            albums_list = albums_list + [album]

        return albums_list

class FacebookAlbum(AbstractAlbum):

    graph_api = None

    def __init__(self, graph_api,  album_object):
        self.graph_api = graph_api
        self.name = album_object["name"]
        self.description = album_object["name"]
        self.updated_date = album_object["updated_time"]
        self.created_date = album_object["created_time"]
        print album_object
        pass
    
    def getName(self):
        return self.name

    def getDescription(self):
        return self.description

    def getCreatedDate(self):
        return self.created_date

    def getUpdatedDate(self):
        return self.updated_date

    def getPictures(self):
        pass

print "Registering facebook adapter"
registerAdapter("http://facebook.com", FacebookAdapter)