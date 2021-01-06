from django.db import models
# from jsonfield import JSONField


class User(models.Model):
    GENDER =(
        ('male','male'),
        ('female','female')
        )
    name = models.CharField(max_length=200,null=True)
    phone = models.CharField(max_length=200,null=True)
    email = models.CharField(max_length=200,null=True)
    data_created = models.DateTimeField(auto_now_add=True,null=True)
    birth_date = models.DateTimeField(null=True)
    gender = models.CharField(max_length=200,null=True,choices=GENDER)
    def __str__(self):
        return self.name
class  Patient(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # medical_history=
    def __str__(self):
        return self.user.name

class Clinic(models.Model):
    name = models.CharField(max_length=200,null=True)
    # rating = models.DecimalField(3, 2)
    address = models.CharField(max_length=200,null=True)
    def __str__(self):
        return self.name

class Doctor(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    clinic = models.ForeignKey(Clinic, on_delete=models.CASCADE)
    specialization = models.CharField(max_length=50)
    rating = models.FloatField(null=True)
    fees =  models.IntegerField(null=True)
    # time_slots = JSONField()
    description = models.CharField(max_length=1024)
    
    def __str__(self):
        return self.user.name

class Appointment(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    doctor=  models.ForeignKey(Doctor, on_delete=models.CASCADE)
    time_slot = models.DateTimeField(null=True)
    review = models.CharField(max_length=1024)
    
class Payment(models.Model):
    key = models.CharField(max_length=250)
    amount = models.IntegerField(null=True)
    appointment = models.ForeignKey(Appointment, on_delete=models.CASCADE)
    



