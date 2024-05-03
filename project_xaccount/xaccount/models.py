from django.db import models

# Create your models here.
class BusinessType (models.Model):
    classification = models.CharField(max_length=30)

class Address(models.Model):
    address1 = models.CharField(max_length=120)
    address2 = models.CharField(max_length=120, blank=True, null=True)
    address3 = models.CharField(max_length=120, blank=True, null=True)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    postal_code = models.CharField(max_length=20)
    lastupdate = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.address1}, {self.city}, {self.state}, {self.country}, {self.postal_code}"

class Person(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    middle_name = models.CharField(max_length=100, blank=True, null=True)
    email1 = models.EmailField(blank=True, null=True)
    email2 = models.EmailField(blank=True, null=True)
    phone1 = models.CharField(max_length=20)
    phone2 = models.CharField(max_length=20, blank=True, null=True)
    phone3 = models.CharField(max_length=20, blank=True, null=True)
    address = models.ForeignKey(Address, on_delete=models.CASCADE)
    lastupdate = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Business(models.Model):
    entity_name = models.CharField(max_length=250)
    business_type = models.ForeignKey(BusinessType, on_delete=models.CASCADE)
    fei_ein_number = models.CharField(max_length=20)
    date_filed = models.DateField()
    state = models.CharField(max_length=2)
    status_active = models.BooleanField(default=True)
    principal_address = models.ForeignKey(Address, related_name='principal_address', on_delete=models.CASCADE)
    mailing_address = models.ForeignKey(Address, related_name='mailing_address', on_delete=models.CASCADE)
    reqistered_agent = models.ForeignKey(Person, related_name='registered_agent', on_delete=models.CASCADE)
    registered_agent_address = models.ForeignKey(Address, related_name='registered_agent_address', on_delete=models.CASCADE)

    def __str__(self):
        return self.entity_name
