from django.shortcuts import render

# Create your views here.

isiblog = {

    'Duis augue libero, pharetra quis hendrerit at, tristique nec risus.': ''' Ut velit erat, fermentum eu pellentesque eu, volutpat sed libero. Ut sed ex eget augue pulvinar lobortis. Nunc ipsum tortor, pretium quis fringilla porta, ultrices quis eros. Vivamus gravida lorem vel lectus tempus tincidunt. Sed at magna interdum, vehicula turpis eget, viverra ante. Maecenas vitae dui ut tellus elementum pellentesque. Praesent placerat risus sit amet est luctus consectetur. Donec id ante gravida, vehicula ligula non, efficitur arcu. Mauris venenatis arcu sed risus ornare, ac consectetur tortor fermentum. Cras vel tempus nisi, nec venenatis orci.

Duis augue libero, pharetra quis hendrerit at, tristique nec risus. Nam ac sodales libero, non faucibus ipsum. Quisque sed purus ut risus varius iaculis. Suspendisse finibus justo sed arcu sodales, sit amet egestas diam ornare. Maecenas porta orci vel placerat bibendum. Nam ac dui eu libero ultricies tincidunt in ac sem. Vivamus accumsan turpis nibh, in vestibulum mauris aliquet sed. Pellentesque condimentum enim et vestibulum iaculis. Integer auctor metus lectus, vitae eleifend purus pretium ut. Phasellus in condimentum lacus. Morbi accumsan est quis metus ullamcorper condimentum. Nullam neque risus, convallis ac ex sit amet, eleifend scelerisque tortor. In tristique tempor augue cursus iaculis. Sed purus dui, volutpat non bibendum eget, elementum a velit. Aliquam quam elit, porta sit amet elit eu, dignissim vestibulum est.

Sed sit amet auctor lorem. Sed faucibus ipsum et ante aliquet, in blandit erat pharetra. Vivamus maximus, massa eu pretium facilisis, eros eros lobortis enim, vitae molestie enim dolor quis lacus. Praesent pulvinar orci id odio ultricies ullamcorper. Morbi facilisis magna id libero commodo, sit amet tempus lectus gravida. Curabitur malesuada mauris ut ligula auctor, dapibus feugiat lorem eleifend. Morbi euismod volutpat est sed vestibulum. Mauris porta nulla nisi, at lobortis neque consectetur sit amet. Aenean venenatis sagittis libero ut rhoncus. Aenean dignissim pretium elementum. Vivamus non ex justo.

Sed orci mi, vehicula vitae sem sit amet, volutpat pellentesque quam. Suspendisse potenti. Ut convallis malesuada augue id auctor. Vestibulum sit amet pulvinar libero. Quisque lobortis laoreet molestie. Curabitur accumsan neque at diam ultricies, nec hendrerit felis vulputate. Fusce eu porttitor dolor, ut maximus est. Vestibulum efficitur imperdiet nisi a ornare. Nullam rutrum nisi vestibulum nisi ullamcorper, sit amet mattis est volutpat. Morbi egestas nisl nibh, eget dignissim nisi rutrum et. Quisque pellentesque metus id libero dapibus pellentesque. Fusce nec mauris interdum sapien gravida venenatis. Aliquam justo leo, congue at leo id, lobortis elementum leo.

Aenean in accumsan libero. Ut nulla dolor, sagittis eget magna sed, placerat dignissim ex. Vivamus bibendum scelerisque volutpat. Aenean vel pharetra ligula, euismod sagittis enim. Quisque at interdum risus. Nam nec odio vel leo mattis cursus sed at augue. Integer imperdiet, urna ac commodo viverra, nibh metus mollis lacus, quis lacinia ipsum felis vel nibh. Nullam magna ante, elementum ac diam a, dignissim vehicula elit.
    ''',

    'Mauris vel venenatis orci.': '''Proin eget justo sed eros tristique commodo. Aliquam interdum varius pulvinar. Vestibulum eu lectus ac justo faucibus rhoncus. Sed tortor augue, ullamcorper mollis nulla sit amet, lacinia maximus ipsum. Nam ut eros sed elit placerat varius. Cras magna neque, iaculis quis semper at, bibendum id eros. Nullam et porta nibh, eu scelerisque est.

Cras sit amet dignissim tellus, vel convallis risus. Mauris egestas velit ac mi accumsan pulvinar. Etiam vitae aliquam libero. Aliquam pulvinar libero quis ex scelerisque semper vitae vel elit. Curabitur ligula magna, mollis et lacus at, sagittis rhoncus sem. Cras aliquam augue maximus lectus ullamcorper, id mollis leo tempor. Fusce efficitur tortor id gravida dictum.

Mauris vel venenatis orci. Ut elementum felis egestas dui lacinia, at porta eros condimentum. Aenean pharetra, lacus at bibendum pretium, nisi sem ullamcorper nunc, eget hendrerit leo dui id felis. Mauris sit amet pharetra eros. Sed bibendum varius velit, sit amet consectetur nisi pellentesque volutpat. Cras eget erat eu lectus cursus tincidunt. Aenean et venenatis purus, non aliquet ipsum. Sed consequat magna id urna dapibus, efficitur malesuada risus vulputate. Suspendisse varius dignissim mi at tincidunt. Quisque vel risus magna. Class aptent taciti sociosqu ad litora torquent per conubia nostra, per inceptos himenaeos. Fusce pharetra lobortis ante, nec varius leo faucibus quis. Praesent non magna posuere, convallis nibh nec, tincidunt nunc. Duis dictum eu justo molestie consequat. Donec consequat, velit et rhoncus rhoncus, nisi risus sodales ante, at sollicitudin massa ipsum eu metus.

Sed laoreet nibh ac feugiat varius. Nulla facilisi. Morbi ut placerat libero. Nulla posuere felis ligula, porta mollis odio euismod sed. Maecenas vitae lacus quam. Integer ornare libero sit amet nulla ornare, sit amet dignissim tellus fringilla. Nam venenatis arcu non ante vestibulum viverra. Phasellus elementum condimentum lectus, et tempus purus faucibus et.

Nullam dapibus sollicitudin libero eget imperdiet. Aenean ullamcorper, enim sit amet consectetur interdum, nisi metus venenatis eros, vitae pulvinar nibh ex eu massa. Maecenas suscipit neque non tellus consequat, quis fermentum enim elementum. Aliquam sed blandit tellus. Nunc id fringilla libero. Proin rutrum sem ante, vitae tempor urna hendrerit varius. Proin dapibus vestibulum ligula sit amet consectetur. Phasellus ullamcorper hendrerit mollis. Pellentesque eu hendrerit ligula.
    ''',
    'Sed malesuada eget ante a ultrices.': '''Nulla pellentesque, nulla eu ultrices accumsan, dui nunc porta dolor, a porttitor nibh neque in augue. Nunc ut ornare arcu, eu vulputate tortor. Vestibulum interdum ligula at risus tristique luctus. Maecenas dictum, metus dictum lobortis tristique, quam ligula pretium velit, ut varius ligula ante sit amet quam. Pellentesque tristique diam et nibh maximus pulvinar. Nullam vel sem tellus. Etiam sed semper ante. Nulla lobortis odio et velit gravida interdum. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas.

Sed malesuada eget ante a ultrices. Mauris semper consequat finibus. Sed varius blandit sollicitudin. Ut venenatis mi elit, nec vulputate ipsum iaculis sed. Nullam sit amet risus justo. Aenean vel lacus iaculis, pharetra mauris nec, laoreet est. Nunc hendrerit, ligula vitae consectetur vestibulum, quam justo cursus ex, sed dapibus nisi magna ac massa. Integer id metus eget nunc mattis bibendum. Aliquam magna quam, rhoncus ut enim eget, ultricies gravida dolor. Phasellus dapibus velit vel ligula condimentum commodo. Nulla porttitor, diam vitae eleifend interdum, eros nisl lobortis elit, sed rhoncus quam leo nec quam. Cras sed augue et enim faucibus sagittis sit amet vel arcu.

Maecenas eu lacus metus. Quisque molestie arcu eu sem efficitur, non sagittis massa eleifend. Sed elementum, leo quis consequat aliquam, arcu diam finibus nisi, sit amet dictum justo lacus in sem. Integer eu ligula nec odio ullamcorper sollicitudin non vitae magna. Vivamus in ultrices odio. Etiam non interdum urna. Vestibulum arcu lacus, mattis sit amet justo condimentum, mollis interdum dolor. Nulla volutpat metus eu tincidunt pretium. Nulla varius odio id felis feugiat molestie. Nam venenatis tempus mi id interdum. Curabitur ultrices turpis urna, eleifend pretium metus faucibus sit amet.

In sit amet ultrices quam. Integer eros odio, aliquet mattis venenatis fermentum, viverra sit amet felis. Suspendisse dignissim justo nec imperdiet venenatis. Nunc at lectus in nisl volutpat aliquet semper non ante. Aenean ultricies et metus vel pharetra. Fusce vel venenatis orci. Quisque id velit quis nunc cursus venenatis non sed eros. Donec a felis a tortor pellentesque accumsan a nec neque. Quisque iaculis et risus at molestie. Fusce luctus enim id eros elementum tincidunt.

Vestibulum feugiat cursus elit, non sollicitudin arcu lacinia vel. Mauris quis ipsum ac ex lacinia porta. Nam laoreet, neque eget ultrices dignissim, nibh lacus lacinia magna, nec luctus nibh justo vitae orci. Donec porta orci a libero volutpat suscipit. Pellentesque id bibendum nisl. Etiam lobortis lectus eget justo auctor blandit. Proin nec gravida magna, eget lacinia quam. Donec porttitor nulla risus, eu tincidunt sapien consequat eu. Aenean iaculis nunc augue, non rhoncus diam faucibus mattis. Vestibulum at leo molestie, lobortis metus eu, faucibus massa. Suspendisse suscipit eros vel erat suscipit elementum. Curabitur facilisis nulla non pellentesque ullamcorper. Etiam at mauris porta, pharetra sapien quis, pretium neque. Maecenas ac elementum ante, ac aliquam diam. Sed ut luctus erat. Mauris facilisis laoreet massa ut tristique.
    '''
}


def index(request):
    title = list(isiblog.keys())
    contex = {
        'heading': 'a Simple Blog',
        'subheading': 'A Blog by Prasetya Adi',
        'urlBackgroud': 'assets/img/home-bg.jpg',
        'list_blog': title,
    }
    return render(request, 'blog/index.html', contex)


def post(request, titleURL):
    contex = {
        'Judul': titleURL,
        'ContenOftitle': isiblog[titleURL],
    }
    return render(request, 'blog/post.html', contex)


def about(request):
    contex = {
        'heading': 'About Me',
        'subheading': 'This is what I do.',
        'urlBackgroud': 'assets/img/about-bg.jpg',
    }
    return render(request, 'blog/about.html', contex)


def contact(request):
    contex = {
        'heading': 'Contact Me',
        'subheading': 'Have questions? I have answers.',
        'urlBackgroud': 'assets/img/contact-bg.jpg',
    }
    return render(request, 'blog/contact.html', contex)
