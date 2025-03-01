def main():
    # MAJOR CREDIT TO @dbisu ON GITHUB FOR MAINTAINING THE MAIN REPOSITORY!
    # CREDIT TO @steveiliop56 ON GITHUB FOR INSPIRING ME TO MAKE THIS TOOL!

    import os, psutil, shutil, ctypes
    from ctypes import wintypes
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
    print(f"{Back.LIGHTBLUE_EX}!! IMPORTANT NOTES !!{Style.RESET_ALL}")
    print("1: Before you start, you are required to plug in your Pico while holding the BOOTSEL button and rename the volume label of it to 'RPI-RP2'.")
    print("2: You are advised to delete all the files in your Pico.")
    print("3: You are advised that you do not try to do anything malicious with the finished product, and I am not liable for any legal troubles you may face.")
    print("4: This is not a finished product, and I am not liable if your Pico somehow gets bricked, although it shouldn't happen.")
    print("5: Full wireless support for the Pico W and Pico 2W are not yet available, but they should still function as if they were a Pico or Pico 2")
    input(f"{Fore.CYAN}\nPress [ENTER] to continue.{Style.RESET_ALL}")
    cls()

    # MODEL SELECTION
    while True:
        print(f"""{Fore.BLUE}SELECT YOUR RASPBERRY PI PICO MODEL:{Style.RESET_ALL}
        1) Pico
        2) Pico W
        3) Pico 2
        4) Pico 2W
        """)
        modelSelection = input(f"{Fore.CYAN}SELECTION: {Style.RESET_ALL}")

        if modelSelection in ['1', '2', '3', '4']:
            break
        else:
            print(f"{Fore.RED}Invalid selection. Pick a number!")
            sleep(2)
            cls()
    cls()

    # DRIVE SELECTION
    while True:
        print(f"{Fore.BLUE}SELECT YOUR PICO'S DRIVE LETTER:{Style.RESET_ALL}")
        selectedDriveLabel = input(f"{Fore.CYAN}SELECTION: {Style.RESET_ALL}")

        if len(selectedDriveLabel) > 1:
            print(f"{Fore.RED}Invalid selection. You must select the drive LETTER that is assigned to your Pico, not the name!{Style.RESET_ALL}")
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
            print(f"{Fore.RED}No drive found.\nAre you sure it's plugged in?\nMaybe you passed the wrong drive letter?\nOr maybe the Pico's drive label is not RPI-RP2?\nIf that's the case, rename it to 'RPI-RP2'.{Style.RESET_ALL}")
            input("\n[Press ENTER to continue]")
            cls()
            continue

    # CONVERSION
    maxConvAmt = 10
    def convertRem(a:int):
        cls()
        print(f"{Fore.CYAN}Converting. Please wait.\n[{str(a)}/{str(maxConvAmt)}]{Style.RESET_ALL}")

    convertRem(0)
    files_to_copy = {
        "1": "dependancies\\process\\adafruit-circuitpython-raspberry_pi_pico-en_US-9.2.1.uf2",
        "2": "dependancies\\process\\adafruit-circuitpython-raspberry_pi_pico_w-en_US-9.2.1.uf2",
        "3": "dependancies\\process\\adafruit-circuitpython-raspberry_pi_pico2-en_US-9.2.1.uf2",
        "4": "dependancies\\process\\adafruit-circuitpython-raspberry_pi_pico2_w-en_US-9.2.1.uf2",
    }
    shutil.copy(f"{files_to_copy[modelSelection]}",f"{selectedDriveLabel}:\\")
    sleep(9)
    convertRem(1)
    shutil.copytree(f"dependancies\\final\\lib\\", f"{selectedDriveLabel}:\\")
    convertRem(2)
    os.makedirs(f"{selectedDriveLabel}:\\lib\\adafruit_hid ", exist_ok=True)
    convertRem(3)
    os.makedirs(f"{selectedDriveLabel}:\\lib\\asyncio", exist_ok=True)
    convertRem(4)
    shutil.copytree("dependancies\\final\\lib\\adafruit_hid", f"{selectedDriveLabel}:\\lib\\adafruit_hid")
    convertRem(5)
    shutil.copytree(f"dependancies\\final\\lib\\asyncio", f"{selectedDriveLabel}:\lib\\asyncio")
    convertRem(6)
    shutil.copy(f"dependancies\\final\\boot.py", f"{selectedDriveLabel}:\\")
    convertRem(7)
    shutil.copy(f"dependancies\\final\\code.py", f"{selectedDriveLabel}:\\")
    convertRem(8)
    shutil.copy(f"dependancies\\final\\duckyinpython.py", f"{selectedDriveLabel}:\\")
    convertRem(9)
    shutil.copy(f"dependancies\\final\\payload.dd", f"{selectedDriveLabel}:\\")

    # FINISH
    cls()
    print(f"{Fore.GREEN}Conversion finished!\n[{str(maxConvAmt)}/{str(maxConvAmt)}]\n{Style.RESET_ALL}")
    sleep(1)
    print(f"{Fore.CYAN}Additional notes:{Style.RESET_ALL}")
    print(f"- Refer to {Fore.YELLOW}https://github.com/dbisu/pico-ducky/tree/main?tab=readme-ov-file{Style.RESET_ALL} for additional info on how to use your new PicoDucky.")
    print(f"- Refer to {Fore.YELLOW}https://docs.hak5.org/hak5-usb-rubber-ducky/duckyscript-tm-quick-reference{Style.RESET_ALL} for additional info on how to edit your payload.")

    print(f"\nCREDIT TO {Fore.LIGHTMAGENTA_EX}@dbisu{Style.RESET_ALL} ON GITHUB FOR MAINTAINING THE MAIN REPOSITORY FOR THE INSTALLATION!")
    print(f"CREDIT TO {Fore.LIGHTMAGENTA_EX}@steveiliop56{Style.RESET_ALL} ON GITHUB FOR INSPIRING ME TO MAKE THIS TOOL!")