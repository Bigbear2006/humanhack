from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomePageView.as_view(), name='home'),
    path('tests/', views.TestListView.as_view(), name='tests'),
    path('test/<int:pk>/', views.TestDetailView.as_view(), name='test_detail'),
    path('training/<int:pk>/', views.TrainingWayDetailView.as_view(), name='train_way_detail'),
    path('create/', views.FormCreateView.as_view(), name='create'),
]
