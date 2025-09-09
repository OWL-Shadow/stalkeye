from playwright.sync_api import sync_playwright
import re
import random
import time
from colorama import Fore, Style
import shutil
import os
import json
from datetime import datetime

social_media_patterns = {
    'linkedin': r"linkedin\.com/in/[\w-]+",
    'facebook': r"facebook\.com/[\w.-]+",
    'instagram': r"instagram\.com/[\w.-]+",
    'twitter': r"twitter\.com/[\w]+",
    'youtube': r"youtube\.com/(user/|channel/|@)[\w.-]+",
    'tiktok': r"tiktok\.com/@[\w.-]+",
    'snapchat': r"snapchat\.com/add/[\w.-]+"
}

blocked_domains = ['ads.google.com', 'doubleclick.net', 'googletagmanager.com']


def matrix_effect(duration=3, density=0.15):
    os.system("cls" if os.name == "nt" else "clear")  
    cols = shutil.get_terminal_size().columns
    streams = [0] * cols
    charset = "01"
    start = time.time()
    while time.time() - start < duration:
        line = []
        for i in range(cols):
            if streams[i] == 0 and random.random() < density:
                streams[i] = random.randint(3, 12)
            if streams[i] > 0:
                ch = random.choice(charset)
                line.append(ch)
                streams[i] -= 1
            else:
                line.append(" ")
        print(Fore.RED + "".join(line) + Style.RESET_ALL)
        time.sleep(0.05)
           
def print_disclaimer():
    os.system("clear")  
    disclaimer = f"""
{Fore.RED}╔══════════════════════════════════════════════════════════════════════════════╗
{Fore.RED}║                          ⚠️  IMPORTANT DISCLAIMER ⚠️                           ║
{Fore.RED}╠══════════════════════════════════════════════════════════════════════════════╣
{Fore.GREEN}║                                                                              ║
{Fore.GREEN}║  This OSINT (Open Source Intelligence) tool is provided for:                 ║
{Fore.GREEN}║                                                                              ║
{Fore.GREEN}║  • Educational purposes only                                                 ║
{Fore.GREEN}║  • Authorized security research                                              ║
{Fore.GREEN}║  • Ethical hacking with proper authorization                                 ║
{Fore.GREEN}║  • Personal security awareness                                               ║
{Fore.GREEN}║                                                                              ║
{Fore.RED}║  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ ║ 
{Fore.RED}║                                                                              ║
{Fore.RED}║  ❗ STRICTLY PROHIBITED:                                                     ║
{Fore.RED}║                                                                              ║
{Fore.RED}║  • Unauthorized scanning or data collection                                  ║
{Fore.RED}║  • Privacy violations                                                        ║
{Fore.RED}║  • Harassment or stalking                                                    ║
{Fore.RED}║  • Any illegal activities                                                    ║
{Fore.RED}║                                                                              ║
{Fore.RED}║  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ ║
{Fore.CYAN}║                                                                              ║
{Fore.CYAN}║  ⚖️  LEGAL COMPLIANCE:                                                        ║
{Fore.CYAN}║                                                                              ║
{Fore.CYAN}║  • You are responsible for complying with local laws                         ║
{Fore.CYAN}║  • Respect robots.txt and terms of service                                   ║
{Fore.CYAN}║  • Ensure proper authorization before scanning                               ║
{Fore.CYAN}║                                                                              ║
{Fore.GREEN}║  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━  ║
{Fore.GREEN}║                                                                              ║
{Fore.GREEN}║  The developer assumes no liability for misuse of this tool.                 ║
{Fore.GREEN}║  Use at your own risk and responsibility.                                    ║
{Fore.GREEN}║                                                                              ║
{Fore.GREEN}╚══════════════════════════════════════════════════════════════════════════════╝
{Style.RESET_ALL}

{Fore.GREEN}By continuing, you acknowledge that you:{Style.RESET_ALL}
{Fore.WHITE}• Have read and understand this disclaimer{Style.RESET_ALL}
{Fore.WHITE}• Will use this tool legally and ethically{Style.RESET_ALL}
{Fore.WHITE}• Accept full responsibility for your actions{Style.RESET_ALL}

"""
    print(disclaimer)
    

    response = input(f"{Fore.YELLOW}Do you accept these terms and wish to continue? (y/N): {Style.RESET_ALL}").strip().lower()
    if response != 'y':
        print(f"{Fore.RED}Operation cancelled. Exiting...{Style.RESET_ALL}")
        exit()

