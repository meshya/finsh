from django.http import HttpRequest, HttpResponse
def core_serv (request:HttpRequest,command:str):
    if command == 'test':
        return HttpResponse('succes')
    if command == 'add':
        ...
    if command == 'remove':
        ...
    if command == 'stat':
        ...
    return HttpResponse('Not Found',status=404)
