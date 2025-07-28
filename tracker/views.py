import requests
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
    
    try:
        response = requests.get(f"https://ipapi.co/{user_ip}/json/")
        data = response.json()
        location_data = {
            'ip': user_ip,
            'city': data.get('city'),
            'region': data.get('region'),
            'country': data.get('country_name'),
            'org': data.get('org'),
            'timezone': data.get('timezone'),
            'latitude': data.get('latitude'),
            'longitude': data.get('longitude'),
        }
    except Exception as e:
        location_data = {
            'ip': user_ip,
            'error': 'Location fetch failed'
        }

    return render(request, 'tracker/index.html', location_data)
