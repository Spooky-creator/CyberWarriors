from pywifi import PyWiFi, const, Profile

def scan_wifi_networks():
    wifi = PyWiFi()
    iface = wifi.interfaces()[0]  
    

    iface.scan()
    results = iface.scan_results()
    

    for network in results:
        print(f"SSID: {network.ssid}, Signal Strength: {network.signal}\n\n")


scan_wifi_networks()
