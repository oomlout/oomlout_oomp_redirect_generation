import time
import pyautogui
import clipboard

delay_shortest = 0.25
delay_short = 2
delay_long = 5

#make a main with kwargs
def main(**kwargs):
    directory_oomp_redirect = "redirect"
    
    yourl_admin = "http://oom.lt/admin"

    #open using start
    import os
    os.system(f"start {yourl_admin}")

    #prompt to login and wait
    input("Press enter when you have logged in")

    yourl_bulk_upload = "https://oom.lt/admin/plugins.php?page=vaughany_bias"
    os.system(f"start {yourl_bulk_upload}")

    index = 1
    run = True
    while run:
        file_redirect = f"{directory_oomp_redirect}\\redirect_{index}.csv"
        if os.path.exists(file_redirect):
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
            file_redirect_full = os.path.abspath(file_redirect)
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
                print(f"File {file_redirect} imported")
            else:
                #wait for input
                input("Press enter when you have resolved the issue")

            #send ctrl w
            pyautogui.hotkey('ctrl', 'w')
            time.sleep(delay_short)

            index += 1
        else:
            run = False



#call main
if __name__ == '__main__':
    kwargs = {}
    main(**kwargs)
