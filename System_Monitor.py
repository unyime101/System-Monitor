import psutil #python module that allows me to have access to cpu , memory and network info
from datetime import datetime
from System_Email import send_email
CPU_THRESHOLD = 80
MEM_THRESHOLD = 80
DISK_THRESHOLD = 90

def log(message): #this method will actually do the writing to the log file
    with open("System_log.txt", "a") as f: #opens the  already created log text file
        f.write(f"{datetime.now()} - {message}\n") #appends the details of the checks to the log. Appends so it doesnt overwrite any previos data


def check_cpu():
  cpu = psutil.cpu_percent(interval = 1) #checks at an interval  of 1 second
  log(f"Cpu Usage: {cpu}%") # stored in txt
  if cpu> CPU_THRESHOLD: #checks to see if it has reached the threshold
    log(f"Alert!! Cpu Usage is too high. Be careful. \n Cpu Usage: {cpu}%")
  return cpu

def check_mem():
  mem = psutil.virtual_memory() #info on ram usage
  log(f"Memory Usage: {mem.percent}%") # amount of mem usage in perecnt val stored in txt
  if mem.percent > MEM_THRESHOLD: #checks againt threshold
    log(f"Alert! Memory usage is too high!\n Memory Usage: ({mem.percent}%)")
    return mem.percent
def check_disk():
   disk = psutil.disk_usage("/") # disk usage at root folder
   log(f"Disk Usage: {disk.percent}%") # logs it to txt
   if disk.percent > DISK_THRESHOLD: # checks it against the threshold
      log(f"Alert!! Disk usage is too high! \n Disk Usage: ({disk.percent}%)")
   return disk.percent

def check_uptime(): #Function i specifcally need as i ssh a lot id like to know  if ive forgotten to turn off my pi server and see how long its been up
    MAX_UPTIME_DAYS = 7  # Will do weekly reboots
    boot_time = datetime.fromtimestamp(psutil.boot_time()) #calculates when the system was first booted up
    uptime = datetime.now() - boot_time #calculates how long its been since it was booted
    uptime_days = uptime.total_seconds() / (60 * 60 * 24) # converts it to days
    log(f"System Uptime: {uptime}") #logs it in txt file
    if uptime_days > MAX_UPTIME_DAYS: # checks if its time for weekly reboot
        log(f"Alert!! Uptime exceeds {MAX_UPTIME_DAYS} days! Reboot and give it a rest.\n It has been: ({uptime_days:.2f} days)")    
    return uptime
def main(): # methods above are called
    log("===== System Check Started =====")
    Line_1 =  check_cpu()
    Line_2 = check_mem() # All these variable to build a message to send. Probably a better way but its 2am 
    Line_3 =check_disk()
    Line_4 =check_uptime()
    log("===== System Check Ended =====\n")
    message = f"""Subject: Pi Sys Monitor\n\nBooted on:{datetime.now()}\nCpu Usage:{Line_1}%\nMemory Usage:{Line_2}%\nDisk Usage:{Line_3}%\nSystem Uptime:{Line_4}"""
   # print(message) Checking the way the message is formatted 
    send_email(message)
if __name__ == "__main__":
    main()
