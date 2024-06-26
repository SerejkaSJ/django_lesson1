from datacenter.models import Passcard
from datacenter.models import Visit
from datacenter.duration import format_duration
from django.shortcuts import render, get_object_or_404


def is_visit_long(visit, minutes=60):
    duration = visit.get_duration()
    if duration.total_seconds() > minutes * 60:
        return True
    return False


def passcard_info_view(request, passcode):
    passcard = get_object_or_404(Passcard, passcode=passcode)
    visits = Visit.objects.filter(passcard=passcard)
    this_passcard_visits = []
    for visit in visits:
        this_passcard_visits.append({
            'entered_at': visit.entered_at,
            'duration': format_duration(visit.get_duration()),
            'is_strange': is_visit_long(visit)
        })

    context = {
        'passcard': passcard,
        'this_passcard_visits': this_passcard_visits
    }
    return render(request, 'passcard_info.html', context)
