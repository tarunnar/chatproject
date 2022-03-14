from django.db import models
from django.utils import timezone
from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer


# Create your models here.
class Notification(models.Model):
    notification = models.TextField()
    is_sent = models.BooleanField(default=True)
    created_at = models.DateTimeField(default=timezone.now())

    def save(self, *args, **kwargs):
        channel_layer = get_channel_layer()
        async_to_sync(channel_layer.group_send)(
            "chat_room", {
                "type": "send_notification",
                "data": {
                    "notification": self.notification,
                    "is_sent": self.is_sent,
                    "created_at": self.created_at.strftime("%Y-%m-%d %H:%M:%S")
                }
            }
        )
        super(Notification, self).save()
