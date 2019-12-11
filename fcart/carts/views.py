from django.shortcuts import render,redirect
from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as ureq
from carts.models import Redmi_Mobiles
import requests

# Create your views here.
def home_view(request):
    return render(request,'carts/home.html')

def scrape_view(request):
    session=requests.Session()
    my_url="https://www.flipkart.com/mobiles/pr?sid=tyy%2C4io&p%5B%5D=facets.brand%255B%255D%3DRealme&otracker=nmenu_sub_Electronics_0_Realme&sort=price_asc"
    uclient=session.get(my_url,verify=False).content
    page_soup=soup(uclient,"html.parser")
    containers=page_soup.findAll("div",{"class":"_3O0U0u"})
    for container in containers:
        product_name=container.div.img["alt"]
        price_container=container.findAll("div",{"class":"_1vC4OE _2rQ-NK"})
        price=(price_container[0].text)
        rating_container=container.findAll("div",{"class":"hGSR34"})
        rating=rating_container[0].text
        
        new_redmi=Redmi_Mobiles()
        new_redmi.model_name=product_name
        new_redmi.price=price
        new_redmi.rating=rating
        new_redmi.save()
        
    return redirect('home')