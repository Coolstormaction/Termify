import os, socket, platform, psutil, datetime
from rich.console import Console 

console = Console()

user = os.getlogin()
host = socket.gethostname()
current_time = datetime.datetime.now().strftime("%I:%M %p")
current_directory = os.getcwd()
sys_info = platform.system()
ip_address = socket.gethostbyname(socket.gethostname())
load_avg = psutil.getloadavg()
memory = psutil.virtual_memory()
memory_used = f"{memory.used / (1024 ** 3):.2f} GB"
memory_available = f"{memory.total / (1024 ** 3):.2f} GB"
cpu_info = platform.processor()
cpu_cores = psutil.cpu_count(logical=False)
cpu_threads = psutil.cpu_count(logical=True)
cpu_details = f"{cpu_info} ({cpu_cores} cores, {cpu_threads} threads)"
network_info = psutil.net_if_stats()
ethernet_info = network_info.get('Ethernet', None) 
network_speed = f"{ethernet_info.speed} Mbps" if ethernet_info else "100%"
processes = len(psutil.pids())
users_online = len(psutil.users())
last_login = datetime.datetime.fromtimestamp(os.path.getatime(os.path.expanduser("~"))).strftime("%Y-%m-%d %H:%M:%S")
battery_info = psutil.sensors_battery()
battery_status = f"{battery_info.percent}% remaining" if battery_info else "100%"

console.print(f"[green]{user}@[blue]{host} [yellow]{current_time}\n[light_blue]{sys_info}@[red]{ip_address} | [yellow]{load_avg} Load Avg.\n[cyan]Memory: [blue]{memory_used}/{memory_available} [green]{cpu_info} ([white]{cpu_cores} cores, {cpu_threads} threads)\n[purple]{network_speed} [green]🔋 {battery_status} [red]Processes [white]and [yellow]User's Online: {processes} | {users_online}\n[blue]Last Login: {last_login}")