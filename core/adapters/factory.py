
__adapter_registry__ = {}

def createAdapter(service_url, service_params):
    """
    Creates adapter to work with specified service type and passes params to it
        :param service_url: url of the service to create adapter for
        :param service_params: dictionary of params that should be passed to adapter
    """

    if service_url in __adapter_registry__:
        global __adapter_registry__
        print "Constructing"
        adapter_class = __adapter_registry__[service_url]
        return adapter_class(service_params)
    else:
        return None


def registerAdapter(service_url, adapter):
    """
    Registers adapter to access network defined by service_url
    """
    print "Registering " + service_url
    global __adapter_registry__
    __adapter_registry__[service_url] = adapter