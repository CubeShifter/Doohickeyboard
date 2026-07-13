# Doohickeyboard
A modular approach to a macropad, utilizing pogos pins for an easy to use snap on and off experience. For this design I made 5 boards, the core, a macropad, a numpad, a knob, and an oled display. This helped me learn a lot about i2c and I learned how to use openscad! Im gonna go into depth about building each one

# General
  This applies for building any board. 3d print the top and bottom case files for whichever one you choose, and put m2 heatsets in the bottom. Solder on any componentry onto the board making sure that male pogos are on the top and left, and female pogos are on the bottom and right, and sandwitch it between the top and bottom cases. Then take an m2 screw on all four sides and secure it. Put the magnets in the holes next to the pogo pins, making sure that south is for female pins and north is for male pins. Use the BOMs, use them. 


#Core


Bottom
<img width="1750" height="1134" alt="Screenshot 2026-07-13 at 12 03 35 AM" src="https://github.com/user-attachments/assets/92f6b2b9-dc99-42cc-8642-dc48d0361e3a" />

Top
<img width="1842" height="996" alt="Screenshot 2026-07-13 at 12 04 32 AM" src="https://github.com/user-attachments/assets/b298496b-3787-4d01-b781-cf143fd8936c" />

Schematic
<img width="966" height="628" alt="Screenshot 2026-07-13 at 12 05 35 AM" src="https://github.com/user-attachments/assets/5ab11748-936a-4cb8-aa48-2cfe3ada6b6b" />

PCB
<img width="1384" height="1182" alt="Screenshot 2026-07-13 at 12 06 21 AM" src="https://github.com/user-attachments/assets/8244b625-4e25-4c6b-ab1a-8a4a204d271e" />

For assembling this, solder on the pogos, SMD solder the xiao, and solder on the switch. i havent added in implementation for it, but you can also do a battery for the xiao and use wireless, just make sure your polarity is correct. When it comes to actually flashing the code onto the xiao, turn it on and plug into the usb port and install [circuit python](https://circuitpython.org) onto it. Once you sucessefully install circuit python, drag the files in the firmware folder into the CIRCUITPY drive and watch it work. When plugging modules into it you will have to turn it off, plug it in and turn it back on for safety reasons.

#Macropad

Bottom
<img width="1700" height="1100" alt="Screenshot 2026-07-13 at 12 21 41 AM" src="https://github.com/user-attachments/assets/b572f440-da3d-4546-a9ec-228059569cc7" />

Top

<img width="1372" height="1130" alt="Screenshot 2026-07-13 at 12 22 17 AM" src="https://github.com/user-attachments/assets/9273ad61-e0bf-4b00-9167-5f759b1ac475" />

Schematic 

<img width="1110" height="806" alt="Screenshot 2026-07-13 at 12 22 56 AM" src="https://github.com/user-attachments/assets/352d907d-dbdb-4388-a979-72b07320d9fc" />

PCB

<img width="2028" height="1254" alt="Screenshot 2026-07-13 at 12 23 37 AM" src="https://github.com/user-attachments/assets/224055ab-5765-4232-86c3-2b727aa79b09" />


Solder the general stuff on, print the case. For soldering the keys, solder on the hotswap sockets so you can easily switch keyboard switches. Feel free to use keyboard keys of your choice, and whatever switches you like. The keys are arranged like the WASD keys, W being copy, A being select all, S being Paste, and D being Cut. If you want to change them you can edit the code.

