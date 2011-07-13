from abc import ABCMeta, abstractproperty, abstractmethod

class AbstractAdapter(object):
    __metaclass__ = ABCMeta


    @abstractmethod
    def getAuthorizedPerson(self):
        """
        Get instance of Person class that represents authorized user of the network
        """
        
    @abstractmethod
    def getPerson(self, person_id):
        """
        Get instance of Person class which represents network user with specified id
            :param person_id: Identifier of the user
        """

    @abstractmethod
    def getServiceName(self):
        """
        Get name of the social network
        """

    @abstractmethod
    def getServiceDescription(self):
        """
        Get description of the social network
        """

    @abstractmethod
    def getServiceUrl(self):
        """
        Get URL to social network website
        """


class AbstractPerson(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def getId(self):
        pass

    @abstractmethod
    def getUsername(self):
        pass

    @abstractmethod
    def getFirstName(self):
        pass

    @abstractmethod
    def getLastName(self):
        pass

    @abstractmethod
    def getGender(self):
        pass
