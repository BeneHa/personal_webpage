from django.contrib import admin

# Register your models here.
from homepage.models import BusinessItem, PrivateItem, ContactItem, SkillItem, PrivatePicture

admin.site.register(BusinessItem)
admin.site.register(PrivateItem)
admin.site.register(PrivatePicture)
admin.site.register(ContactItem)
admin.site.register(SkillItem)