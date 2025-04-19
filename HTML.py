# HTML Code section to seperate the sections

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
                <th>Toggle door</th>
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