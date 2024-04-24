from django.db import models
from datetime import date

class Blood_stock(models.Model):
    bloodGroup = models.CharField(max_length=10)
    name = models.CharField(max_length=200)
    place = models.CharField(max_length = 200)
    hospital = models.CharField(max_length = 255,null=True)
    age = models.IntegerField(null=True)
    phone = models.IntegerField(null=True)
    date_uploaded = models.DateField(("Date"), default=date.today)
    hospital_num = models.IntegerField(null=True)
    hospital_add = models.CharField(max_length = 200,null=True)
    hospital_mail = models.EmailField(null=True)

    def __str__(self):
        return f"{self.bloodGroup} {self.name} {self.place} {self.age} {self.phone} {self.date_uploaded} {self.hospital} {self.hospital_num} {self.hospital_add} {self.hospital_mail}"


class BloodDonor_hospitals(models.Model):
    hos_name = models.CharField(max_length=100)
    hos_place = models.CharField(max_length=255)
    posted_date = models.DateField(("Date"),default=date.today)
    hos_contact = models.IntegerField(null=True)
    hos_mail = models.EmailField(null=True)
    blood_need = models.CharField(max_length = 10)

    def __str__(self):
        return f"{self.hos_name} {self.hos_place} {self.posted_date} {self.hos_contact} {self.blood_need} {self.hos_mail}"
    

class BloodDonor_organisation(models.Model):
    org_name = models.CharField(max_length=50)
    org_place = models.CharField(max_length=50)
    posted_date = models.DateField(("Date"),default=date.today)
    org_contact = models.IntegerField(null=True)
    org_mail = models.EmailField(null=True)
    blood_need  = models.CharField(max_length = 10)

    def __str__(self):
        return f"{self.org_name} {self.org_place} {self.posted_date} {self.org_contact} {self.blood_need} {self.org_mail}"

class Admin_login(models.Model):
    admin_name = models.CharField(max_length = 50)
    admin_pass = models.CharField(max_length = 10)

    def __str__(self):
        return f"{self.admin_name} {self.admin_pass}"