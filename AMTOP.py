import phonenumbers
from phonenumbers import geocoder, carrier

def main_menu():
    print("\033[32m         _                          _    _           ")
    print(f"\033[33m        / \\   _ __ ___   ___  ___  | | _(_)_ __ ___  ")
    print("\033[35m       / _ \\ | '_ ` _ \\ / _ \\/ __| | |/ / | '_ ` _ \\ ")
    print("\033[33m      / ___ \\| | | | | | (_) \\__ \\ |  | | | | | | | |")
    print("\033[32m     /_/   \\_\\_| |_| |_|\\___/|___/ |_|\\_\\_|_| |_| |_|")
    
    print('\033[032m\033[032m\033[33m  \033[032m \033[37m \033[032m \033[33m')
    
    print('\033[091m[\033[096mFacebook\033[91m]\033[35m:\033[97m[\033[31mMIK TC\033[97m]\033[091m[ \033[096mInstergram\033[91m]\033[35m:\033[97m[\033[31mMIK TC\033[97m]\033[091m[\033[096mWhatsapp\033[91m]\033[35m:\033[97m[\033[31m0754607575\033[97m] ')
 
    print('\033[092m  [ ]\033[35m:\033[97m[\033[96mTOOL CREATEBY BLACTECH\033[97m]\033[32m(AMOS KIM the MIK TC.TOP BOY )\033[32m[ ]')   
 
    
    print("\033[32m        TOP BOY WEB DEVELOPER \033[31m:\033[32m AMOS KIM CYBERSECURITY")   
   #empty
    print('\033[032m \033[032m \033[33m  \033[032m \033[37m \033[032m \033[33m')
    print('\033[032m \033[032m \033[33m  \033[032m \033[37m \033[032m \033[33m')
    print('\033[032m \033[032m \033[33m  \033[032m \033[37m \033[032m \033[33m')
    
     
    
    
    print('\033[032m[ \033[37m1 \033[032m] \033[33m Track phone numbers            \033[032m[ \033[37m2 \033[032m] \033[33m back ')

    choice = input("\nEnter your choice (1 or 2): ")
    
    if choice == "1":
        track_number()
    elif choice == "2":
        print("\n\033[36mProgram by Amos. Returning to menu...\n")
        main_menu()
    else:
        print("\033[31mInvalid choice. Please enter 1 or 2.\n")
        main_menu()

def track_number():
    print("\n\033[39m=== Phone Number Tracker ===\n")
    number = input("Enter a phone number (with country code, e.g., +254754607575): ")

    try:
        # Geolocation
        ch_number = phonenumbers.parse(number, "CH")
        location = geocoder.description_for_number(ch_number, "en")

        # Carrier
        service_number = phonenumbers.parse(number, "RO")
        carrier_name = carrier.name_for_number(service_number, "en")

        print("\n\033[32mLocation:", location)
        print("\033[33mCarrier:", carrier_name)
    except:
        print("\033[31mInvalid phone number. Please try again.\n")

    # Wait for user to press 2 to return
    while True:
        back = input("\nPress 2 to return to main menu: ")
        if back == "2":
            print()
            main_menu()
            break
        else:
            print("\033[31mInvalid input. Please press 2 to return.\033[0m")

# Start the program
main_menu()