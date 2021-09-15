from django.db import models

class Profile(models.Model):
    patientName = models.CharField(max_length=255)
    age = models.CharField(max_length=3)
    admissionTime = models.DateTimeField(auto_now_add=True)
    contactNumber = models.CharField(max_length=10)

    def __str__(self):
        return self.patientName

class Record(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    temperature = models.FloatField(default=0)
    spo2 = models.FloatField(default=0)
    hbpm = models.IntegerField(default=0)
    timeStamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.profile.patientName
