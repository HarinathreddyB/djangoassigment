
from django import forms
g=[['MALE','male'],('FEMALE','female')]
c=[['PYTHON','python'],['DJANGO','django']]
class NameForm(forms.Form):
    name=forms.CharField(max_length=100)
    age=forms.IntegerField()
    
    email=forms.EmailField(max_length=30)
    password=forms.CharField(max_length=100,widget=forms.PasswordInput)
    number=forms.IntegerField(max_value=100,min_value=25,required=False)
    date=forms.DateField()
    #gender=forms.ChoiceField(choices=g)
    gender=forms.ChoiceField(choices=g,widget=forms.RadioSelect)
   



class TopicForm(forms.Form):
    topic=forms.CharField(max_length=100)
    date=forms.DateField()











