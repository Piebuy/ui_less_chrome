from util import *

def main():
    settings = load_settings()
    chrome_path = settings.get('chrome_path','')
    url = settings.get('default_website','')
    
    while True:
        arguments = []
        settings = load_settings()
        chrome_path = settings.get('chrome_path','')

        clear_screen()
        default_website = settings.get('default_website','')
        c_path_set = "Not a valid Chrome path" if not is_valid_chrome_path(chrome_path) else 'True'
        print(f"-- Opens Chrome UI less --      Default Website: {default_website}      Chrome Path Set: {c_path_set}\n")
        print("Paste website and press enter or write nothing to use default website.")
        print("Type 'dw' to set default website, 'cp' to set chrome.exe path, 'l' to list saved URLs")
        print("argument '--a' to add URL to saved URLs when opening, --i for incognito mode\n")
        url_arguments = input("\nPaste website here: ").split()
        url = url_arguments[0] if len(url_arguments) > 0 else ""
        arguments = url_arguments[1:] if len(url_arguments) > 1 else []

        if url == "":
            url = default_website
        elif url.lower().strip() == 'dw':
            setting = input('Set default website, press enter to go back: ')
            if setting != "":
                url = add_www_https(setting)
                settings['default_website'] = url
                save_settings(settings)
                continue

        elif url.lower().strip() == 'cp':
            setting = input('Set chrome.exe path, press enter to go back: ')
            if setting == "":
                continue
            setting = setting[1:-1] if setting.startswith('"') and setting.endswith('"') else setting
            setting = setting[0:-1] if setting.endswith('\\') else setting
            setting = setting + '\\chrome.exe' if not setting.endswith('chrome.exe') else setting
            settings['chrome_path'] = setting
            save_settings(settings)
            chrome_path = settings['chrome_path']
            continue

        elif url.lower() == 'l':
            saved_urls = load_list_of_urls(SAVED_URLS_FILENAME)
            print("\n-- Saved URLs --")
            for i, saved_url in enumerate(saved_urls):
                print(f"{i+1}. {saved_url}")
            choice = input("\nType the number of the URL to open it, type number + d to delete it, or press enter to go back: ")
            if choice.isdigit():
                index = int(choice) - 1
                if 0 <= index < len(saved_urls):
                    url = saved_urls[index]
            elif choice.endswith('d'):
                index = int(choice[:-1]) - 1
                if 0 <= index < len(saved_urls):
                    saved_urls.pop(index)
                    save_list_of_urls(saved_urls, SAVED_URLS_FILENAME)
                continue
            else:
                continue

        url = add_www_https(url)
        if '--a' in arguments:
            saved_urls = load_list_of_urls(SAVED_URLS_FILENAME)
            if url not in saved_urls:
                saved_urls.append(url)
                save_list_of_urls(saved_urls, SAVED_URLS_FILENAME)

        try:
            if '--i' in arguments: # type: ignore
                url = url.replace(' --i','').replace('--i','') # type: ignore
                subprocess.Popen([chrome_path, "--incognito", f"--app={url}"]) # type: ignore
            else:
                subprocess.Popen([chrome_path, f"--app={url}"]) # type: ignore
            break

        except Exception as e:
            print(f"\nError: Could not open Chrome. {e}")
            print("Make sure the chrome.exe path is set correctly.")
            input("\nPress Enter to continue...")

if __name__ == "__main__":
    check_settings_exist()
    main()