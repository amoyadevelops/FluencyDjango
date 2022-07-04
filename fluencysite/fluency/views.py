from django.shortcuts import render
from django.http import HttpResponse
from .models import VocabList, Item
# Create your views here.
def index(response, categoryname):
    list = VocabList.objects.get(categoryname=categoryname)
    items = list.item_set.get(id=1)
    return render(response, 'fluency/Fluency.html',{}) #HttpResponse("<h1> %s </h1> <br></br> <br></br> <p>%s</p>" % (list.categoryname, str(Item.text)))
def home(response):
    return render(response, 'fluency/home.html',{})
def flashcard(response):
    return HttpResponse('<h1> flashcard <h1>')