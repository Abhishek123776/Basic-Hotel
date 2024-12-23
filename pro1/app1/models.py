from django.db import models

# Create your models here.
class Room(models.Model):
    room_number = models.CharField(max_length=20, unique=True)
    room_type = models.CharField( max_length=10)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.room_type} - {self.room_number}"


class Booking(models.Model):
    room = models.ForeignKey(Room,on_delete=models.CASCADE)
    user_id = models.IntegerField() 
    check_in_date = models.DateField()
    check_out_date = models.DateField()
