from django.shortcuts import render
from notification.models import Notification

# Create your views here.


def notification(request, user_id):
    notifications = Notification.objects.filter(recipient=request.user)

    def delete_notifications():
        notifications.delete()
        return ''


    return render(request, 'notifications.html', {
        'heading': 'Notify Me!',
        'notifications': notifications,
        'delete': delete_notifications,

    })




