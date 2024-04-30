from django.shortcuts import render
from django.views import View
from django.views.generic import DetailView
from .models import BugReport, FeatureRequest


def index(request):
    return render(request, 'quality_control/index.html')


class IndexView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'quality_control/index.html')


def bugs_list(request):
    bugs = BugReport.objects.all()
    return render(request, 'quality_control/bugs_list.html', {'bug_list': bugs})


class BugDetailView(DetailView):
    model = BugReport
    pk_url_kwarg = 'bug_id'
    template_name = 'quality_control/bug_detail.html'


def features_list(request):
    features = FeatureRequest.objects.all()
    return render(request, 'quality_control/features_list.html', {'feature_list': features})


class FeatureDetailView(DetailView):
    model = FeatureRequest
    pk_url_kwarg = 'feature_id'
    template_name = 'quality_control/feature_detail.html'