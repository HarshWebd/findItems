from django.db import models

# Create your models here.
class findItem(models.Model):
    id = models.AutoField(primary_key=True)
    Image = models.ImageField( upload_to="img/")
    Name = models.CharField(max_length=70)
    Price = models.CharField(max_length=70)
    Place = models.TextField(blank=True)

    def __str__(self) -> str:
        return self.Name