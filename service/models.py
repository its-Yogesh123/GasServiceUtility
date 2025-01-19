import uuid
from django.contrib.auth.models import User
from django.db import models
class ServiceRequest(models.Model):
    STATUS= [
        ('pending', 'Pending'),
        ('in_progress', 'In Progress..'),
        ('resolved', 'Resolved'),
    ]
    reference_id = models.UUIDField(default=uuid.uuid4, unique=True, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='service_requests')
    service_type = models.CharField(max_length=100)  # Example: 'Gas Leakage', 'Billing Issue'
    description = models.TextField()
    attached_file = models.FileField(upload_to='public/service_attachments/', blank=True, null=True)
    status = models.CharField(max_length=20, choices=STATUS, default='pending')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.reference_id} - {self.user.username}"