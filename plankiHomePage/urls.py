from django.urls import path, re_path
from .views import *

app_name = 'plankiHomePage'

urlpatterns = [
    # Home page url
    path('', index, name='index'),

    # Contact page url
    path('contacts/', contacts, name='contacts'),

    # Privacy url
    path('privacy/', privacy, name='privacy'),

    # Terms url
    path('terms/', terms, name='terms'),

    # Feedback url
    path('feedback/', feedback, name='feedback'),

    # Products urls
    path('sashes/', sashes, name='sashes'),
    path('jettons/', jettons, name='jettons'),
    path('slats/<slug:slug_id>/', slats, name='slats'),

    # Detail product url
    path('detail_slats/<slug:slug_id>', detail_slats, name='detail_slats'),
    path('detail_sashes/<slug:slug_id>', detail_sashes, name='detail_sashes'),
    path('detail_jettons/<slug:slug_id>', detail_jettons, name='detail_jettons'),

    # Authorization
    path('register/', register, name='register'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    path('change_password/', change_password, name='change_password'),

    # Settings
    path('settings/', settings, name='settings'),

    # Search
    path('search/', search, name='search'),

]
