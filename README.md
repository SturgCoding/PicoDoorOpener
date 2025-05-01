CAD files (STL) for door handle will be added once fixed and working on my one at home

- DO DO:
    Added STL 
    Now **Develop a universal solution to handle pulling

    Figure out what type of motor/servo will be best for overcoming the force of the handle pull
    and add code to allow the script handler to enable the operation of the handle
      - Tests still in process

- TO IMPROVE:
    Captive Portal aspect or BLE communication to allow for faster or 'auto' access
    to the portal/interface
    Timeout/low energy mode needs to be added to make the system more power effifient when it is run off of battery power

- NOTES:
    Moved to ESP32 for easier prototyping, however code and how it works will be fine on Pico
    This was because i had a dev.exapansion board to hand making GND, 5V, GPIO21 perfectly close
    ESP32 has issues with creating a password locked connection compared to Pico

- CREDITS:
    https://www.printables.com/@MuldeeThings_81206
        For the 9V battery holder implented on the 3D print STL
    https://cults3d.com/en/users/cebess/3d-models
        For the Servo holder/cage implented on the 3D print STL
