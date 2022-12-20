from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from app.forms import *
from app.models import *
def djangoforms(request):
    NF=NameForm()
    d={'form':NF}
    if request.method=='POST':
        form_data=NameForm(request.POST)
        if form_data.is_valid():
            return HttpResponse(str(form_data.cleaned_data))
            n=form_data.cleaned_data['name']
            a=form_data.cleaned_data['age']
            g=form_data.cleaned_data['gender']
            m=form_data.cleaned_data['email']
            n=form_data.cleaned_data['number']
            d=form_data.cleaned_data['date']

            
            
            d1={'n':n,'a':a,'g':g,'m':m,'n':n}
            return render(request,'data.html',d1)
    return render(request,'djangoforms.html',d)

def insert_topic(request):
    TF=TopicForm()
    d={'form':TF}
    if request.method=='POST':
        form_data=TopicForm(request.POST)
        if form_data.is_valid():
            tn=form_data.cleaned_data['topic']
            dt=form_data.cleaned_data['date']
            T=Topic.objects.get_or_create(topic_name=tn,date=dt)[0]
            T.save()
            return HttpResponse('Inerted')
    return render(request,'insert_topic.html',d)











