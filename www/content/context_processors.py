import settings


def add_ga_tracking_code(request):
    return {'GA_TRACKING_CODE': settings.GA_TRACKING_CODE}
