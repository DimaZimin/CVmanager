from django.contrib.auth.decorators import login_required
from django.db.models.query import QuerySet
from django.shortcuts import render
from applications.models import Application
from collections import Counter
import itertools


def application_statuses_data(labels, applications):
    data = []
    for status in labels:
        counter = 0
        for application in applications:
            if application.get_status_display() == status:
                counter += 1
        data.append(counter)
    return data


@login_required
def dashboard(request):
    # applications data
    applications = Application.objects.filter(user=request.user)
    applications_labels = Application.get_statuses()
    applications_data = application_statuses_data(applications_labels, applications)
    applications_percentage = [part / sum(applications_data) * 100 if sum(applications_data) != 0 else 0 for part in applications_data]
    total_applications = applications.count()
    technologies = [str(tech) for tech in itertools.chain(*[list(app.company.technologies.all()) for app in applications])]
    technologies_counted = Counter(technologies)
    locations = [app.company.location if app.company.location else 'Other' for app in applications]
    locations_counted = Counter(locations)
    locations_data = [number for number in locations_counted.values()]
    locations_percentage = [
        round(part/sum(list(locations_counted.values())) * 100, 2)
        for part in list(locations_counted.values())
    ]
    industries = [str(app.company.industry) for app in applications]
    industries_counted = Counter(industries)
    industries_percentage = [
        round(part/sum(list(industries_counted.values()))*100, 2)
        for part in list(industries_counted.values())
    ]
    technologies_percentage = [
        round(part/sum(list(technologies_counted.values())) * 100, 2)
        for part in technologies_counted.values()
    ]
    return render(
        request,
        'dashboard/index.html',
        context={
            'total_applications': total_applications,
            'applications_zipper': zip(applications_labels, applications_data),
            'applications_labels': applications_labels,
            'applications_data': applications_data,
            'applications_percentage': applications_percentage,
            'technologies_zipper': zip(list(technologies_counted.keys()), list(technologies_counted.values())),
            'technologies_labels': list(technologies_counted.keys()),
            'total_technologies': len(list(technologies_counted.keys())),
            'technologies_percentage': technologies_percentage,
            'locations_labels': list(locations_counted.keys()),
            'locations_total': len(list(locations_counted.keys())),
            'locations_percentage': list(locations_percentage),
            'locations_data': locations_data,
            'locations_zipper': zip(list(locations_counted.keys()), list(locations_counted.values())),
            'industries_zipper': zip(list(industries_counted.keys()), list(industries_counted.values())),
            'industries_labels': list(industries_counted.keys()),
            'industries_percentage': industries_percentage,
            'industries_total': len(industries_counted.keys())
        }
    )
