from facebook import GraphAPI

from  abstract_adapter import (AbstractAdapter,
                               AbstractPerson)

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
        """
        Get instance of Person class that represents authorized user of the network
        """
        user_object = self.graph_api.get_object("me")
        return FacebookPerson(user_object)

    def getPerson(self, person_id):
        """
        Get instance of Person class which represents network user with specified id
            :param person_id: Identifier of the user
        """
        user_object = self.graph_api.get_object(person_id)
        return FacebookPerson(user_object)

    def getServiceName(self):
        """
        Get name of the social network
        """
        return "Facebook Social Network"

    def getServiceDescription(self):
        """
        Get description of the social network
        """
        pass

    def getServiceUrl(self):
        """
        Get URL to social network website
        """
        pass


class FacebookPerson(AbstractPerson):
    def __init__(self, user_object):
        print user_object.__str__()

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


print "Registering facebook adapter"
registerAdapter("http://facebook.com", FacebookAdapter)