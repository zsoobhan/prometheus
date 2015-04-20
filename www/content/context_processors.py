from django.conf import settings


def add_ga_tracking_code(request):
    return {'GA_TRACKING_CODE': settings.GA_TRACKING_CODE}


def add_robots_question(request):
    q_and_a = request.session.get('q_and_a', None)
    if q_and_a:
        return {'QUESTION': q_and_a['question']}
    return {}
