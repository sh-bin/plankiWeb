from django.urls import path, re_path
from . import views

app_name = 'plankiHomePage'

urlpatterns = [
    # Home page url
    path('', views.index, name='index'),

    # Contact page url
    path('contacts/', views.contacts, name='contacts'),

    # Privacy url
    path('privacy/', views.privacy, name='privacy'),

    # Terms url
    path('terms/', views.terms, name='terms'),

    # Feedback url
    path('feedback/', views.feedback, name='feedback'),

    # Products urls
    path('slats/<slug:slug_id>/', views.slats, name='slats'),

    # Detail product url
    path('detail_slats/<slug:slug_id>', views.detail_slats, name='detail_slats'),

    # Authorization
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('change_password/', views.change_password, name='change_password'),

    # Settings
    path('settings/', views.settings, name='settings'),

    # Search
    path('search/', views.search, name='search'),

    #Cart
    path('cart/', views.cart, name='cart'),

    #Send data
    path('sendCart/', views.sendCart, name='sendCart')

]