def intro():

    os.system("clear")  
    BANNER = r"""
   ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀  ⢀⣠⣤⣶⣶⣶⣶⣦⣤⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢦⣤⣤⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣦⣤⣤⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⣻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⣿⠟⠁⢀⣈⠙⢿⣿⣿⣿⠟⠁⢀⣈⠙⢿⣿⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣾⣿⠀⢻⣿⡿⠂⣸⣿⣿⣿⠀⢻⣿⡿⠀⣸⣿⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣷⣤⣄⣤⣴⣿⠁⠀⣻⣷⣤⣄⣤⣴⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⣿⣿⣿⣿⣿⣿⣿⣧⢠⣿⣿⣿⣿⣿⣿⣿⣿⣝⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣾⣿⣿⣿⣿⣿⣿⠟⣭⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣆⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣻⣻⣿⣿⠇⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⡀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⠿⢟⠿⢿⣿⡄⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⡄⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡿⡿⢿⣿⣿⣷⡈⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡄⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢿⣾⣷⣾⣿⣿⣷⣄⠙⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡄⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣮⣶⣭⣭⣛⣽⣿⣿⣦⣈⠙⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡄⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢷⣭⣯⣻⣝⣛⣿⣿⣿⣿⣶⣤⣉⠛⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⠀⠀
⠀⠀⠀⠀⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠹⣿⣛⣛⠿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣤⣉⡛⠿⣿⣿⣿⣿⣿⣿⣇⠀
⠀⠀⠀⠀⠈⠙⠷⣶⣤⣄⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⢿⡿⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣯⣽⣿⣿⣿⣿⡄
⠀⠀⠀⠀⠀⠰⣄⠀⣀⠉⠉⠛⠛⠷⠶⣦⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠻⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡏⠙⢿⣧
⠀⠀⠀⠘⠛⠓⢉⡄⡹⠆⠀⠀⠀⠀⠀⠉⠛⠿⢷⣶⣤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢻⣿⣿⣿⣿⡏⠛⠛⠛⠛⠛⠊⢿⣿⣿⠀⠀⠙
⠀⠀⠀⠀⠀⠀⠉⠛⠋⠢⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⢹⣿⣷⣦⣄⣀⡀⠀⠀⢀⣀⣼⣿⣿⣿⡿⠁⠀⠀⠀⠀⠀⠀⠈⢻⣿⡀⠀⠀
⠈⠉⠙⠒⠲⠶⠶⢶⣶⣤⣬⣽⣶⣦⣤⣤⣤⣶⣶⣿⡿⠿⠿⠟⠛⠿⠿⠏⣴⣿⣿⠟⣛⣛⣋⣀⣀⡀⠀⠀⡀⠀⠀⠀⠀⠹⡇⠀⠀
⠀⠀⠀⠀⢀⣠⠶⠛⠋⠉⠉⠁⠀⠈⠉⠉⠉⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠈⢏⠈⡏⠈⠛⠛⠻⠿⢿⣿⣿⣿⣿⣿⣶⣦⣤⣤⠑⠀⠀
⠀⠀⠀⠐⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠉⠛⠻⠿⣿⡇⠀⠀⠀
    """ 
    print(Fore.GREEN  + f"{BANNER}" + Style.RESET_ALL)
    print(Fore.GREEN  + "I often feel that night and shadow are more alive than day and light...." + Style.RESET_ALL)
    print(Fore.RED + "Welcome ,night wanderer !!" + Style.RESET_ALL)
    print(Fore.RED + "By OWL-Shadow\n\n\n" + Style.RESET_ALL)
def filter_url(url , filtered_urls):
    domain = re.findall(r'https?://(?:www\.)?([^/]+)', url)
    if domain:
         domain = domain[0].lower()
         if not any(blocked in domain for blocked in blocked_domains):
             filtered_urls.append(url)
                        
def extract_phones(text):
   
    intl_pattern = r"\+\d{1,4}[\s\(-]?\d{1,6}[\s\)-]?\d{1,6}[\s-]?\d{1,6}\b"
    
    local_pattern = r"\b0[5-7][\s-]?\d{2}[\s-]?\d{2}[\s-]?\d{2}[\s-]?\d{2}\b"

    intl_phones = re.findall(intl_pattern, text)
    local_phones = re.findall(local_pattern, text)
    

    cleaned_phones = []
    for phone in intl_phones + local_phones:
       
        cleaned = re.sub(r'\s+', ' ', phone)  
        cleaned = re.sub(r'[\s-]+$', '', cleaned)  
        cleaned_phones.append(cleaned)
    
    return cleaned_phones

