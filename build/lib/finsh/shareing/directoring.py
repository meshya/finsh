


def get_shared_dirs ():
    from django.conf import settings
    return settings.SHARED_DIRS


def find_shared_file (fname):
    import os
    from pathlib import Path
    shared_dirs = get_shared_dirs()
    for shdir in shared_dirs:
        file_candidate = Path(shdir).resolve()/fname
        if os.path.exists(file_candidate):
            return file_candidate
    from django.http import Http404
    raise Http404(f"file {fname} not found in shareds this is shared dirs : \n {shared_dirs}")


