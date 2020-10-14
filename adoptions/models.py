from django.db import models

# Model = Database Table
# Field = Database Coloumn
# Record = Database Row

class Pet(models.Model):
    SEX_CHOICES = [('M','Male'),('F','Female')]

    name = models.CharField(max_length=100)
    submitter = models.CharField(max_length=100)
    species = models.CharField(max_length=30)
    breed = models.CharField(max_length=100, blank=True)                                    # Since Breed can be Unknown
    description = models.TextField()                                                        # Since Description can be very long
    sex = models.CharField(max_length=1, blank=True, choices=SEX_CHOICES)                   # Since Sex can be Unknown
    submission_date = models.DateTimeField()
    age = models.IntegerField(null=True)                                                    # Since age can be less than Zero
    vaccinations = models.ManyToManyField('Vaccine', blank=True)                            # Since Applied Vaccines might not be known

class Vaccine(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

