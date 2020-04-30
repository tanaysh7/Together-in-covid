from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponse,HttpResponseRedirect
from django import forms
from django.template import RequestContext


# Create your views here.
class HomePageView(TemplateView):
    def get(self, request, **kwargs):
        return render(request, 'index.html', context=None)

class DetailsForm(forms.Form):
    
    firstname = forms.CharField(label='firstname', max_length=100)
    lastname =forms.CharField(label='lastname', max_length=100)
    phone=forms.CharField(label='phone', max_length=20)
    country=forms.CharField(label='country', max_length=100)
    category=forms.CharField(label='category', max_length=100)


 
class ThanksPageView(TemplateView):
    def getthanks(request, **kwargs):
        if request.method == 'POST':
            form = DetailsForm(request.POST)
            # check whether it's valid:
            if form.is_valid():
                # process the data in form.cleaned_data as required
                # ...
                # redirect to a new URL:
                
                #call function with body

               
                return render(request,'thanks.html',context={'firstname':request.POST['firstname']})
            else:
                render(request, 'index.html', context=None)
            
        else:
            return render(request, 'index.html', context=None)


class Volunteers(TemplateView):
    def getVolunteers(request):
        name='Test'
        return HttpResponse('{ "name":"' + name + '", "phone":+1 999 999 9999, "country":"USA" }')


