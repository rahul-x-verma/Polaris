# Polaris
##A Directions App for Bear Transit and the Night Safety Shuttle. 

This application aims to give Berkeley students a user friendly guide for unversity-owned transit services, similar to what Google Maps's public transportation does for transit agencies that serve the general public.

The heart of this application is a database containing information about each time a bus
operated by Bear Transit or the Night Safety Shuttle stops somewhere. Finding a
path between two points involves creating a graph data structure from this
database and using Breadth-First Search. The user interface is managed by Flask, with Twitter Bootstrap powering the front end.

This application has been deployed on Heroku and can be found at https://berkeley-polaris.herokuapp.com/
