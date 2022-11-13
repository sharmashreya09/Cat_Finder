from django.shortcuts import render
from catapp.models import Contact

# Create your views here.
#fknMErSWmTFXyKOjNHzVLw==YfAXzk15UtN1MGiR
def home(request):
    return render(request,'home.html')

def contact(request):
    if request.method == 'POST':
         name=request.POST['name']
         email=request.POST['email']
         message=request.POST['message']
         contact= Contact.objects.create(name=name, email=email, message=message)

    return render(request,'contact.html')

def about(request):
    return render(request, 'about.html')


def cat(request):
    import json
    import requests
    if request.method == 'POST':
           name=request.POST['query']
           api_url = 'https://api.api-ninjas.com/v1/cats?name='
           api_request = requests.get(
               api_url + name, headers={'X-Api-Key': 'fknMErSWmTFXyKOjNHzVLw==YfAXzk15UtN1MGiR'})
           try:
               api = json.loads(api_request.content)
           except Exception as e:
               api = "oops! There was an error"
               print(e)
           return render(request, 'cat.html', {'api': api})
    else:
        return render(request, 'cat.html', {'query': 'Enter a valid query'})


