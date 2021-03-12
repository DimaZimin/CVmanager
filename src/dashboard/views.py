from django.http import JsonResponse
from django.shortcuts import render
from applications.models import Application
from chartjs.views.pie import HighChartPieView


def dashboard(request):
    applications = Application.objects.all()
    total_applications = applications.count()
    labels = Application.get_statuses()
    data = []
    for status in labels:
        counter = 0
        for application in applications:

            if application.get_status_display() == status:
                counter += 1
        data.append(counter)
    return render(
        request,
        'dashboard/index.html',
        context={
            'total_applications': total_applications,
            'zipper': zip(labels, data),
            'labels': labels,
            'data': data
        }
    )

