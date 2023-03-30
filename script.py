import requests
import threading
import os



print("\033[91m\033[1m")
# Get URLs to visit from user input
urls = []
while True:
    url = input("Enter a URL to visit (or 'done' to finish): ")
    if url == 'done':
        break
    urls.append(url)

# Number of clicks to perform
num_clicks = 100

# Number of threads to use
num_threads = 10

# Function to perform a single click
def perform_click(num_clicks, url):
    while True:
        try:
            response = requests.get(url)
            # Do something with the response, if needed
        except requests.exceptions.RequestException as e:
            print("Error:", e)
        if num_clicks > 0:
            num_clicks -= 1
        else:
            break
          
# Print banner
os.system('clear')
print("\033[91m\033[1m") # Set color to lolcat rainbow
print("""
                            ..-,
                     ,-"         "-.
                   ,'               `.
                  /                   \
                                      
                 |                     |
                 |        o   o        |
              .-.|        o   o        |,-.
              |(\| ?b._   o   o   _.dP |/)|
              |\d`. |`""=.__ __.=""'| .'6/|
              `.\_|  -.."_/   \_"..-  |_/,'
                `._\  --.. .   .---  /_,'
                    \      ___      /
Spray and Pray       `-.  "..."  .-'
                 ._ .-|.`-._ _.-'.|-. _.
             _.-/ .' '  \       /  ` `. \-._
        ..--"   . \..._).\_   _/.(_.../ .   "--..
       /\        \ |""--.._"="_..--""| /        /\
       
      |  \ .      \ `.     ===     .' .      . /  |
    ./    \ \       . `-.       .-'         / /    \.
    |_     `|         .  `-. ,-'            |'     _|
     /"-.   |           .   "               |   .-"\
     
    /    T-. \      \      ._      .--.    / .-T    |\
    						     
   .     |  "-\       .           /    |  /-"  |     .
   |     `    |.        - .     .("    / .|    '     |
   \   | ._  .'|              _.-".-",'  |`.  _. |   /
   ()  |   "(   `._________._..__Seal___.'  )"   |  ()
   (   `    \    (========( / /)========)   /    /   )
   """)


# Prompt user to start scanning
while True:
    choice = input("\033[0mDo you want to scan now? (yes/no): ")
    if choice == 'yes':
        # Create and start the threads
        threads = []
        clicks_per_thread = num_clicks // num_threads
        for i in range(num_threads):
            for url in urls:
                thread_num_clicks = clicks_per_thread if i < num_threads-1 else num_clicks-(clicks_per_thread*(num_threads-1))
                thread = threading.Thread(target=perform_click, args=(thread_num_clicks, url))
                threads.append(thread)
                thread.start()

        # Wait for all threads to finish
        for thread in threads:
            thread.join()

        print("\033[92m\033[1m") # Set color to lolcat rainbow
        print("Finished clicking", num_clicks, "times on", len(urls), "URLs.")
        break
    elif choice == 'no':
        print("\033[93m\033[1m") # Set color to lolcat rainbow
        print("Thank you, goodbye.")
        break
    else:
        print("\033[91m\033[1m") # Set color to lolcat rainbow
        print("Invalid choice. Please enter 'yes' or 'no'.")
        
