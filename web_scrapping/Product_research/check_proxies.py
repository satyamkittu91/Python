import threading
import queue
import requests
import csv

lock = threading.Lock()

q = queue.Queue()
valid_proxies = []

with open("proxy_list.txt", "r") as f:
    proxies = f.read().split("\n")
    for p in proxies:
        if p.strip():
            q.put(p.strip())

with open("Free_Proxy_List.txt",newline='', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    for row in reader:
        ip = row['ip'].strip('"')
        port = row['port'].strip('"')
        protocol = row['protocols'].strip('"').lower()
        if protocol == 'http':
            proxy = f"http://{ip}:{port}"
        elif protocol == 'https':
            proxy = f"https://{ip}:{port}"
        elif protocol == 'socks5':
            proxy = f"socks5://{ip}:{port}"
        elif protocol == 'socks4':
            proxy = f"socks4://{ip}:{port}"
        else:
            continue
        q.put(proxy)

with open ("proxies.txt", "r") as f:
    for line in f:
        proxy = line.strip()
        if proxy:
            if not proxy.startswith(("http://", "https://", "socks5://", "socks4://")):
                proxy = f"http://{proxy}"
            q.put(proxy)


def check_proxy():
    global q
    while True:
        try:

            proxy = q.get_nowait()
        except queue.Empty:
            break
        try:
            res = requests.get("http://ipinfo.io/json",
                               proxies={"http": proxy,
                                        "https": proxy},
                                        timeout=5)
            if res.status_code == 200:
                print(proxy)
                with lock:
                    valid_proxies.append(proxy)

        except:
            continue


# Start multiple threads to check proxies
threads = []
for _ in range(50):
    t = threading.Thread(target=check_proxy)
    t.start()
    threads.append(t)

for th in threads:
    th.join()
print("Proxy checking completed. Valid proxies saved to 'valid_proxies.txt'.")

with open("valid_proxies.txt", "w") as f:
    f.write("\n".join(valid_proxies))
