from django.urls import path
from . import views 


app_name = 'blog'
urlpatterns = [
    # post views
    # path('', views.post_list, name='post_list'),
    path('blog/', views.PostListView.as_view(), name='post_list'),
    path('blog/<slug:post>/',
         views.post_detail,
         name='post_detail'),
    path('about/', views.AboutPageView.as_view(), name='about'),
    path('', views.HomePageView, name='home'),
] 
