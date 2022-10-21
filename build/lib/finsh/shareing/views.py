from django.http import HttpResponse, Http404, StreamingHttpResponse
from django.conf import settings
from wsgiref.util import FileWrapper
from .directoring import find_shared_file
from sad.conf import log, c

from os import path as pathing

def upload_from_share_dir (request, fpath):
    
    def calc_size (size):
        if size // 1024 < 2 :
            return f'{size}b'
        if (size // 1024) // 1024 < 2:
            return f'{size// 1024}Kb'
        if ((size // 1024) // 1024) // 1024 < 2:
            return f'{(size// 1024) // 1024}Mb'
        if (((size // 1024) // 1024) // 1024) // 1024 < 2:
            return f'{(((size// 1024) // 1024) // 1024)}Gb'

    file_dir = find_shared_file(fpath)
    file_size = pathing.getsize(file_dir)
    default_content_type = 'application/forcedownload'
    log(f'FILE:{c.green(fpath)}:] SIZE:{c.red(calc_size(file_size))}:{"}"}')

    if not pathing.exists(file_dir):
        return Http404()
    try :
        if file_size < 50 * 1024**2 :
            response = HttpResponse(open(file_dir,'rb').read(),content_type=default_content_type)
        else:
            response = StreamingHttpResponse(FileWrapper(open(file_dir,'rb'),8192),content_type=default_content_type)
        
        response['Content-Disposition'] = f'inline; filename={pathing.basename(file_dir)}'
        response['Content-Length'] = file_size
        
        return response
    except :
        return Http404()
