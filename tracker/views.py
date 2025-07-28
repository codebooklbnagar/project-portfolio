from django.shortcuts import render

def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip

def get_ip(request):
    user_ip = get_client_ip(request)
    return render(request, 'tracker/index.html', {'ip': user_ip})
