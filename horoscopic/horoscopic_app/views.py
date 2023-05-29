from django.shortcuts import render
from django.views.generic.edit import FormView
from .forms import HoroscopeForm
import requests

# Create your views here.
class HoroscopeCreateView(FormView):
    template_name = "horoscopic/get_prediction.html"
    form_class = HoroscopeForm

    # handle the POST request
    def post(self, request):
        # 1) extract the `sign` from the form
        sign = request.POST.get('sign', '') # 
        # 2) and fetch the horoscope information from the API
        req = requests.get(f'https://ohmanda.com/api/horoscope/{sign}')
        # 3) store it in a context variable in your render function 
        context = req.json() # to get a dictionary from the requests library call
        print(context)
        

        context['form'] = HoroscopeForm()
        
        return render(request, 'horoscopic/get_prediction.html', context)