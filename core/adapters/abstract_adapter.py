from abc import ABCMeta, abstractproperty, abstractmethod

class AbstractAdapter(object):
    """
    Abstract class for all social network adapters which declares all necessary methods
    """
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
    """
    Abstract class that represents user of abstract social network
    """
    __metaclass__ = ABCMeta

    @abstractmethod
    def getId(self):
        """
        Returns id of the user
        """

    @abstractmethod
    def getUsername(self):
        """
        Returns username of the user
        """

    @abstractmethod
    def getFirstName(self):
        """
        Returns first name of the user
        """

    @abstractmethod
    def getLastName(self):
        """
        Returns last name of the user
        """

    @abstractmethod
    def getGender(self):
        """
        Returns gender of the user
        """

    def getAlbums(self):
        """
        Returns list of the user`s album
        """

class AbstractAlbum(object):
    __metaclass__ = ABCMeta

    def getName(self):
        """
        Returns name of the album
        """

    def getDescription(self):
        """
        Returns description of the album
        """

    def getCreatedDate(self):
        """
        Returns date on which album was created
        """

    def getUpdatedDate(self):
        """
        Returns date on which last changes to album were made
        """

    def getPictures(self):
        """
        Returns list of pictures of album
        """