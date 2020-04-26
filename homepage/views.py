from django.shortcuts import render, redirect
from homepage.models import BusinessItem, PrivateItem, ContactItem, SkillItem

# Create your views here.

def redirect_to_index(request):
    return redirect("home_page")

def contact_page(request):
    all_contact_items = ContactItem.objects.all()
    return render(request, "contact_page.html", {"contact_items": all_contact_items})

def index_page(request):
    return render(request, "home.html")

def business_page(request):
    all_business_items = BusinessItem.objects.all().extra(order_by=["-end_date"])
    return render(request, "business_page.html", {"items": all_business_items})

def private_page(request):
    all_private_items = PrivateItem.objects.all()
    print(all_private_items)
    return render(request, "private_page.html", {"items": all_private_items})

def skills_page(request):
    all_skill_items = SkillItem.objects.all()
    return render(request, "skills_page.html", {"items": all_skill_items})

def impressum_page(request):
    return render(request, "impressum_page.html")
