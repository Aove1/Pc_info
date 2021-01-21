import platform
import GPUtil
import psutil
import datetime
import os
import subprocess as sp
from tabulate import tabulate
from psutil._common import bytes2human
from cpuinfo import get_cpu_info

uname = platform.uname()
date = datetime.datetime.now()

Mb = 1024 * 1024
Gb = Mb * 1024
def Round(nmup):
    nmup / (1024 * 1024 * 1024)
    return round(nmup, 2)

"""                                                        System Informations                                                        """


def system_informations():
    print("=" * 20, "System Information", "=" * 20)
    print(f"System    : {uname.system} {uname.release}")
    print(f"Users Name: {psutil.users()}")
    print(f"Version   : {uname.version}")
    print(f"Machine   : {uname.machine}")
    input('\nPress any key to continue.. ')
    sp.call('cls', shell=True)


""
"""                                                        Gpu Informations                                                        """


def Gpu_informations():
    gpus = GPUtil.getGPUs()
    list_gpus = []
    for gpu in gpus:
        gpu_id = gpu.id
        gpu_name = gpu.name
        gpu_load = f'{round(((gpu.load) * 100), 2)}%'
        gpu_free_M = f'{gpu.memoryFree}MB'
        gpu_Use_M = f'{gpu.memoryUsed}MB'
        gpu_Total_M = f'{gpu.memoryTotal}MB'
        gpu_temperature = f'{gpu.temperature}°C'
        gpu_version = f'{gpu.driver}'
        gpu_uuid = gpu.uuid
        list_gpus.append(
            (gpu_id, gpu_name, gpu_load, gpu_free_M, gpu_Use_M, gpu_Total_M, gpu_temperature, gpu_version, gpu_uuid))
    print("=" * 50, "GPU Information", "=" * 50)
    print(tabulate(list_gpus, headers=(
    " id", "name", "load", "MemoryFree", "MemoryUsed", "MemoryTotal", "Temperature", "Version", "Uuid"),
                   tablefmt="fancy_grid"))
    input("\nPress any key to continue.. ")
    sp.call('cls', shell=True)


""
"""                                                        Cpu Informations                                                        """


def Cpu_informations():
    print("=" * 25, "CPU Information", "=" * 20)
    cpufreq = psutil.cpu_freq()
    list_cpu = []
    Current_Frequency = f"{0.001 * cpufreq.current:.2f} Ghz or {cpufreq.current:.2f} Mhz"
    CPU_Usage = f"{round(psutil.cpu_percent(), 2)} %"
    CPU_count = psutil.cpu_count()
    CPU_name = get_cpu_info()['brand_raw']
    l3_cache_size = f"{Round(get_cpu_info()['l3_cache_size']/ Mb)} MB"
    list_cpu.append((CPU_name, CPU_Usage, CPU_count, Current_Frequency, l3_cache_size))

    print(tabulate(list_cpu, headers=("Name", "Usage", "Cores   ", "   Current Frequency", "L3 Cache Size"), tablefmt="fancy_grid"))
    input("\nPress any key to continue.. ")
    sp.call('cls', shell=True)



""

"""                                                        Memory Informations                                                        """


def memory_informations():
    print("=" * 25, "Memory Information", "=" * 25)
    mem = psutil.virtual_memory()
    list_memory = []

    memory_total = f"{Round(mem.total / Gb)} GB"
    memory_use = f"{Round(mem.used / Mb)} MB | {mem.percent}%"
    memory_free = f"{Round(mem.free / Mb)} MB | {round(((mem.total - mem.used) / mem.total) * 100, 2)}%"
    memory_speed = 121
    list_memory.append((memory_speed, memory_total, memory_use, memory_free))

    print(tabulate(list_memory, headers=(" Name", "Total", "       Use", "      Free"), tablefmt="fancy_grid"))
    input("\nPress any key to continue.. ")
    sp.call('cls', shell=True)

""

"""                                                        Process Informations                                                        """


def Process():
    print("=" * 35, "All Process ", "=" * 35)
    psutil.test()
    input("\nPress any key to continue.. ")
    sp.call('cls', shell=True)


""
"""                                                        Disk Informations                                                        """


def disk():
    print("="*20, "Disk Information", datetime.datetime.now().strftime('%x'), "="*20)
    list_total = []
    for part in psutil.disk_partitions(all=True):
        if os.name == 'nt':
            if 'cdrom' in part.opts or part.fstype == '':
                continue
        usage = psutil.disk_usage(part.mountpoint)
        list_total.append((part.device, bytes2human(usage.total), bytes2human(usage.used), bytes2human(usage.free), f"{usage.percent} %", part.fstype))

    print(tabulate(list_total, headers=("Device", "Total", "Used", "Free", "Use ", "Type"), tablefmt="fancy_grid"))
    input("\nPress any key to continue.. ")
    sp.call('cls', shell=True)
""


def go():
    print("|", "=" * 20, date.strftime("%x | %X"), "=" * 20, "|")
    x = input(
        "1: System Information\n2: GPU Information\n3: Cpu Information\n4: Memory Information\n5: Show All "
        "Process \n6: disk Information \n7: Exit\nEnter : ")
    if x == "1":
        system_informations()
    elif x == "2":
        Gpu_informations()
    elif x == "3":
        Cpu_informations()
    elif x == "4":
        memory_informations()
    elif x == "5":
        Process()
    elif x == "6":
        disk()
    elif x == "7":
        exit()
    else:
        print("Error Renter")


while True:
    go()
