[![Python Version](https://img.shields.io/badge/python-3.7%2B-blue)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Open Source Love](https://badges.frapsoft.com/os/v2/open-source.svg?v=103)](https://github.com/OWL-Shadow/stalkeye)

 -----------------------------------------------------StalkEye - OSINT Intelligence Tool -----------------------------------------------------

StalkEye is a powerful Python-based OSINT (Open Source Intelligence) tool designed for ethical security research and digital footprint analysis. It automates the process of searching for a target username across the web using DuckDuckGo, then systematically scans the discovered URLs to extract valuable information such as email addresses, phone numbers, social media profiles, and more.


Disclaimer:
This tool is intended for authorized security assessments, educational purposes, and personal security awareness only. Misuse of this tool for unauthorized scanning, harassment, or any illegal activities is strictly prohibited.

Features :

o Search Automation: Automatically queries DuckDuckGo for a given username.
 
o Advanced Data Extraction: Parses web pages to find and extract:
	Email Addresses
 	Phone Numbers (International and local formats)
 	Social Media Profiles (LinkedIn, Facebook, Instagram, Twitter/X, YouTube, TikTok, Snapchat)
 	Dates
 	Files (PDF, TXT, DOC, XLS, ZIP, RAR)

o Smart Filtering: Filters out ads and tracking domains to focus on relevant results.

o JSON Reporting: Saves all findings in a structured JSON file for further analysis.

o Stealthy Operation: Uses Playwright with a real Chrome user-agent for reliable scraping.

Ethical First: Includes a mandatory interactive disclaimer to ensure responsible use.

 -----------------------------------------------------⚠️ Legal & Ethical Disclaimer⚠️ -----------------------------------------------------
By using StalkEye, you agree to the following:

You will use this tool only on targets you have explicit permission to test.

You will comply with all applicable laws and regulations in your country.

You will respect robots.txt files and the Terms of Service of scanned websites.

The developer (Nyx-Shadow) is not responsible for any misuse or damage caused by this tool.

This tool is for educational and authorized security research purposes ONLY.

You are solely responsible for your actions.
 
-----------------------------------------------------Installation -----------------------------------------------------
1. Clone the Repository
bash
git clone https://github.com/OWL-Shadow/stalkeye.git
cd stalkeye
2. Install Python Dependencies
Ensure you have Python 3.7+ installed. Then, install the required libraries:

bash
pip install -r requirements.txt

3. Install Playwright Browsers
This tool uses Playwright to control a Chromium browser. Install it with:

bash
playwright install chromium

Usage
Run the tool:

bash
python stalkeye.py
Read and Accept the Disclaimer: You must agree to the terms to continue.

Enter the Target Username: When prompted, input the username you want to investigate.

Wait for Analysis: The tool will automatically search, visit links, and extract information. This may take several minutes.

Review Results: Findings will be printed to the console in real-time and saved to a JSON file (e.g., results_johndoe_20250909.json) in the same directory.
													
----------------------------------------------------- Technical Overview  -----------------------------------------------------
Language: Python 3

Core Libraries:

playwright: For browser automation and web scraping.

colorama: For colored terminal output.

re: For regex-based data extraction.

Patterns: Uses custom regular expressions to identify and validate data points.

🤝 Contributing
Contributions are welcome! Please feel free to submit a Pull Request.


📜 License
This project is licensed under the MIT License - see the LICENSE.txt file for details.

 Acknowledgments :
Inspired by the need for accessible OSINT tools for ethical security practices.

Built with the powerful Playwright framework.

Thanks to the open-source community for continuous support and inspiration.





Happy (and ethical) hunting!!
