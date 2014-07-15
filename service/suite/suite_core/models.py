from django.db import models

    
#Rooms list - conf
class RoomAvailable (models.Model):
    number = models.CharField (max_length = 10)
    room_type = models.CharField (max_length = 100)

    def __str__(self):
        return self.number

#Services list
class Service (models.Model):
    name = models.CharField (max_length = 100)

    def __str__(self):
        return self.name
    
#Pricelist
class PriceList (models.Model):
    name = models.CharField (max_length = 100)
    date_start = models.DateField ()
    date_end = models.DateField ()
    price = models.DecimalField (max_digits = 10, decimal_places = 2)
    service = models.ForeignKey (Service)

#Modifiers list
class Modifier (models.Model):
    name = models.CharField (max_length = 200)
    perc = models.BooleanField ()
    amount = models.DecimalField (max_digits = 10, decimal_places = 2)

class Customer (models.Model):
    name = models.CharField (max_length = 200)
    surname = models.CharField (max_length = 200)

class Contact (models.Model):
    customer = models.ForeignKey (Customer)
    contact_type = models.CharField (max_length = 100)
    contact = models.CharField (max_length = 500)

class Reservation (models.Model):
    customer = models.ForeignKey (Customer)
    date_res = models.DateField ()
    note = models.TextField ()

class Room (models.Model):
    room = models.ForeignKey (RoomAvailable)
    date_arr = models.DateField ()
    date_dep = models.DateField ()

class Occupancy (models.Model):
    number = models.IntegerField ()
    date_arr = models.DateField ()
    date_dep = models.DateField ()
    service = models.ForeignKey (Service)
    pricelist = models.ForeignKey (PriceList)
    modifier = models.ForeignKey (Modifier)
