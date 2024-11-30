from django.db import models


class ServiceRequest(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('in_progress', 'In Progress'),
        ('completed', 'Completed'),
    ]

    customer_name = models.CharField(max_length=100)
    customer_email = models.EmailField()
    request_description = models.TextField()
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='pending',
    )
    date_submitted = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Request by {self.customer_name} ({self.status})"
