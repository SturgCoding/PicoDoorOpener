import network
import socket
import time
from machine import Pin

# Start Access Point
ap = network.WLAN(network.AP_IF)
ap.config(essid='PicoW_AP', password='SturgPico')  # Optional password
ap.active(True)

# Wait until AP is active
while not ap.active():
    time.sleep(1)

print("AP started. Connect to:", ap.ifconfig()[0])

# === UI HTML ===
def web_page():
    # All URLs will be unusable as not connected to the internet
    
    # CSS will have to be code-oriented with the functionality entact
        # All photos may not be able to be loaded onto the Pico
        # Extensive code for CSS could 'brick' the Pico but is unlikely
        
    return """
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Pico Wireless controls</title>
    <style>
        body {
            /* PCB like background */
            background: #1a1a1a; /* Dark background for contrast */
            background-image: 
              linear-gradient(90deg, #8B4513 2px, transparent 2px), /* Horizontal copper traces */
              linear-gradient(0deg, #8B4513 2px, transparent 2px), /* Vertical copper traces */
              linear-gradient(90deg, #FFD700 1px, transparent 1px), /* Horizontal gold traces */
              linear-gradient(0deg, #FFD700 1px, transparent 1px); /* Vertical gold traces */
            background-size: 40px 40px, 40px 40px, 80px 80px, 80px 80px;
            background-position: 0 0, 20px 20px, 0 0, 20px 20px;
            background-repeat: repeat, repeat, repeat, repeat;
            /* PCB like background */
            font-family: Arial, sans-serif;
            margin: 0;
            padding: 0;
            height: 100vh;
            display: flex;
            justify-content: center;
            align-items: center;
        }
        .container {
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100%;
            width: 100%;
            flex-direction: column;
            padding: 10px;
        }
        table {
            border-collapse: collapse;
            width: 100%;
            max-width: 600px;
            margin: 20px auto;
            text-align: center;
        }
        th, td {
            padding: 20px;
            font-size: 18px;
        }
        th {
            background-color: #333;
            color: #fff;
        }
        td {
            background-color: #f4f4f4;
        }
        .switch-button {
            padding: 10px 20px;
            background-color: #4CAF50;
            color: white;
            border: none;
            border-radius: 25px;
            cursor: pointer;
            font-size: 16px;
            transition: background-color 0.3s ease;
            width: 100%;
            max-width: 200px;
            margin: 10px 0;
        }
        .switch-button.off {
            background-color: #f44336;
        }
        .switch-button:hover {
            background-color: #45a049;
        }
        .switch-button.off:hover {
            background-color: #e60000;
        }
        /* Media Query for small devices */
        @media screen and (max-width: 600px) {
            table {
                width: 100%;
            }
            .container {
                padding: 5px;
            }
            .switch-button {
                width: 100%; /* Make buttons full width on small devices */
            }
            th, td {
                font-size: 16px;
                padding: 10px;
            }
        }
        /* Make sure the body fills the entire screen */
        html, body {
            height: 100%;
            margin: 0;
        }
    </style>
</head>
<body>
    <div class="container">
        <table>
            <tr>
                <th>Toggle light</th>
                <th>Script 2</th>
                <th>Script 3</th>
            </tr>
            <tr>
                <td><button class="switch-button off" onclick="toggleSwitch(this, '1')">OFF</button></td>
                <td><button class="switch-button off" onclick="toggleSwitch(this, '2')">OFF</button></td>
                <td><button class="switch-button off" onclick="toggleSwitch(this, '3')">OFF</button></td>
            </tr>
        </table>
    </div>
    <script>
        function toggleSwitch(button, scriptId) {
            let state = 'on';
            if (button.classList.contains('off')) {
                button.classList.remove('off');
                button.textContent = 'ON';
            } else {
                button.classList.add('off');
                button.textContent = 'OFF';
                state = 'off';
            }
            fetch('/?script=' + scriptId + '&state=' + state)
                .then(response => console.log('Sent:', scriptId, state))
                .catch(error => console.error('Error:', error));
        }
    </script>
</body>
</html>
"""

# === Script handler ===
def scripts(num):
    # Easier switch case basis, using exec()
    program = {
        1: "LED = Pin('LED', Pin.OUT); LED.toggle()",
        2: "LED = Pin(16, Pin.OUT); LED.toggle()",
        3: 'print("Script 3: Not implemented")'
    }
    if program.get(num):
        exec(program[num])
    else:
        print("Invalid script")

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
            print(f"Script {script} set to {state}")
            scripts(script)

        # Always return HTML
        response = web_page()
        conn.send("HTTP/1.1 200 OK\r\nContent-Type: text/html\r\n\r\n")
        conn.sendall(response)
        conn.close()

    except Exception as e:
        print("Error:", e)
        conn.close()
