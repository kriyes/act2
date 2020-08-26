from django.contrib import admin
from django.urls import path
from .  import views   #new
from .views import EventListView,EventDetailView,JobListView,JobDetailView,BlogDetailView,BlogListView,TalentDetailView,TalentListView


urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('tc/', views.tc, name='tc'),
    path('pp/', views.pp, name='pp'),
    path('rp/', views.rp, name='rp'),
    path('blog/', BlogListView.as_view(), name='bloglistview'),
    path('blog/<int:pk>', BlogDetailView.as_view(), name='blogdetailview'),
    path('talent/<int:pk>', TalentDetailView.as_view(), name='talentdetailview'),
    path('talent/', TalentListView.as_view(), name='talentListview'),
    path('job/', JobListView.as_view(), name='joblistview'),
    path('job/<int:pk>', JobDetailView.as_view(), name='jobdetailview'),
    path('event/', EventListView.as_view(), name='eventlistview'),
    path('event/<int:pk>', EventDetailView.as_view(), name='eventdetailview'),


]