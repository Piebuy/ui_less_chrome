import subprocess
import os

CHROME_PATH_FILENAME = 'ui_less_chrome_path.txt'
DEFAULT_WEBSITE_FILENAME = 'ui_less_settings.txt'
SAVED_URLS_FILENAME = 'ui_less_saved_urls.txt'

def main():
    chrome_path = read_default_website(CHROME_PATH_FILENAME)
    url = ''
    
    while True:
        clear_screen()
        default_website = read_default_website(DEFAULT_WEBSITE_FILENAME)
        c_path_set = 'Path not set' if chrome_path == '' or chrome_path == None else 'Path set'
        print(f"-- Opens Chrome UI less --      Default Website: {default_website}      Chrome Path: {c_path_set}\n")
        print("Paste website and press enter or write nothing to use default website (--i for incognito mode)")
        print("Type s to set default website")
        print("Type p to set path to your chrome.exe")
        url = input("\nPaste website here: ")

        if url == "":
            url = default_website
            break
        elif url.lower() == 's':
            setting = input('Set default website: ')
            url = add_www_https(setting)
            save_default_website(url,DEFAULT_WEBSITE_FILENAME)
        elif url.lower() == 'p':
            setting = input('Set chrome.exe path: ')
            setting = setting[1:-1] if setting.startswith('"') and setting.endswith('"') else setting
            setting = setting[0:-1] if setting.endswith('\\') else setting
            setting = setting + '\\chrome.exe' if not setting.endswith('chrome.exe') else setting
            save_default_website(setting,CHROME_PATH_FILENAME)
            chrome_path = read_default_website(CHROME_PATH_FILENAME)

        else:
            url = 'www.' + url if not "www." in url and "https://" not in url else url
            url = 'https://' + url if not "https://" in url else url
            break
    if '--i' in url: # type: ignore
        url = url.replace(' --i','').replace('--i','') # type: ignore
        subprocess.Popen([chrome_path, "--incognito", f"--app={url}"]) # type: ignore
    else:
        subprocess.Popen([chrome_path, f"--app={url}"]) # type: ignore
    
def add_www_https(url):
    url = 'www.' + url if not "www." in url else url
    url = 'https://' + url if not "https://" in url else url
    return url

def save_default_website(url,filename):
    script_dir = os.path.dirname(os.path.abspath(__file__))
    filepath = os.path.join(script_dir, filename)
    with open(filepath, 'w') as file:
        file.write(url)

def read_default_website(filename):
    script_dir = os.path.dirname(os.path.abspath(__file__))
    filepath = os.path.join(script_dir, filename)
    if os.path.exists(filepath):
        with open(filepath, 'r') as file:
            return file.read()
def clear_screen():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def save_list_of_urls(urls, filename):
    script_dir = os.path.dirname(os.path.abspath(__file__))
    filepath = os.path.join(script_dir, filename)
    with open(filepath, 'w') as file:
        for url in urls:
            file.write(url + '\n')
def load_list_of_urls(filename):
    script_dir = os.path.dirname(os.path.abspath(__file__))
    filepath = os.path.join(script_dir, filename)
    urls = []
    if os.path.exists(filepath):
        with open(filepath, 'r') as file:
            for line in file:
                urls.append(line.strip())
    return urls
if __name__=='__main__':
    try:
        main()
    except Exception as e:
        try:
            print()
            print(e)
        finally:
            input("\nPress Enter to close...")