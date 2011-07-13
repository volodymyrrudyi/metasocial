"""
Module with high-level api to access different social networks
"""
from adapters.factory import createAdapter
from adapters.abstract_adapter import AbstractAdapter


class MetaNetwork(object):
    """
    MetaNetwork class is a common interface that should be used to retrieve data from social
    networks.
    """

    impl = None
    """
    Reference to adapter that is used to communicate with network. Must inherit AbstractAdapter
    """

    def __init__(self, service_url, service_params):
        """
        Constructor receives two parameters which define what kind of network user wants to work with.
        :param service_type: Url of the service that will be accessed
        :param service_params: Parameters that needed to access service data, e.g. access tokens
        """
        self.impl = createAdapter(service_url, service_params)

    def getAuthorizedPerson(self):
        """
        Get instance of Person class that represents authorized user of the network
        """
        return self.impl.getAuthorizedPerson()

    def getPerson(self, person_id):
        """
        Get instance of Person class which represents network user with specified id
            :param person_id: Identifier of the user
        """
        return self.impl.getPerson(person_id)

    def getServiceName(self):
        """
        Get name of the social network
        """
        return self.impl.getServiceName()

    def getServiceDescription(self):
        """
        Get description of the social network
        """
        return self.impl.getServiceDescription()

    def getServiceUrl(self):
        """
        Get URL to social network website
        """
        return self.impl.getServiceUrl()

