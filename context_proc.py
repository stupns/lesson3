def my_ip(request):
    return {'my_ip_adress': request.META['REMOTE_ADDR']}