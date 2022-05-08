from follow_bot import spotify
import threading, os, time
from pystyle import Colors, Colorate


lock = threading.Lock()
counter = 0
proxies = []
proxy_counter = 0

line = print(Colorate.Horizontal(Colors.blue_to_green, "╚╦═════════════════╦═════════════════════╦╝", 1))
print("")
py = print(Colorate.Horizontal(Colors.blue_to_green, """  ██████  ███████ ███████ ██    ██ 
██    ██ ██         ███   ██  ██  
██    ██ █████     ███     ████   
██ ▄▄ ██ ██       ███       ██    
 ██████  ███████ ███████    ██    
    ▀▀                            
                                   """, 1))
print("")
pog = print(Colorate.Horizontal(Colors.blue_to_green, """███████ ██████   ██████  ████████ ██ ███████ ██    ██     ██████   ██████  ████████ 
██      ██   ██ ██    ██    ██    ██ ██       ██  ██      ██   ██ ██    ██    ██    
███████ ██████  ██    ██    ██    ██ █████     ████       ██████  ██    ██    ██    
     ██ ██      ██    ██    ██    ██ ██         ██        ██   ██ ██    ██    ██    
███████ ██       ██████     ██    ██ ██         ██        ██████   ██████     ██    
                                                                                    
                                                                                    """, 1))     
print("")   
v2 = print(Colorate.Horizontal(Colors.blue_to_green, """╚╦═════════════════╦═════════════════════╦╝""", 1))                     

print(Colors.blue + """
    Made by Qezy#1337
""")

spotify_profile = str(input("Spotify Link or Username: "))
threads = int(input("\nThreads: "))

def load_proxies():
    if not os.path.exists("proxies.txt"):
        print("\nFile proxies.txt not found")
        time.sleep(10)
        os._exit(0)
    with open("proxies.txt", "r", encoding = "UTF-8") as f:
        for line in f.readlines():
            line = line.replace("\n", "")
            proxies.append(line)
        if not len(proxies):
            print("\nNo proxies loaded in proxies.txt")
            time.sleep(10)
            os._exit(0)

print("\n[1] Proxies\n[2] Proxyless")
option = int(input("\n> "))
if option == 1:
    load_proxies()

def safe_print(arg):
    lock.acquire()
    print(arg)
    lock.release()

def thread_starter():
    global counter
    if option == 1:
        obj = spotify(spotify_profile, proxies[proxy_counter])
    else:
        obj = spotify(spotify_profile)
    result, error = obj.follow()
    if result == True:
        counter += 1
        safe_print("[Success] Followed {}".format(counter))
    else:
        safe_print(f"Error {error}")

while True:
    if threading.active_count() <= threads:
        try:
            threading.Thread(target = thread_starter).start()
            proxy_counter += 1
        except:
            pass
        if len(proxies) <= proxy_counter: #Loops through proxy file
            proxy_counter = 0