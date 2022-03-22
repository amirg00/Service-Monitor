import psutil
import subprocess
import re

def win_sample():
    """
    Function return a sample of services
    for the curent time. sample is list of
    tuple, each tuple is service witw
    name and status.
    """
    services_list = list(psutil.win_service_iter())
    return [(service.name(), psutil.win_service_get(service.name()).status()) for service in services_list]


def linux_sample():
    running = '+'
    services_lst = []
    output_str = subprocess.check_output("service --status-all", shell=True).decode("UTF-8")
    services_list = output_str.split('\n')

    for index, service in enumerate(services_list):
        # Happens because the last \n after split
        if service == "":
            continue
        service_symbols = service.split(' ')

        status, service_name = service_symbols[2], service_symbols[5]

        if status == running:
            status = "Running"
        else:
            status = "Stopped"

        services_lst.insert(index, (status, service_name))

    return services_lst


