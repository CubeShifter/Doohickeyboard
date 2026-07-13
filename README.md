# Doohickeyboard
A modular approach to a macropad, utilizing pogos pins for an easy to use snap on and off experience. For this design I made 5 boards, the core, a macropad, a numpad, a knob, and an oled display. This helped me learn a lot about i2c and I learned how to use openscad! Im gonna go into depth about building each one

# General
  This applies for building any board. 3d print the top and bottom case files for whichever one you choose, and put m2 heatsets in the bottom. Solder on any componentry onto the board making sure that male pogos are on the top and left, and female pogos are on the bottom and right, and sandwitch it between the top and bottom cases. Then take an m2 screw on all four sides and secure it. Put the magnets in the holes next to the pogo pins, making sure that south is for female pins and north is for male pins. Use the BOMs, use them. Also if this comes off as bad, or not thorough enough, keep in mind i am writing this at 1am in the morning, and also at 7am after being in a flight with crying babies.<img width="1154" height="1314" alt="Screenshot 2026-07-13 at 12 30 04 AM" src="https://github.com/user-attachments/assets/a2f754e3-5385-4371-b4e7-d9647a383860" />
<img width="1162" height="1296" alt="Screenshot 2026-07-13 at 12 29 52 AM" src="https://github.com/user-attachments/assets/c7096a9c-27e7-4dc2-82b8-8c21955d485c" />



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

#Numpad!!!

Bottom
<img width="1018" height="1302" alt="Screenshot 2026-07-13 at 12 30 39 AM" src="https://github.com/user-attachments/assets/573b3dca-dda6-4425-8f13-142d35b909d9" />

Top
<img width="1058" height="1260" alt="Screenshot 2026-07-13 at 12 30 57 AM" src="https://github.com/user-attachments/assets/eb57c526-6137-40b0-99b4-58358c8b4ecd" />



PCB
<img width="998" height="1044" alt="Screenshot 2026-07-13 at 12 28 15 AM" src="https://github.com/user-attachments/assets/b3044123-f215-4c75-88df-e0740c8b8956" />

Same thing as usual, solder gneral stuff, print case. Use hotswap sockets for keys. I reccomend buying a set if numpad keys as you need custom 2u keys that normally are hard to get. if ur confused on what the keys do just look at the example. As always, change them in the code if u would like. <img width="474" height="493" alt="image" src="https://github.com/user-attachments/assets/c85ee745-2a44-4558-bd85-88a65d435779" />

# Oled
Bottom
  <img width="1250" height="1182" alt="Screenshot 2026-07-13 at 12 36 03 AM" src="https://github.com/user-attachments/assets/bf19ffff-726c-444a-ac00-a49c13c6d78f" />

  Top
  <img width="846" height="902" alt="Screenshot 2026-07-13 at 12 39 31 AM" src="https://github.com/user-attachments/assets/c33e88ad-6074-4d5e-ae34-46add5ca09bd" />
Extra piece
<img width="1336" height="1202" alt="Screenshot 2026-07-13 at 12 41 11 AM" src="https://github.com/user-attachments/assets/6ec6da9b-7d38-47f5-99dd-0e6bd318211e" />

  
SChematic
  <img width="914" height="664" alt="Screenshot 2026-07-13 at 12 40 28 AM" src="https://github.com/user-attachments/assets/00d16735-94a3-4784-a414-7a6b1817fe3d" />

PCB
  <img width="1786" height="1548" alt="Screenshot 2026-07-13 at 12 40 05 AM" src="https://github.com/user-attachments/assets/2e82f7dc-6371-4941-8dea-3944caa96a3c" />

Do general stuff. you may notice a frametop.stl. please also print that. When assembling, solder on wires to the pcb and connect them to the oled. I thin you als need to change some resistors up to config it for I2c on the oled, but check the docs on the oled about that. Once you have it wired, sandwitch the oled between the top and the extra file, and it will be nice. Currently the display only says "hai omelette" but you can edit the code to change it to your name and give it more fucntionality.


#Knob
Bottom

<img width="1324" height="1218" alt="Screenshot 2026-07-13 at 12 44 31 AM" src="https://github.com/user-attachments/assets/6f148ef9-8b65-4126-a42c-45bd86f5bbf7" />

Top

<img width="1512" height="1254" alt="Screenshot 2026-07-13 at 12 44 46 AM" src="https://github.com/user-attachments/assets/2186fbee-20b3-4499-8e9f-1ad133f69b73" />
Sch

<img width="2344" height="1318" alt="Screenshot 2026-07-13 at 12 45 44 AM" src="https://github.com/user-attachments/assets/f62ceb32-d87e-4beb-aaf6-b9475d83d0c4" />

Pcb <img width="1486" height="1426" alt="Screenshot 2026-07-13 at 12 45 04 AM" src="https://github.com/user-attachments/assets/17b20787-555c-457d-9f8c-d3d9ab58b7ef" />


Pretty normal, just find a knob so the encoder looks fine. currently it controls volume and press it to mute. nothing special at all.

