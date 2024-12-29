import time
import pyautogui
import clipboard

import os

delay_shortest = 0.25
delay_short = 2
delay_long = 5

#make a main with kwargs
def main(**kwargs):
    directory_oomp_redirect = "redirect"
    #make if not exists
    if not os.path.exists(directory_oomp_redirect):
        os.makedirs(directory_oomp_redirect)
    directory_oomp_redirect_split = "temporary"
    #make if not exists
    if not os.path.exists(directory_oomp_redirect_split):
        os.makedirs(directory_oomp_redirect_split)

    
    yourl_admin = "http://oom.lt/admin"

    #open using start

    os.system(f"start {yourl_admin}")

    #try to login
    if True:
        print("Trying to login")
        #wait 10 seconds
        time.sleep(10)

        #tab twoce
        pyautogui.hotkey('tab')
        time.sleep(delay_shortest)
        pyautogui.hotkey('tab')
        time.sleep(delay_shortest)

        #press enter
        pyautogui.hotkey('enter')
        print("    waiting for login")
        time.sleep(10)

        #select all
        pyautogui.hotkey('ctrl', 'a')
        time.sleep(delay_short)
        #copy
        pyautogui.hotkey('ctrl', 'c')
        time.sleep(delay_short)
        #check for
        string_check = "Admin interface"
        if string_check in clipboard.paste():
            print("Logged in")
        else:
            #prompt to login and wait
            input("Press enter when you have logged in")

    yourl_bulk_upload = "https://oom.lt/admin/plugins.php?page=vaughany_bias"
    os.system(f"start {yourl_bulk_upload}")

    file_redirect = f"{directory_oomp_redirect}\\redirect_1.csv"
    file_redirect_uploaded = f"{directory_oomp_redirect}\\redirect_uploaded_1.csv"

    #load the file
    count = 1
    index = 1
    
    #spliting redirect.csv_1 and checking for duplicates
    if True:
        #load uploaded ones into an array
        uploaded_lines = []
        if os.path.exists(file_redirect_uploaded):
            with open(file_redirect_uploaded, 'r') as f:
                for line in f:
                    uploaded_lines.append(line)
        with open(file_redirect, 'r') as f:
            redirect_split_base = f"{directory_oomp_redirect_split}\\redirect_{index}.csv"
            for line in f:
                #test if it has already been uploaded
                if line in uploaded_lines:
                    pass
                    #print(f"Skipping line {line} as it has already been uploaded")                    
                    #print(",", end="", flush=True)
                else:
                    if count == 1:
                        with open(redirect_split_base, 'w') as f_split:
                            f_split.write(line)
                    else:
                        with open(redirect_split_base, 'a') as f_split:
                            f_split.write(line)
                    #print(".", end="", flush=True)  
                    count += 1
                    if count > 500:
                        #make a string variable with tthe count value                
                        count = 1
                        index += 1
                        status_string = f"writing file {index}"
                        print(status_string) 
                        redirect_split_base = f"{directory_oomp_redirect_split}\\redirect_{index}.csv"

    index = 1
    run = True
    while run:
        file_redirect_current = f"{directory_oomp_redirect_split}\\redirect_{index}.csv"
        if os.path.exists(file_redirect_current):
            os.system(f"start {yourl_bulk_upload}")
            time.sleep(delay_long)
            #tab 9 times
            for i in range(9):
                pyautogui.hotkey('tab')
                time.sleep(delay_shortest)
            #enter
            pyautogui.hotkey('enter')
            time.sleep(delay_short)
            #type file path
            #get full filename for file_redirect
            file_redirect_full = os.path.abspath(file_redirect_current)
            pyautogui.write(file_redirect_full)
            time.sleep(delay_short)
            #enter
            pyautogui.hotkey('enter')
            time.sleep(delay_short)
            #tab once
            pyautogui.hotkey('tab')
            time.sleep(delay_short)
            #enter
            pyautogui.hotkey('enter')
            time.sleep(delay_long)

            #select all
            pyautogui.hotkey('ctrl', 'a')
            time.sleep(delay_short)
            #copy
            pyautogui.hotkey('ctrl', 'c')
            time.sleep(delay_short)
            #check for 
            string_check = "URLs imported"
            if string_check in clipboard.paste():
                print(f"File {file_redirect_current} imported")
            else:
                #wait for input
                input("Press enter when you have resolved the issue")

            #send ctrl w
            pyautogui.hotkey('ctrl', 'w')
            time.sleep(delay_short)

            index += 1
        else:
            run = False

    #add all the uploaded redirects to redirect/redirect_uploaded_1.csv
    if True:
        print("Adding all uploaded redirects to redirect_uploaded_1.csv")
        
        #load in redirect_1.csv
        #read all lines into an array
        lines = []
        
        if os.path.exists(file_redirect):
            print(f"    File {file_redirect} exists")   
            with open(file_redirect, 'r') as f:
                for line in f:
                    lines.append(line)
            lines_uploaded = []
            with open(file_redirect_uploaded, 'w') as f:
                for line in lines:
                    lines_uploaded.append(line)
            #if line isn't in lines_uploaded add it
            if not line in lines_uploaded:
                lines_uploaded.append(line)
            #write to file
            with open(file_redirect_uploaded, 'w') as f:
                for line in lines_uploaded:
                    f.write(line)
        else:
            print(f"    File {file_redirect} does not exist")

        
    #delete the redirect csvs in temporary
    for i in range(1, index):
        file_redirect = f"{directory_oomp_redirect_split}\\redirect_{i}.csv"
        if os.path.exists(file_redirect):
            print(f"deleting temporary file {i}")
            os.remove(file_redirect)
    


#call main
if __name__ == '__main__':
    kwargs = {}
    main(**kwargs)
