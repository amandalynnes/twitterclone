"""twitterclone URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from twitteruser import views
from tweet import views as tweetview
from authentication import views as authview
from notification import views as notview

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index_view, name='home'),
    path('accounts/login/', authview.login_view, name='login'),
    # path('addtweet/', views.add_tweet, name='add_tweet'),
    # path('tweet/<int:tweet_id>/', views.tweet_view, name='ticket'),
    # path('tweet/edit/<int:tweet_id>/', views.tweet_edit, name='edit_tweet'),
    # path('author/edit/<int:author_id>/', views.author_edit, name='edit_author'),
    # path('author/<int:author_id>/', views.author_view, name='author_view'),

]
