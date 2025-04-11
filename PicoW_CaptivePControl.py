import network
import socket
import time

# Linked Management scripts
import HTML
import ScriptHandle

# Start Access Point
ap = network.WLAN(network.AP_IF)
ap.config(essid='PicoW_AP', password='PicoPass')  # Optional password
ap.active(True)

# Wait until AP is active
while not ap.active():
    time.sleep(1)

print("AP started. Connect to:", ap.ifconfig()[0])

# === Server socket ===
addr = socket.getaddrinfo("0.0.0.0", 80)[0][-1]
server = socket.socket()
server.bind(addr)
server.listen(5)
print("Web server running on", addr)

while True:
    try:
        conn, client_addr = server.accept()
        print("Client connected from", client_addr)
        request = conn.recv(1024).decode()
        print("Request:\n", request)

        # Handle ?script=X&state=Y
        if "GET /?" in request:
            query = request.split("GET /?")[1].split(" ")[0]
            print("Query:", query)
            pairs = query.split("&")
            params = {k: v for k, v in (pair.split("=") for pair in pairs if "=" in pair)}
            script = int(params.get("script", 0))
            state = params.get("state", "")
            print(f"Execute: Script {script} set to {state}")
            print(f"Executed: {ScriptHandle.Handler(script, state)}")

        # Always return HTML
        response = HTML.web_page()
        conn.send("HTTP/1.1 200 OK\r\nContent-Type: text/html\r\n\r\n")
        conn.sendall(response)
        conn.close()

    except Exception as e:
        print("Error:", e)
        conn.close()
