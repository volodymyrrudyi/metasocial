from  abstract_adapter import (AbstractAdapter,
                               AbstractPerson)
from factory import registerAdapter
from twitter import Api as TwitterAPI

class TwitterAdapter(AbstractAdapter):
    """
    Twitter adapter class. Inherits AbstractAdapter
    """

    """
    Access token that is used to retrieve information from twitter
    """
    twitter_api    = None
    """
    Twitter Api object
    """

    def __init__(self, params):
        self.access_token_key       = params["access_token_key"]
        self.access_token_secret    = params["access_token_secret"]
        self.consumer_key           = params["consumer_key"]
        self.consumer_secret        = params["consumer_secret"]
        self.twitter_api            = TwitterAPI(self.consumer_key, self.consumer_secret,
                                                 self.access_token_key, self.access_token_secret)

    def getAuthorizedPerson(self):
        user_object = self.twitter_api.VerifyCredentials()
        return TwitterPerson(user_object)

    def getPerson(self, person_id):
        """
        Get instance of Person class which represents network user with specified id
            :param person_id: Identifier of the user
        """
        user_object = self.twitter_api.GetUser(person_id)
        return TwitterPerson(user_object)

    def getServiceName(self):
        """
        Get name of the social network
        """
        return "Twitter Social Network"

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


class TwitterPerson(AbstractPerson):
    """
    Implementation of Person class for twitter adapter
    """
    def __init__(self, user_object):
        print user_object.__str__()

        self.id         = str(user_object.GetId())
        self.user_name  = user_object.GetScreenName()
        self.first_name = user_object.GetName()
        self.last_name  = user_object.GetName()
        self.gender     = None


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


print "Registering twitter adapter"
registerAdapter("http://twitter.com", TwitterAdapter)