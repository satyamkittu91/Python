from bs4 import BeautifulSoup

with open("file.html", "r", encoding="utf-8") as file:
    html = file.read()

soup = BeautifulSoup(html, "html.parser")

#Returns html in a pretty format
print(soup.prettify())

# Find all <h5> tags
h5_tags = soup.find_all("h5")

# Print the text of each <h5> tag
for h5 in h5_tags:
    print(h5.get_text(strip=True))