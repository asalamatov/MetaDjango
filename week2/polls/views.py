from django.shortcuts import render
from django.http import HttpResponse, HttpResponsePermanentRedirect
from django.urls import reverse

# Create your views here.

# def index(request):
#     return  HttpResponse("Hello World")

# def home(request):
#     path = request.path
#     response = HttpResponse("This works")
#     return response

# def home(request):
#     path = request.path
#     scheme = request.scheme
#     method = request.method
#     address = request.META['REMOTE_ADDR']
#     user_agent = request.META['HTTP_USER_AGENT']
#     path_info = request.path_info

#     response = HttpResponse()
#     response.headers["Age"] = 20

#     msg = f"""<br>
#         <br>Path: {path}
#         <br>Address: {address}
#         <br>Scheme: {scheme}
#         <br>Method: {method}
#         <br>User Agent: {user_agent}
#         <br>Path info: {path_info}
#         <br>Age: {response.headers}

#     """
#     return HttpResponse(msg, content_type = "text/html", charset="utf-8")


# def showform(request):
#     return render(request, './form.html')

# def getform(request):
#     if request.method == "POST":
#         id = request.POST['id']
#         name = request.POST['name']
#     return HttpResponse('Name: {} UserID: {}'.format(name, id))

# def menuitems(request, dish):
#     items = {
#         'pasta': "makaron tamaq",
#         'falafel': "arapca tamaq",
#         'cheesecake': "Syr menen tort",
#     }

#     description = items[dish]

#     return HttpResponse(f'<h2>{dish}</h2>' + description)

# def display_menu_item(request)

# def index(request):
#     # return HttpResponse('index')
#     return HttpResponsePermanentRedirect(reverse('polls:login'))

# def login(request):
#     return HttpResponse("login")

from .forms import LogForm, BookingForm

def form_view(request):
    form = LogForm()
    if request.method == "POST":
        form = LogForm(request.POST)
        if form.is_valid():
            form.save()
    context = {'form':form}
    return render(request, "home.html", context)

def booking_view(request):
    form = BookingForm()
    if request.method == "POST":
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
    context = {'form': form}
    return render(request, 'home.html', context)