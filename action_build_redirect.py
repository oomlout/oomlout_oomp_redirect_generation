import os


def main(**kwargs):

    force_data_update = False

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
    ids.append("md5_6")
    ids.append("md5_6_alpha")
    ids.append("part_number")
    ids.append("bip_39_word_no_space_2")
    ids.append("bip_39_word_underscore_2")
    ids.append("bip_39_word_dash_2")
    ids.append("bip_39_word_no_space_3")
    ids.append("bip_39_word_underscore_3")
    ids.append("bip_39_word_dash_3")
    


    redirects = []

    for part_id in oomp:
        part = oomp[part_id]
        for id in ids:
            if id in part:
                try:
                    short_link = part[id]
                    url = part["link_main"]
                    title = part["name"]
                    redirect = {
                        "short_link": short_link,
                        "url": url,
                        "title": title
                    }
                    import copy
                    if short_link != "":
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
        
        
        

    




if __name__ == '__main__':
    kwargs = {}
    main(**kwargs)