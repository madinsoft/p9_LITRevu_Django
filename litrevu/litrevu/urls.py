"""
URL configuration for litrevu project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
#from litreview_app import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
import litreview_app.views
import authentication.views

urlpatterns = [
    path('admin/', admin.site.urls),
    #path('homepage/', litreview_app.views.homepage),
    path('registration/', litreview_app.views.registration, name='registration'),
    path('flow/', litreview_app.views.flow, name='home'),
    #path('ticket_create/', litreview_app.views.ticket_create),
    #path('review_create/', litreview_app.views.review_create),
    #path('review_ticket_create/', litreview_app.views.review_ticket_create),
    path('your_posts/', litreview_app.views.your_posts, name='your_posts'),
    #path('review_update/', litreview_app.views.review_update),
    #path('ticket_update/', litreview_app.views.ticket_update),
    path('subscriptions/', litreview_app.views.subscriptions, name='subscriptions'),
    #path('user_update/', litreview_app.views.user_update),
    path('', authentication.views.login_page, name = 'login'),
    path('logout/', authentication.views.logout_user, name='logout'),
    path('signup/', authentication.views.signup_page, name='signup'),
]

urlpatterns += staticfiles_urlpatterns()
