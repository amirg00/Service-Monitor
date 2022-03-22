import psutil

def win_sample():
    """
    Function return a sample of services
    for the curent time. sample is list of
    tuple, each tuple is service witw
    name and status.
    """
    services_list = list(psutil.win_service_iter())
    return [(service.name(), psutil.win_service_get(service.name()).status()) for service in services_list] 