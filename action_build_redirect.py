import os
import time

def main(**kwargs):

    #store start time
    time_start = time.time()

    force_data_update = False
    force_data_update = True

    import action_build_oomp
    if force_data_update:
        action_build_oomp.main(**kwargs)

    file_oomp_pickle = "temporary/parts.pickle"
    #make it if it doesn't exist in one line
    
    if not os.path.exists(file_oomp_pickle):
        action_build_oomp.main(**kwargs)

    directory_oomp_redirect = "redirect"

    #import oomp from the pickle file
    import pickle
    with open(file_oomp_pickle, 'rb') as file:
        oomp = pickle.load(file)

    #build the redirect files
    if not os.path.exists(directory_oomp_redirect):
        os.mkdir(directory_oomp_redirect)


    ids = []
    ids.append("id")
    ids.append("short_code")
    ids.append("oomlout_short_code")
    ids.append("md5_6")
    ids.append("md5_6_alpha")
    ids.append("part_number")
    ids.append("bip_39_word_no_space_2")
    ids.append("bip_39_word_underscore_2")
    ids.append("bip_39_word_dash_2")
    ids.append("bip_39_word_no_space_3")
    ids.append("bip_39_word_underscore_3")
    ids.append("bip_39_word_dash_3")
    ids.append("link_buy")
    for i in range(1, 10):
        ids.append(f"link_short_{i}")
    


    redirects = []

    for part_id in oomp:
        part = oomp[part_id]
        for id in ids:
            if id in part:
                try:
                    short_link = part[id]                    
                    url = part["link_main"]
                    if "link_redirect" in part:
                        url = part["link_redirect"]
                    title = part["name"]
                    redirect = {
                        "short_link": short_link,
                        "url": url,
                        "title": title
                    }
                    import copy
                    if short_link != "":
                        redirects.append(copy.deepcopy(redirect))
                        if "link_buy" in part:
                            redirect = copy.deepcopy(redirect)                            
                            redirect["url"] = part["link_buy"]
                            redirect["short_link"] = f"buy_{short_link}"
                            redirects.append(copy.deepcopy(redirect))
                except Exception as e:
                    print(f"Error with part {part_id}")
                    print(e)


    
    redirect_per_file = 500000
    index_file = 1
    file_redirect = f"{directory_oomp_redirect}\\redirect_{index_file}.csv"
    #write the redirect files
    file = open(file_redirect, 'w')
    index = 1
    for redirect in redirects:
        if index % redirect_per_file == 0 and index != 0:
            file.close()
            index_file += 1
            file_redirect = f"{directory_oomp_redirect}\\redirect_{index_file}.csv"
            file = open(file_redirect, 'w')
            print(f"Creating file {file_redirect}")
        line = ""
        #add long url
        url = redirect["url"]
        short_link = redirect["short_link"]
        title = redirect["title"]
        line += f'{url},'
        #add short url
        line += f'{short_link},'
        #add title
        line += f'{title}'
        #add new line
        line += '\n'
        file.write(line)
        index += 1
    file.close()
    
    time_end = time.time()
    time_taken = time_end - time_start    
    time_taken_minute_second = time.strftime("%M:%S", time.gmtime(time_taken))
    print(f"Time taken: {time_taken_minute_second}")

    
        

    




if __name__ == '__main__':
    kwargs = {}
    main(**kwargs)