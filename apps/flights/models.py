from django.db import models


class Airport(models.Model):
    id = models.CharField(max_length=50, primary_key=True)


class Airline(models.Model):
    id = models.CharField(max_length=50, primary_key=True)
    name = models.CharField(max_length=50)


class Leg(models.Model):
    id = models.CharField(max_length=50, primary_key=True)
    departure_time = models.DateTimeField()
    arrival_time = models.DateTimeField()
    stops = models.IntegerField()
    duration_mins = models.FloatField()
    departure_airport = models.OneToOneField(
        Airport,
        on_delete=models.CASCADE,
        related_name="departure_airport",
    )
    arrival_airport = models.OneToOneField(
        Airport,
        on_delete=models.CASCADE,
        related_name="arrival_airport",
    )
    airline_id = models.OneToOneField(
        Airline,
        on_delete=models.CASCADE,
        related_name="airline_id",
    )


class Agent(models.Model):
    id = models.CharField(max_length=50, primary_key=True)
    agent_rating = models.FloatField()


class Itinerary(models.Model):
    id = models.CharField(max_length=50, primary_key=True)
    price = models.FloatField()
    first_leg = models.OneToOneField(
        Leg,
        on_delete=models.CASCADE,
        related_name="first_leg",
    )
    second_leg = models.OneToOneField(
        Leg,
        on_delete=models.CASCADE,
        related_name="second_leg",
    )
    agent_id = models.OneToOneField(
        Agent,
        on_delete=models.CASCADE,
        related_name="agent_id",
    )
