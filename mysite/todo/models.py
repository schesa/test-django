from django.db import models

# Create your models here.
class Todo(models.Model):
    text = models.TextField()
    completed = models.BooleanField(default=False)
    priority = models.CharField(
        choices=(
            ('HIGH', 'High'),
            ('MEDIUM', 'Medium'),
            ('LOW', 'Low'),
        ),
        default='LOW',
        max_length=50
    )
    due_date = models.DateField(null=True)