import psutil
import subprocess


def win_sample():
    """
    Function return a sample of services for the current time. sample is list of
    tuple, each tuple is a service with name and status.
    """
    services_list = list(psutil.win_service_iter())
    return [(service.name(), psutil.win_service_get(service.name()).status()) for service in services_list]


# TODO: NEED TO FIX WHEN GIVEN A SERVICE NAME WITH SPACE, SUCH AS: 'AVG ANTIVIRUS'
def linux_sample():
    """
    The function return the services sample for linux operating system.
    Sample is returned as a list of tuples (couples when first value is the server status -
    'still running or already stopped' and the second value is the service's name).
    :return: the services list as a tuple: [(STATUS, SERVICE_NAME)...].
    """
    running = '+'
    services_lst = []
    output_str = subprocess.check_output("service --status-all", shell=True).decode("UTF-8")
    services_list = output_str.split('\n')[:-1] # remove the last '' after last \n

    for index, service in enumerate(services_list):
        
        service_symbols = service.split(' ')
        status, service_name = service_symbols[2], service_symbols[5]

        if status == running:
            status = "Running"
        else:
            status = "Stopped"

        services_lst.insert(index, (status, service_name))

    return services_lst
