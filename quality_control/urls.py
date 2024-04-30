from django.urls import path
from quality_control import views


app_name = 'quality_control'

urlpatterns = [
    # path('', views.index, name='index'),
    path('', views.IndexView.as_view(), name='index'),
    path('bugs/', views.bugs_list, name='bug_list'),
    path('bugs/<int:bug_id>/', views.BugDetailView.as_view(), name='bug_detail'),
    path('features/', views.features_list, name='feature_list'),
    path('features/<int:feature_id>/', views.FeatureDetailView.as_view(), name='feature_detail')
]