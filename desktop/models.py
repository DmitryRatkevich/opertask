from django.db import models
from django.core.exceptions import ValidationError
from users.models import User

class Task(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('in_progress', 'In Progress'),
        ('completed', 'Completed'),
        ('rejected', 'Rejected'),
    ]

    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    comment = models.TextField(max_length=180, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='tasks_created'
    )
    processed_by = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True, blank=True, related_name='tasks_processed'
    )

    def __str__(self):
        return f'Task {self.id} - {self.status}'

    def clean(self):
        """Ensure that only users with the correct roles can create or process tasks."""
        if self.created_by and self.created_by.role != 'store':
            raise ValidationError("The creator of the task must have the role 'store'.")
        if self.processed_by and self.processed_by.role != 'operator':
            raise ValidationError("The processor of the task must have the role 'operator'.")

    def assign_to_operator(self, operator):
        """Assign the task to an operator and change status to 'in_progress'."""
        if self.status != 'pending':
            raise ValidationError("Only tasks with 'pending' status can be assigned.")
        if operator.role != 'operator':
            raise ValidationError("Only users with the 'operator' role can process tasks.")
        self.processed_by = operator
        self.status = 'in_progress'
        self.save()

    def mark_as_completed(self):
        """Mark the task as completed."""
        if self.status != 'in_progress':
            raise ValidationError("Only tasks with 'in_progress' status can be completed.")
        self.status = 'completed'
        self.processed_by = None
        self.save()

    def mark_as_rejected(self):
        """Mark the task as rejected."""
        if self.status != 'in_progress':
            raise ValidationError("Only tasks with 'in_progress' status can be rejected.")
        self.status = 'rejected'
        self.processed_by = None
        self.save()

    def return_to_pending(self):
        """Return the task to pending status."""
        if self.status != 'in_progress':
            raise ValidationError("Only tasks with 'in_progress' status can be returned to pending.")
        self.status = 'pending'
        self.processed_by = None
        self.save()


class Photo(models.Model):
    """Model to store photos associated with a task."""
    task = models.ForeignKey(
        Task, on_delete=models.CASCADE, related_name='photos'
    )
    image = models.ImageField(upload_to='photos/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Photo {self.id} for Task {self.task.id}'
