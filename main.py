# MAJOR CREDIT TO @dbisu ON GITHUB FOR MAINTAINING THE MAIN REPOSITORY!
# CREDIT TO @steveiliop56 ON GITHUB FOR INSPIRING ME TO MAKE THIS TOOL!

import os, psutil, shutil
from time import sleep
from colorama import Fore, Back, Style, just_fix_windows_console
just_fix_windows_console()
os.system("title Pico Ducky Builder")
def cls():
    os.system('cls')
cls()

def get_volume_label(drive_mountpoint):
    # man idk what any of this is i just copied it from somewhere
    # i guess it's like win32 constants or something
    import ctypes
    from ctypes import wintypes
    GetVolumeInformationW = ctypes.windll.kernel32.GetVolumeInformationW
    root_path_name = ctypes.create_unicode_buffer(drive_mountpoint, 1024)
    volume_name_buffer = ctypes.create_unicode_buffer(1024)
    file_system_name_buffer = ctypes.create_unicode_buffer(1024)
    serial_number = wintypes.DWORD()
    max_component_length = wintypes.DWORD()
    file_system_flags = wintypes.DWORD()
    result = GetVolumeInformationW(
        root_path_name,
        volume_name_buffer,
        ctypes.sizeof(volume_name_buffer),
        ctypes.byref(serial_number),
        ctypes.byref(max_component_length),
        ctypes.byref(file_system_flags),
        file_system_name_buffer,
        ctypes.sizeof(file_system_name_buffer),
    )

    if result:
        return volume_name_buffer.value
    else:
        return None

# DISCLAIMER
print(Back.LIGHTBLUE_EX+"!! IMPORTANT NOTES !!"+Style.RESET_ALL)
print(f"\n{Fore.LIGHTYELLOW_EX}1: RUN AS ADMINISTRATOR!{Style.RESET_ALL}")
print("2: Before you start, you are required to plug in your Pico while holding the BOOTSEL button and rename the volume label of it to 'RPI-RP2'.")
print("3: You are advised to delete all the files in your Pico.")
print("4: You are advised that you do not try to do anything malicious with the finished product, and I am not liable for any legal troubles you may face.")
print("5: This is not a finished product, and I am not liable if your Pico somehow gets bricked, although it shouldn't happen.")
print("6: Full wireless support for the Pico W and Pico 2W are not yet available, but they should still function as if they were a Pico or Pico 2")
print("7: This tool does not yet work on Linux or macOS. Use it on a Windows machine.")
input(Fore.CYAN+"\nPress [ENTER] to continue."+Style.RESET_ALL)
cls()

# MODEL SELECTION
while True:
    print(f"""{Fore.BLUE}SELECT YOUR RASPBERRY PI PICO MODEL:{Style.RESET_ALL}
    1) Pico
    2) Pico W
    3) Pico 2
    4) Pico 2W
    """)
    modelSelection = input(Fore.CYAN+"SELECTION: "+Style.RESET_ALL)

    if modelSelection == '1' or modelSelection == '2' or modelSelection == '3' or modelSelection == '4':
        break
    else:
        print(Fore.RED+"Invalid selection. Pick a number!")
        sleep(2)
        cls()
cls()

# DRIVE SELECTION
while True:
    print(Fore.BLUE+"SELECT YOUR PICO'S DRIVE LETTER:"+Style.RESET_ALL)
    selectedDriveLabel = input(Fore.CYAN+"SELECTION: "+Style.RESET_ALL)

    if len(selectedDriveLabel) > 1:
        print(Fore.RED+"Invalid selection. You must select the drive LETTER that is assigned to your Pico, not the name!"+Style.RESET_ALL)
        sleep(4)
        cls()
        continue

    driveCheckPassed = False
    for part in psutil.disk_partitions():
        cls()
        if part.device and selectedDriveLabel in part.device and get_volume_label(part.mountpoint) == "RPI-RP2":
            print(f"{Fore.GREEN}FOUND DRIVE {part.device} AS {get_volume_label(part.mountpoint)}{Style.RESET_ALL}")
            sleep(2)
            driveCheckPassed = True
            break

    if driveCheckPassed:
        break
    else:
        print(Fore.RED+"No drive found.\nAre you sure it's plugged in?\nMaybe you passed the wrong drive letter?\nOr maybe the Pico's drive label is not RPI-RP2?\nIf that's the case, rename it to 'RPI-RP2'."+Style.RESET_ALL)
        input("\n[Press ENTER to continue]")
        cls()
        continue

# CONVERSION
def convertRem(a:int):
    cls()
    print(Fore.CYAN+f"Converting. Please wait.\n[{str(a)}/11]"+Style.RESET_ALL)

convertRem(0)
if modelSelection == "1":
    os.system(f"copy dependancies\process\\adafruit-circuitpython-raspberry_pi_pico-en_US-9.2.1.uf2 {selectedDriveLabel}:\ ")
elif modelSelection == "2":
    os.system(f"copy dependancies\process\\adafruit-circuitpython-raspberry_pi_pico_w-en_US-9.2.1.uf2 {selectedDriveLabel}:\ ")
elif modelSelection == "3":
    os.system(f"copy dependancies\process\\adafruit-circuitpython-raspberry_pi_pico2-en_US-9.2.1.uf2 {selectedDriveLabel}:\ ")
elif modelSelection == "4":
    os.system(f"copy dependancies\process\\adafruit-circuitpython-raspberry_pi_pico2_w-en_US-9.2.1.uf2 {selectedDriveLabel}:\ ")
sleep(9)
convertRem(1)
os.system(f"copy dependancies\\final\lib\ {selectedDriveLabel}:\ ")
convertRem(2)
os.system(f"mkdir {selectedDriveLabel}:\lib\ ")
convertRem(3)
os.system(f"mkdir {selectedDriveLabel}:\lib\\adafruit_hid ")
convertRem(4)
os.system(f"mkdir {selectedDriveLabel}:\lib\\asyncio ")
convertRem(5)
os.system(f"copy dependancies\\final\lib\\adafruit_hid {selectedDriveLabel}:\lib\\adafruit_hid ")
convertRem(6)
os.system(f"copy dependancies\\final\lib\\asyncio {selectedDriveLabel}:\lib\\asyncio ")
convertRem(7)
os.system(f"copy dependancies\\final\\boot.py {selectedDriveLabel}:\ ")
convertRem(8)
os.system(f"copy dependancies\\final\code.py {selectedDriveLabel}:\ ")
convertRem(9)
os.system(f"copy dependancies\\final\duckyinpython.py {selectedDriveLabel}:\ ")
convertRem(10)
os.system(f"copy dependancies\\final\payload.dd {selectedDriveLabel}:\ ")
sleep(5)

# FINISH
cls()
print(Fore.GREEN+"Conversion finished!\n[11/11]\n"+Style.RESET_ALL)
sleep(1)
print(Fore.CYAN+"Additional notes:"+Style.RESET_ALL)
print(f"1. Refer to {Fore.YELLOW}https://github.com/dbisu/pico-ducky/tree/main?tab=readme-ov-file{Style.RESET_ALL} for additional info on how to use your new PicoDucky.")
print(f"2. Refer to {Fore.YELLOW}https://docs.hak5.org/hak5-usb-rubber-ducky/duckyscript-tm-quick-reference{Style.RESET_ALL} for additional info on how to edit your payload.")

print(f"\nCREDIT TO {Fore.LIGHTMAGENTA_EX}steveiliop56{Style.RESET_ALL} ON GITHUB FOR INSPIRING ME TO MAKE THIS TOOL!")
