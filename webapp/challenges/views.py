from django.http import response
from django.http.response import HttpResponseNotFound
from django.shortcuts import redirect, render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

# Create your views here.

Bulan = {
    "Januari": "Ini LIST bulan Januari",
    "Februari": "Ini LIST bulan Februari",
    "Maret": "Ini LIST bulan Maret",
    "April": "Ini LIST bulan April",
}


def index(request):
    list_bulan = ""
    nama_bulan = list(Bulan.keys())
    for bulan in nama_bulan:

        urlBulan = reverse('bulanreverse', args=[bulan])
        list_bulan += f'<li><a href=\"{urlBulan}\">{bulan}</a></li>'

    responeData = f"<ul>{list_bulan}</ul>"
    return HttpResponse(responeData)


def Random1(request, bulan):
    Heading = "Ini Bulan dengan REGEX. Bulan ini adalah: "
    str = Heading + bulan

    return HttpResponse(str)


def Random2(request, bulan):
    Heading = "Ini Bulan dengan IF. Bulan ini adalah: "
    if bulan == "Januari":
        bulan = "Januari"
        str = Heading + bulan
    else:
        lain = "ini bulan lainnya"
        str = Heading + lain

    return HttpResponse(str)


def Random3(request, bulan):
    try:
        str = Bulan[bulan]
        return HttpResponse(str)
    except:
        return HttpResponseNotFound("This month is not supported")


def Random4(request, bulan):
    bulankeys = list(Bulan.values())
    str = bulankeys[bulan-1]
    return HttpResponse(str)


def Random5(request, bulan):
    bulankeys = list(Bulan.keys())
    redirectbulan = bulankeys[bulan-1]
    return HttpResponseRedirect(reverse('bulanreverse', args=[redirectbulan]))
