def get_ip(request):
    x = request.META.get('HTTP_X_FORWARDED_FOR')
    if x:
        ip = x.split(',')[0].strip()
    else:
        ip = request.META.get("REMOTE_ADDR")
    return ip
