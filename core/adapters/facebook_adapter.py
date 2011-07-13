
from facebook import
from  abstract_adapter import AbstractAdapter

class FacebookAdapter(AbstractAdapter):

    access_token = ""
    graph_api    = None

    def __init__(self, params):

        if "access_token" in params:
            self.access_token = params["access_token"]
            self.graph_api = facebook
        else:
            raise LookupError("access_token key was not found in parameter dictionary")
        pass

    def getAuthorizedPerson(self):
        """
        Get instance of Person class that represents authorized user of the network
        """
        pass

    def getPerson(self, person_id):
        """
        Get instance of Person class which represents network user with specified id
            :param person_id: Identifier of the user
        """
        pass


    def getServiceName(self):
        """
        Get name of the social network
        """
        pass

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

