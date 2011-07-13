#!/usr/bin/python

from metasocial.core.metanetwork import MetaNetwork

print "Trying to connect to facebook"

access_token = raw_input("Enter access token: ")
network = MetaNetwork("http://facebook.com", {"access_token" : access_token})
me = network.getAuthorizedPerson()

print "Username  : " + me.getUsername()
print "First Name: " + me.getFirstName()
print "Last Name : " + me.getLastName()
print "ID        : " + me.getId()