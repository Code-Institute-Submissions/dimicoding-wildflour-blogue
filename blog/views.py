from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader


def test(request):
    tempalte = loader.get_template("base.html")
    return HttpResponse(tempalte.render())
