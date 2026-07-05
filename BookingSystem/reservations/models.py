from django.db import models
from django.contrib.auth.models import User

class Room(models.Model):
    ROOM_TYPES = [
        ("conference", "Conference room"),
        ("office", "Office"),
        ("meeting room", "Meeting room"),
    ]
    name = models.CharField(max_length=200)
    room_type = models.CharField(max_length=20, choices=ROOM_TYPES)
    capacity = models.IntegerField()
    price_per_hour = models.DecimalField(max_digits=8, decimal_places=2)
    description = models.TextField()


class Booking(models.Model):
    STATUS_CHOICES = [
        ("pending", "Pending"),
        ("comfirmed", "Comfirmed"),
        ("cancelled", "Cancelled"),
    ]  # Додали кому для синтаксису
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    start_time = models.DateTimeField()
    end_time = models.CharField(max_length=20, choices=STATUS_CHOICES, default="pending")
    created_at = models.DateTimeField(auto_now_add=True)


def is_room_available(room, start, end):
    return not Booking.objects.filter(
        room=room,
        start_time__lt=end,
        end_time=start,  # Твоє поле називається end_time, тому замість status__in звертаємось до нього
    ).exists()