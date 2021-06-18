from typing import ContextManager
from django import http
from django.conf.urls import url
from django.http.response import HttpResponse
from django.shortcuts import render
from django.urls.base import reverse

# Create your views here.

Content = {
    'Lorem ipsum dolor sit amet, consectetur adipiscing elit.': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Cras ac imperdiet magna. Pellentesque sodales et justo id dapibus. Nullam sollicitudin lobortis nisl, a maximus diam accumsan et. Phasellus sit amet neque id nulla sagittis tempor. Etiam et dui purus. Cras a nisl sed lectus faucibus auctor at id mi. Aenean vel congue turpis. Nam placerat velit risus, non vestibulum magna interdum et. Quisque auctor tellus efficitur dolor imperdiet tincidunt. Nulla dictum posuere feugiat. Quisque vel leo a quam vulputate laoreet eu quis orci.',
    'Lorem quis orci': None,
    'Donec quis orci finibus, facilisis risus ut, volutpat est.': 'Donec quis orci finibus, facilisis risus ut, volutpat est. Vestibulum tincidunt ante a lectus convallis eleifend. Proin dictum pretium dolor, quis pulvinar ex interdum non. Etiam ac eros ante. Cras interdum quis mauris nec ultrices. Fusce nulla magna, molestie et tincidunt a, faucibus ac mi. Cras nec vulputate justo. Donec ex odio, accumsan sit amet orci luctus, consectetur condimentum diam. Etiam interdum sem diam, ac semper dui iaculis tincidunt. Aenean maximus sed turpis sit amet scelerisque.',
    'Aenean placerat suscipit metus, eget scelerisque massa feugiat ut.': 'Aenean placerat suscipit metus, eget scelerisque massa feugiat ut. Donec pharetra imperdiet semper. Sed consequat ex vel lorem ornare, a sagittis lacus congue. Sed rhoncus facilisis diam id pulvinar. Praesent sagittis velit ut suscipit lacinia. Duis mi dolor, finibus ac placerat vel, cursus sed urna. Sed maximus mi lacinia, iaculis erat non, placerat elit. Duis ultricies, mi vel vestibulum placerat, ipsum risus blandit magna, eu pulvinar sapien orci nec justo. Quisque eu dictum metus, ac finibus massa. Curabitur aliquam orci eu varius maximus. Duis sed massa sed felis placerat pellentesque. Orci varius natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Donec egestas, libero et finibus egestas, nunc turpis dictum erat, aliquam pulvinar ipsum lacus et est. Integer placerat dolor sit amet imperdiet facilisis.',
    'Quisque vitae lorem quis metus vehicula finibus ac quis augue.': 'Quisque vitae lorem quis metus vehicula finibus ac quis augue. Integer pretium, ipsum at vulputate imperdiet, tortor sapien tincidunt massa, ut tempus dui arcu rutrum neque. Proin imperdiet, neque et aliquet vestibulum, dolor libero euismod risus, in tempor quam magna pharetra justo. Curabitur sollicitudin vel arcu mollis gravida. Pellentesque aliquam nec tellus a convallis. Praesent non nisl id urna tempor laoreet. Proin placerat sem sit amet dui suscipit, eget interdum mauris auctor. Quisque tincidunt congue dui. Phasellus vel enim consequat, molestie est sed, lobortis lacus. Donec sit amet odio maximus, rhoncus lacus id, bibendum quam. Etiam feugiat eros in nibh rhoncus vehicula. Donec non blandit justo, id pretium est. Interdum et malesuada fames ac ante ipsum primis in faucibus. Maecenas egestas mauris sed varius interdum. Cras scelerisque mauris at dolor dictum, eget euismod leo commodo.',
    'Sed vehicula pellentesque odio, id pulvinar metus fermentum sed.': 'Sed vehicula pellentesque odio, id pulvinar metus fermentum sed. Etiam in nisi sed metus rhoncus dignissim. Integer ut varius purus, vitae tempor ante. Morbi leo libero, maximus interdum sagittis in, posuere eu est. Aliquam non est faucibus, venenatis turpis sed, lacinia lectus. Fusce placerat consectetur lacus in porttitor. Phasellus ut mi viverra nisl faucibus rhoncus ut a turpis. Suspendisse finibus blandit porttitor. Duis mollis a nisl vel blandit. Nulla facilisi. Etiam faucibus volutpat tincidunt. In ultrices lacinia odio, non vehicula lectus ultricies in.',
    'Sed turpis erat, fermentum porta tempus eget, auctor eu velit.': 'Sed turpis erat, fermentum porta tempus eget, auctor eu velit. Pellentesque hendrerit ullamcorper vehicula. Quisque a venenatis lectus. Integer eget luctus velit. Curabitur imperdiet sapien vitae felis fringilla, quis mattis nisi semper. Nam lobortis, est eget eleifend posuere, arcu sem lobortis nisi, eget rhoncus dolor lacus non nisi. Nullam volutpat aliquam ultrices. Pellentesque tempus sagittis nisl quis ultrices.'
}


def index(request):
    title = list(Content.keys())
    contex = {
        'Judul': "Belajar Template Engine",
        'isi': title,
    }
    return render(request, 'templateengine/index.html', contex)


def itemContent(request, title):

    data = {
        'Judul': title,
        'ContenOftitle': Content[title],
    }
    return render(request, 'templateengine/itemContent.html', data)
