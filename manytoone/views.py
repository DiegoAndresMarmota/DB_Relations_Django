from django.shortcuts import render
from django.http import HttpResponse
from .models import Reporter, Article
from datetime import date

# Create your views here.


def create(request):
    rep = Reporter(first_name="Diego", last_name="Solis", email="diego_solis@gmail.com")
    rep.save()
    art1 = Article(
        headline="Lorem ipsum dolot", pub_date=date(2022, 5, 5), reporter=rep
    )
    art1.save()
    art2 = Article(
        headline="Lorem ipsum dorime", pub_date=date(2021, 10, 7), reporter=rep
    )
    art2.save()
    art3 = Article(
        headline="Lorem ipsum aimet", pub_date=date(2023, 1, 2), reporter=rep
    )
    art3.save()

    result = art1.reporter.first_name

    return HttpResponse(result)
