from django.urls import path
from quality_control import views


app_name = 'quality_control'

urlpatterns = [
    # path('', views.index, name='index'),
    path('', views.IndexView.as_view(), name='index'),
    # path('bugs/', views.bugs_list, name='bug_list'),
    path('bugs/', views.BugsListView.as_view(), name='bug_list'),
    # path('bugs/<int:bug_id>/', views.bug_detail, name='bug_detail'),
    path('bugs/<int:bug_id>/', views.BugDetailView.as_view(), name='bug_detail'),
    # path('bug/new/', views.create_bug_report, name='create_bug_report'),
    path('bug/new/', views.BugReportCreateView.as_view(), name='create_bug_report'),
    # path('bug/<int:bug_id>/update/', views.update_bug_report, name='update_bug'),
    path('bug/<int:bug_id>/update/', views.BugReportUpdateView.as_view(), name='update_bug'),
    # path('bug/<int:bug_id>/delete/', views.delete_bug_report, name='delete_bug'),
    path('bug/<int:bug_id>/delete/', views.BugReportDeleteView.as_view(), name='delete_bug'),
    # path('features/', views.features_list, name='feature_list'),
    path('features/', views.FeaturesListView.as_view(), name='feature_list'),
    # path('features/<int:feature_id>/', views.feature_detail, name='feature_detail'),
    path('features/<int:feature_id>/', views.FeatureDetailView.as_view(), name='feature_detail'),
    # path('feature/new/', views.create_feature_request, name='create_feature_request'),
    path('feature/new/', views.FeatureRequestCreateView.as_view(), name='create_feature_request'),
    # path('feature/<int:feature_id>/update/', views.update_feature_request, name='update_feature'),
    path('feature/<int:feature_id>/update/', views.FeatureRequestUpdateView.as_view(), name='update_feature'),
    # path('feature/<int:feature_id>/delete/', views.delete_feature_request, name='delete_feature'),
    path('feature/<int:feature_id>/delete/', views.FeatureRequestDeleteView.as_view(), name='delete_feature')
]