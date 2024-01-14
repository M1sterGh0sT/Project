from django.shortcuts import render, get_object_or_404, redirect
from app.models import *
from django.contrib.auth.models import auth
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .forms import *


def home(request):
    getSeriesName = SeriesName.objects.all()
    return render(request, 'pages/home.html', {
        'movieName': getSeriesName,
    })

def series(request):
    getSeriesName = SeriesName.objects.all()
    return render(request, 'pages/series.html', {
        'movieName': getSeriesName,
    })



def about(request):
    return render(request, 'pages/about.html')



def seriesChar(request):
    char = SeriesName.objects.all()

    return render(request, 'pages/seriesChar.html', {
        'movie': char,
    })
    



def index(request, pk):
    series_instance = get_object_or_404(SeriesName, pk=pk)

    character_info_list = series_instance.products.all()
    return render(request, 'pages/index.html', {
        'movieName': series_instance,
        'character': character_info_list,
    })


def details(request, pk):
    char = get_object_or_404(CharacterInfo, pk=pk)
    return render(request, 'pages/name.html', {
        'char': char,
    })


def serieasDetails(request, pk):
    series_instance = get_object_or_404(SeriesName, pk=pk)
    return render(request, 'pages/aboutSerias.html', {
        'info': series_instance,
    })
  






# login logout registration functions

def register(request):

    if request.method == 'POST':
        if request.POST['password1'] == request.POST['password2']:
            try:
                User.objects.get(username = request.POST['username'])
                return render(request,'userAuth/register.html', {
                    'error':'Username is already taken'
                })
            
            except User.DoesNotExist:
                user = User.objects.create_user(request.POST['username'],password=request.POST['password1'])
                auth.login(request,user)
                return redirect('app:login')
        else:
            return render (request,'userAuth/register.html', {
                'error':'Password does not match'
            })
        
    return render(request, 'userAuth/register.html')



def login(request):

    if request.method == 'POST':
        user = auth.authenticate(username=request.POST['username'], password = request.POST['password'])

        if user is not None:
            auth.login(request,user)
            return redirect('app:user')
        else:
            return render (request,'userAuth/login.html', {
                'error': 'Username or password is incorrect',
            })
        
    return render (request,'userAuth/login.html')
        


def logout(request):
    auth.logout(request)

    return redirect('app:login')







# user page

def user(request):
    user_series = UserSeries.objects.filter(user=request.user)
    return render(request, 'pages/user.html', {
        'content': user_series,
    })





    



# user forms


def userProjects(request):
    user_series = UserSeries.objects.filter(user=request.user)
    return render(request, 'creatingForms/userProjects.html', {
        'content': user_series,
    })




def userSeries(request):
    if request.method == "POST":
        create_name = request.POST.get('createName')
        about = request.POST.get('about')
        link = request.POST.get('link')
        image = request.FILES.get('image')

        series = UserSeries.objects.create(
            createName=create_name,
            about=about,
            link=link,
            image=image,
            user=request.user 
        )
        
        return redirect('app:userProjects')
    
    return render(request, 'creatingForms/createSeries.html')




def choice(request):
    char = UserSeries.objects.filter(user=request.user)
    return render(request, 'creatingForms/choiceSeries.html', {
        'char': char,
    })



def userIndex(request, pk):
    series_instance = get_object_or_404(UserSeries, pk=pk)

    character_info_list = series_instance.products.all()
    return render(request, 'creatingForms/userIndex.html', {
        'movieName': series_instance,
        'character': character_info_list,
    })


def userDetails(request, pk):
    char = get_object_or_404(UserCharacter, pk=pk)
    return render(request, 'pages/name.html', {
        'char': char,
    })



def userChar(request, pk):
    series = get_object_or_404(UserSeries, id=pk)

    if request.method == 'POST':
        name = request.POST.get('name')
        planet = request.POST.get('planet')
        quote = request.POST.get('quote')
        image = request.FILES.get('image')
        description = request.POST.get('description')
        character = UserCharacter.objects.create(
            seriesName=series,
            name=name,
            planet=planet,
            quote=quote, 
            image=image,
            description=description
        )
         
        return redirect('app:userProjects')

    return render(request, 'creatingForms/createChar.html', {
        'series': series
    })

        


def charDetails(request, pk):
    char = get_object_or_404(UserCharacter, pk=pk)
    return render(request, 'creatingForms/userCharName.html', {
        'char': char,
    })





def search_view(request):
    query = request.GET.get('query', '')

    if query:
        all_series = SeriesName.objects.filter(createName__icontains=query)
    else:
        all_series = SeriesName.objects.all()

    return render(request, 'pages/user.html', {
        'all_series': all_series, 
        'query': query
    })



