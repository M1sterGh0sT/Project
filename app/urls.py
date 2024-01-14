from . import views
from django.urls import path 





app_name = 'app'
urlpatterns = [
    path('', views.login, name='login'),
    path('series/', views.series, name='series'),
    path('index/<int:pk>', views.index, name='index'),
    path('seriesCharacters/', views.seriesChar, name='seriesChar'),
    path('about/', views.about, name='about'),
    path('id/<int:pk>/', views.details, name='details'),
    path('serieasDetails/<int:pk>/', views.serieasDetails, name='serieasDetails'),
    path('user/', views.user, name='user'),

    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),

    # path('createSeries/', views.createSeries, name='createSeries'),
    # path('createChar/<int:pk>/', views.createChar, name='createChar'),
    path('choice/', views.choice, name='choice'),


    path('userProjects/', views.userProjects, name='userProjects'),
    path('userSeries/', views.userSeries, name='userSeries'),
    path('userChar/<int:pk>/', views.userChar, name='userChar'),
    path('userIndex/<int:pk>', views.userIndex, name='userIndex'),
    path('userDetails/<int:pk>/', views.userDetails, name='userDetails'),
    path('charDetails/<int:pk>/', views.charDetails, name='charDetails'),
    path('search_view/', views.search_view, name='search_view'),
]