def extract_emails(text):
    return re.findall(r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+", text)

def extract_dates(text):
    return re.findall(r"\b\d{2}[-/.]\d{2}[-/.]\d{4}\b", text)

def extract_files(text):
    return re.findall(r'https?://[^\s]+\.(pdf|txt|docx?|xlsx?|zip|rar)', text, re.IGNORECASE)

def extract_media(url ,text):
    found_profiles = []
    for platform , pattern in social_media_patterns.items():
       
        if re.search(pattern, url):
            found_profiles.append(url)
       
        matches = re.findall(pattern, text)
        for match in matches:
            full_url = f"https://{match}"
            found_profiles.append(full_url)
    return found_profiles

def check_url(url):
    pattern = r"https?://(?:www\.|dz)?(linkedin\.com|facebook\.com|instagram\.com|snapchat\.com)/[^\s]+"
    return bool(re.match(pattern, url))

def check_file(url):
    pattern = r"[a-zA-Z0-9_.+-]+\.(pdf|txt|docx|csv|xls|xlsx|zip|rar)$"
    return bool(re.search(pattern, url))

def main():
  filtered_urls = []
  all_emails = []
  all_phones = []
  all_medias = []
  all_dates = []
  all_files = []
  with sync_playwright() as p:
    
    username = input("enter the target name :").strip()
    print("start searching...")
    browser = p.chromium.launch(
    headless=True,
    args=[
        '--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome120.0.0.0 Safari/537.36'
    ] )
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://duckduckgo.com/", timeout=300000)
    page.wait_for_selector('input[name="q"]', timeout=100000)
    page.fill('input[name="q"]', username)
    page.wait_for_timeout(2000)
    page.keyboard.press("Enter")
    page.wait_for_timeout(30000)

    links = page.query_selector_all("li div h2 a")
    urls = [link.get_attribute("href") for link in links if link.get_attribute("href")]

    print(Fore.GREEN + f"Found {len(urls)} results:" + Style.RESET_ALL)
    for url in urls:
        print(Fore.WHITE + url + Style.RESET_ALL)
   
    for url in urls:
        filter_url(url , filtered_urls)

    for url in filtered_urls:

        new_page = context.new_page()

        if check_url(url):
            print(Fore.CYAN  + "social media found :" + Style.RESET_ALL)
            print(Fore.GREEN + url + Style.RESET_ALL)

        if check_file(url):
            print(Fore.CYAN + "files found :" + Style.RESET_ALL)
            print(Fore.GREEN + url + Style.RESET_ALL)

        try:
            new_page.goto(url, timeout=30000)
            visible_text = new_page.evaluate("""() => {
                return document.body.innerText;
            }""")

            emails = extract_emails(visible_text)
            phones = extract_phones(visible_text)
            dates = extract_dates(visible_text)
            files = extract_files(visible_text)
            medias = extract_media(url , visible_text)

            if emails or phones or dates or files or medias:
                print(Fore.GREEN + f"\ninformations found in {url} :" + Style.RESET_ALL)

                if emails:
                    emails = list(set(emails))
                    all_emails.extend(emails)
                    print(Fore.CYAN + "emails :" + Style.RESET_ALL)
                    for email in emails:
                        print(Fore.WHITE + email + Style.RESET_ALL)

                if dates:
                    dates = list(set(dates))
                    all_dates.extend(dates)
                    print(Fore.CYAN + "dates :" + Style.RESET_ALL)
                    for date in dates:
                        print(Fore.WHITE + date + Style.RESET_ALL)

                if phones:
                    phones = list(set(phones))
                    all_phones.extend(phones)
                    print(Fore.CYAN + "phones :" + Style.RESET_ALL)
                    for phone in phones:
                        print(Fore.WHITE + phone + Style.RESET_ALL)

                if files:
                    files = list(set(files))
                    all_files.extend(files)
                    print(Fore.CYAN + "files :" + Style.RESET_ALL)
                    for fil in files:
                        print(Fore.WHITE + fil + Style.RESET_ALL)

                if medias:
                    medias = list(set(medias))
                    all_medias.extend(medias)
                    print(Fore.CYAN+ "accounts :" + Style.RESET_ALL)
                    for media in medias:
                        print(Fore.WHITE + media + Style.RESET_ALL)

        except Exception as e:
            print(Fore.RED + f"Error visiting {url}: {e}" + Style.RESET_ALL)

        new_page.close()
        time.sleep(random.uniform(2, 6))

    browser.close()

    results = {
    'target': username,
    'timestamp': datetime.now().isoformat(),
    'total_urls_processed': len(filtered_urls),
    'emails': list(set(all_emails)),
    'phones': list(set(all_phones)),
    'social_media': list(set(all_medias)),
    'dates': list(set(all_dates)),
    'files': list(set(all_files))  
     }
    
    with open(f'results_{username}_{datetime.now().strftime("%Y%m%d")}.json', 'w') as f:
      json.dump(results, f, indent=2)


if __name__ == "__main__":
    matrix_effect(duration=3, density=0.15)
    print_disclaimer()
    intro()
    main()    