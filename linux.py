import os, psutil
from time import sleep
from colorama import Fore, Back, Style
def clr():
    os.system('clear')
clr()

if os.geteuid() != 0:
    exit(f"{Fore.RED}You need to run this file as the root user! Please use {Fore.CYAN}sudo python linux.py{Fore.RED}.{Style.RESET_ALL}")

# DISCLAIMER
print(Back.LIGHTBLUE_EX + "!! IMPORTANT NOTES !!" + Style.RESET_ALL)
print("1: Before you start, you are required to plug in your Pico while holding the BOOTSEL button.")
print("2: You are advised to delete all the files in your Pico.")
print("3: You are advised that you do not try to do anything malicious with the finished product, and I am not liable for any legal troubles you may face.")
print("4: This is not a finished product, and I am not liable if your Pico somehow gets bricked, although it shouldn't happen.")
print("5: Full wireless support for the Pico W and Pico 2W are not yet available, but they should still function as if they were a Pico or Pico 2.")
input(Fore.CYAN + "\nPress [ENTER] to continue." + Style.RESET_ALL)
clr()

# MODEL SELECTION
while True:
    print(f"""{Fore.BLUE}SELECT YOUR RASPBERRY PI PICO MODEL:{Style.RESET_ALL}
    1) Pico
    2) Pico W
    3) Pico 2
    4) Pico 2W
    """)
    modelSelection = input(Fore.CYAN + "SELECTION: " + Style.RESET_ALL)

    if modelSelection in ['1', '2', '3', '4']:
        break
    else:
        print(Fore.RED + "Invalid selection. Pick a number!" + Style.RESET_ALL)
        sleep(2)
        clr()
clr()

def convertRem(a:int):
    clr()
    print(Fore.CYAN + f"Converting. Please wait.\n[{str(a)}/6]" + Style.RESET_ALL)

# DRIVE SELECTION
while True:
    print(Fore.BLUE + "SELECT YOUR PICO'S DRIVE MOUNT POINT (e.g., /media/username/RPI-RP2):" + Style.RESET_ALL)
    selectedDrivePath = input(Fore.CYAN + "SELECTION: " + Style.RESET_ALL)

    if not os.path.ismount(selectedDrivePath):
        print(Fore.RED + "Invalid selection. Ensure it's the correct mount point of your Pico." + Style.RESET_ALL)
        sleep(4)
        clr()
        continue

    driveCheckPassed = False
    for part in psutil.disk_partitions():
        clr()
        if part.mountpoint == selectedDrivePath:
            print(f"{Fore.GREEN}FOUND MOUNTPOINT: {part.mountpoint}{Style.RESET_ALL}")
            sleep(2)
            driveCheckPassed = True
            convertRem(0)
            files_to_copy = {
                "1": "dependancies/process/adafruit-circuitpython-raspberry_pi_pico-en_US-9.2.1.uf2",
                "2": "dependancies/process/adafruit-circuitpython-raspberry_pi_pico_w-en_US-9.2.1.uf2",
                "3": "dependancies/process/adafruit-circuitpython-raspberry_pi_pico2-en_US-9.2.1.uf2",
                "4": "dependancies/process/adafruit-circuitpython-raspberry_pi_pico2_w-en_US-9.2.1.uf2"
            }
            os.system(f"cp {files_to_copy[modelSelection]} {part.mountpoint}")
            sleep(20)
    if driveCheckPassed:
        break

while True:
    clr()
    print(Fore.BLUE + "RE-ENTER YOUR PICO'S DRIVE MOUNT POINT (e.g., /media/username/CIRCUITPY):" + Style.RESET_ALL)
    selectedDrivePath = input(Fore.CYAN + "SELECTION: " + Style.RESET_ALL)

    if not os.path.ismount(selectedDrivePath):
        print(Fore.RED + "Invalid selection. Ensure it's the correct mount point of your Pico." + Style.RESET_ALL)
        sleep(4)
        clr()
        continue

    driveCheckPassed = False
    for part in psutil.disk_partitions():
        clr()
        if part.mountpoint == selectedDrivePath:
            print(f"{Fore.GREEN}FOUND MOUNTPOINT: {part.mountpoint}{Style.RESET_ALL}")
            driveCheckPassed = True
            sleep(2)
            convertRem(1)
            os.system(f"cp -r dependancies/final/lib/ {part.mountpoint}")
            convertRem(2)
            sleep(2)
            os.system(f"cp dependancies/final/boot.py {part.mountpoint}")
            convertRem(3)
            os.system(f"cp dependancies/final/code.py {part.mountpoint}")
            convertRem(4)
            os.system(f"cp dependancies/final/duckyinpython.py {part.mountpoint}")
            convertRem(5)
            os.system(f"cp dependancies/final/payload.dd {part.mountpoint}")
            break
    if driveCheckPassed:
        break


# FINISH
clr()
print(Fore.GREEN + "Conversion finished!\n[6/6]\n" + Style.RESET_ALL)
sleep(1)
print(Fore.CYAN + "Additional notes:" + Style.RESET_ALL)
print(f"- Refer to {Fore.YELLOW}https://github.com/dbisu/pico-ducky/tree/main?tab=readme-ov-file{Style.RESET_ALL} for additional info on how to use your new PicoDucky.")
print(f"- Refer to {Fore.YELLOW}https://docs.hak5.org/hak5-usb-rubber-ducky/duckyscript-tm-quick-reference{Style.RESET_ALL} for additional info on how to edit your payload.")

print(f"\nCREDIT TO {Fore.LIGHTMAGENTA_EX}@dbisu{Style.RESET_ALL} ON GITHUB FOR MAINTAINING THE MAIN REPOSITORY FOR THE INSTALLATION!")
print(f"CREDIT TO {Fore.LIGHTMAGENTA_EX}@steveiliop56{Style.RESET_ALL} ON GITHUB FOR INSPIRING ME TO MAKE THIS TOOL!")