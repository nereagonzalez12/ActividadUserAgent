from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.

def dispositivos_view(request):

    # Let's assume that the visitor uses an iPhone...
    movil = request.user_agent.is_mobile  # returns True
    tablet = request.user_agent.is_tablet # returns False
    tactil = request.user_agent.is_touch_capable # returns True
    pc = request.user_agent.is_pc # returns False
    bot = request.user_agent.is_bot # returns False
    ip_cliente = request.META.get('REMOTE_ADDR')
    context = {
        'movil': movil,
        'tablet': tablet,
        'pc': pc,
        'bot': bot,
        'tactil': tactil,
        'ip_cliente': ip_cliente,
    }

    return render(request, 'dispositivos.html', context)
def first_view(request):
    context = {
        'welcome': "welcome"
    }
    return render(request, 'base.html', context)

def info_view(request):
    navegador = request.user_agent.browser  # returns Browser(family=u'Mobile Safari', version=(5, 1), version_string='5.1')
    familia_navegador = request.user_agent.browser.family  # returns 'Mobile Safari'
    so = request.user_agent.os  # returns OperatingSystem(family=u'iOS', version=(5, 1), version_string='5.1')
    familia_so = request.user_agent.os.family  # returns 'iOS'
    version_so = request.user_agent.os.version_string  # returns '5.1'
    context = {
        'navegador': navegador,
        'familia_navegador': familia_navegador,
        'so': so,
        'familia_so': familia_so,
        'version_so': version_so,
    }
    return render(request, 'informacion.html', context)

