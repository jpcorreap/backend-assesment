from django.db import models


class Agent(models.Model):
    id = models.CharField(max_length=50, primary_key=True)
    agent_rating = models.DecimalField()


class Itinerary(models.Model):
    id = models.CharField(max_length=50, primary_key=True)
    agent_id = models.CharField(max_length=50) # TODO Add relation to Agent class
    price = models.DecimalField


class Airport(models.Model):
    id = models.CharField(max_length=50, primary_key=True)


class Airline(models.Model):
    id = models.CharField(max_length=50, primary_key=True)
    name = models.CharField(max_length=50)


class Leg(models.Model):
    id = models.CharField(max_length=50, primary_key=True)
    departure_airport = models.CharField(max_length=50) # TODO Add relation to Airport class
    arrival_airport = models.CharField(max_length=50) # TODO Add relation to Airport class
    airline_id = models.CharField(max_length=50) # TODO Add relation to Airline class
    departure_time = models.DateTimeField()
    arrival_time = models.DateTimeField()
    stops = models.IntegerField()
    duration_mins = models.DecimalField()
