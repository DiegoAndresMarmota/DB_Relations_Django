from django.shortcuts import render
from django.http import HttpResponse
from .models import Publication, Article

# Create your views here.


def create(request):
    art1 = Article(headline="Primer Articulo")
    art1.save()
    art2 = Article(headline="Segundo Articulo")
    art2.save()
    art3 = Article(headline="Tercer Articulo")
    art3.save()

    pub1 = Publication(title="Primera Publicación")
    pub1.save()
    pub2 = Publication(title="Segunda Publicación")
    pub2.save()
    pub3 = Publication(title="Tercera Publicación")
    pub3.save()
    pub4 = Publication(title="Cuarta Publicación")
    pub4.save()
    pub5 = Publication(title="Quinta Publicación")
    pub5.save()
    pub6 = Publication(title="Sexta Publicación")
    pub6.save()
    pub7 = Publication(title="Septima Publicación")
    pub7.save()

    art1.publications.add(pub1)
    art1.publications.add(pub2)
    art1.publications.add(pub3)
    art2.publications.add(pub4)
    art2.publications.add(pub5)
    art3.publications.add(pub6)
    art3.publications.add(pub7)

    result = art1.publications.all()
    result = pub1.article_set.all()
    result = Publication.objects.get(id=2)
    art1.publications.remove(pub1)

    return HttpResponse(result)
