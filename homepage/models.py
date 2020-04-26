from django.db import models


# Create your models here.
class BusinessItem(models.Model):
    company_name = models.TextField()
    position = models.TextField()
    detailed_description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()
    picture = models.ImageField(upload_to="business_pictures")
    current_flag = models.BooleanField()


    def __str__(self):
        return "BusinessItem " + self.position + " at " + self.company_name


class PrivateItem(models.Model):
    name = models.TextField()
    description = models.TextField()

    def __str__(self):
        return "PrivateItem " + self.name


class PrivatePicture(models.Model):
    name = models.TextField()
    picture = models.ImageField(upload_to="private_pictures")
    private_item = models.ForeignKey("PrivateItem", on_delete=models.CASCADE, related_name="picture")

    def __str__(self):
        return "Picture related to " + str(self.private_item)

class ContactItem(models.Model):
    name = models.TextField()
    link = models.TextField()
    picture = models.ImageField(upload_to="contact_pictures")

    def __str__(self):
        return ("ContactItem " + self.name)


class SkillItem(models.Model):
    name = models.TextField()
    description = models.TextField()
    picture = models.ImageField(upload_to="skill_pictures")

    def __str__(self):
        return "SkillItem " + self.name