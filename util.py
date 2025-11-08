import subprocess
import os

SETTINGS_FILE_NAME = 'ui_less_settings.txt'
SAVED_URLS_FILENAME = 'ui_less_saved_urls.txt'

def save_settings(settings):
    script_dir = os.path.dirname(os.path.abspath(__file__))
    filepath = os.path.join(script_dir, SETTINGS_FILE_NAME)
    with open(filepath, 'w') as file:
        for key, value in settings.items():
            file.write(f"{key}={value}\n")
def load_settings():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    filepath = os.path.join(script_dir, SETTINGS_FILE_NAME)
    settings = {}
    if os.path.exists(filepath):
        with open(filepath, 'r') as file:
            for line in file:
                if '=' in line:
                    key, value = line.strip().split('=', 1)
                    settings[key] = value
    return settings
def check_settings_exist():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    filepath = os.path.join(script_dir, SETTINGS_FILE_NAME)
    if not os.path.exists(filepath):
        default_settings = {
            'default_website': 'https://www.google.com',
            'chrome_path': ''
        }
        save_settings(default_settings)
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

def add_www_https(url):
    url = 'www.' + url if not "www." in url else url
    url = 'https://' + url if not "https://" in url else url
    return url

def is_valid_chrome_path(path):
    """Check if the given path points to a valid chrome.exe file."""
    return os.path.isfile(path) and os.path.basename(path).lower() == "chrome.exe"
def check_args(args):
    
    if len(args) == 0:
        url_arguments = input("\nPaste website here: ").split()
    else:
        url_arguments = [arg for arg in args]
        if '--url' in args:
            for i, arg in enumerate(args):
                if arg == '--url':
                    url_arguments.insert(0, args[i+1])
                    url_arguments.pop(i+2)
                    url_arguments.pop(i+1)
                    break
        else:
            url_arguments.insert(0, '')
    
    return url_arguments