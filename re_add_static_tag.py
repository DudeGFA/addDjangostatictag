from bs4 import BeautifulSoup
import re

# Define the name of the HTML file to modify
html_file = "re_testfile.html"

# Define the base URL for your Django project
base_url = "https://example.com/"

# Define the path to your static directory
static_dir = "static/"

# Open the HTML file and read its contents
with open(html_file, "r") as f:
    soup = BeautifulSoup(f, "html.parser")

# Find all the href, poster, onclick, url(), and src attributes and update them with the appropriate Django static tag
for tag in soup.find_all():
    if tag.has_attr("href"):
        tag["href"] = re.sub(r'(?<=\bhref=["\'])/?(?!http|ftp)(.+?)\.(css|js|png|jpe?g|gif)(?=["\'])', f"{{% static '{static_dir}\\g<1>.\\g<2>' %}}", tag["href"])
    if tag.has_attr("poster"):
        tag["poster"] = re.sub(r'(?<=\bposter=["\'])/?(?!http|ftp)(.+?)\.(jpe?g|png)(?=["\'])', f"{{% static '{static_dir}\\g<1>.\\g<2>' %}}", tag["poster"])
    if tag.has_attr("onclick"):
        tag["onclick"] = re.sub(r'(?<=\bonclick=["\'])/?(?!http|ftp)(.+?)\.(js)(?=["\'])', f"{{% static '{static_dir}\\g<1>.\\g<2>' %}}", tag["onclick"])
    if tag.has_attr("style"):
        tag["style"] = re.sub(r'(?<=\burl\(["\'])/?(?!http|ftp)(.+?)\.(jpe?g|png|gif)(?=["\'])', f"{{% static '{static_dir}\\g<1>.\\g<2>' %}}", tag["style"])
    if tag.name == "script" and tag.has_attr("src"):
        tag["src"] = re.sub(r'(?<=\bsrc=["\'])/?(?!http|ftp)(.+?)\.(js)(?=["\'])', f"{{% static '{static_dir}\\g<1>.\\g<2>' %}}", tag["src"])

# Write the modified HTML back to the file
with open(html_file, "w") as f:
    f.write(str(soup))
