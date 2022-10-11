from accounts.models import Profile
from django.db import models


class Friend(models.Model):

    ACCEPTED = 'A'
    PENDING = 'P'
    DENIED = 'D'

    STATUS_CHOICES = [
        (ACCEPTED, 'Accepted'),
        (PENDING, 'Pending'),
        (DENIED, 'Denied'),
    ]


    id_requester = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='requester')
    id_receiver = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='receiver')
    request_date = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, default=PENDING)

    def __str__(self) -> str:
        return f'{self.id_requester.surname} - {self.id_receiver.surname}'
    

