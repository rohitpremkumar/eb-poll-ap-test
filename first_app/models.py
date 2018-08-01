from django.db import models

class LeaveMessage(models.Model):
    """A typical class defining a model, derived from the Model class."""

    # Fields
    name= models.CharField(max_length=20)
    email = models.EmailField(max_length=20)
    topic = models.CharField(max_length=20)
    message = models.TextField(max_length=1000)

    # Metadata
    class Meta:
        ordering = ['name']

    # Methods
    def get_absolute_url(self):
        """Returns the url to access a particular instance of MyModelName."""
        return reverse('leave-message', args=[str(self.id)])

    def __str__(self):
        """String for representing the MyModelName object (in Admin site etc.)."""
        return self.email