from .models import Polizas
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.contrib.admin.views.decorators import staff_member_required


def report(request):
    return render_to_response(
        "admin/polizas/report.html",
        {'book_list' : Polizas.objects.all()},
        RequestContext(request, {}),
    )
report = staff_member_required(report)
