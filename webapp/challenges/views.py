from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def Random(request, bulan):
    Heading = "Ini Bulan dengan REGEX. Bulan ini adalah: "
    str = Heading + bulan

    return HttpResponse(str)


def Random2(request, bulan2):
    Heading = "Ini Bulan dengan IF. Bulan ini adalah: "
    if bulan2 == "Januari":
        bulan = "Januari"
        str = Heading + bulan
    else:
        lain = "ini bulan lainnya"
        str = Heading + lain

    return HttpResponse(str)


def Random3(request, bulan2):
    Heading = "Ini Bulan dengan IF. Bulan ini adalah: "
    if bulan2 == "Januari":
        bulan = "Januari"
        str = Heading + bulan
    else:
        lain = "ini bulan lainnya"
        str = Heading + lain

    return HttpResponse(str)
