from bs4 import BeautifulSoup


with open(r"C:\Programming\Python\Python\web_scrapping\times.html", "r") as file:
    soup = BeautifulSoup(file.read(), "html.parser")

print(soup.find_all("div"))