from django.db import models


class TODO(models.Model):
    STATUS_CODE=(
        ('P', 'In Progress'),
        ('C', 'Completed'),
        ('N', 'Pending')
    )
    title=models.CharField(max_length=80)
    descriptions=models.CharField(max_length=256)
    date_time=models.CharField(max_length=20)
    status_task=models.CharField(max_length=3, choices=STATUS_CODE)
    created_on=models.DateTimeField(auto_now_add=True)
    updated_on=models.DateTimeField(auto_now_add=True)
    
    