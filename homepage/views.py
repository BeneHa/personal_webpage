from django.shortcuts import render, redirect
from homepage.models import BusinessItem, PrivateItem, ContactItem, SkillItem
import requests
import json
import os

# Create your views here.

def send_tracking_data(page_name, request):
    #Get real client IP instead of Heroku-internal IP
    ip_address = request.get_host()
    print(ip_address)

    ipstack_api_key = os.environ["IPSTACK_API_KEY"]
    ip_information = requests.post(f"http://api.ipstack.com/{ip_address}?access_key={ipstack_api_key}")
    res = ip_information.json()

    payload = {
        "page_name": page_name,
        "browser_name": request.user_agent.browser.family,
        "browser_version": request.user_agent.browser.version_string,
        "os_name": request.user_agent.os.family,
        "os_version": request.user_agent.os.version_string,
        "device": request.user_agent.device.family,
        "ip_address": ip_address,
        "country_name": res["country_name"],
        "region_name": res["region_name"],
        "city": res["city"]
    }
    url = "https://bhaeuse-webpage-functions.azurewebsites.net/api/http_trigger_index_page"
    #url = "http://localhost:7071/api/http_trigger_index_page"

    requests.post(url, data = json.dumps(payload))


def redirect_to_index(request):
    return redirect("home_page")

def contact_page(request):
    send_tracking_data("contact", request)
    all_contact_items = ContactItem.objects.all()
    return render(request, "contact_page.html", {"contact_items": all_contact_items})

def index_page(request):
    send_tracking_data("home", request)
    return render(request, "home.html")

def business_page(request):
    send_tracking_data("business", request)
    all_business_items = BusinessItem.objects.all().extra(order_by=["-end_date"])
    return render(request, "business_page.html", {"items": all_business_items})

def private_page(request):
    send_tracking_data("private", request)
    all_private_items = PrivateItem.objects.all()
    print(all_private_items)
    return render(request, "private_page.html", {"items": all_private_items})

def skills_page(request):
    send_tracking_data("skills", request)
    all_skill_items = SkillItem.objects.all()
    return render(request, "skills_page.html", {"items": all_skill_items})

def impressum_page(request):
    send_tracking_data("impressum", request)
    return render(request, "impressum_page.html")
