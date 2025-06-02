from bs4 import BeautifulSoup

# Load the HTML file
with open("product.html", "r", encoding="utf-8") as file:
    html_content = file.read()

# Parse HTML with BeautifulSoup
soup = BeautifulSoup(html_content, "html.parser")

# Find the table
table = soup.find("table")

# Extract table headers
headers = [th.text.strip() for th in table.find_all("th")]

# Extract table rows
rows = []
for tr in table.find_all("tr")[1:]:  # Skip the header row
    cells = tr.find_all("td")
    if cells:
        row = [td.text.strip() for td in cells]
        rows.append(row)

# Print headers and rows
print("Headers:", headers)
print("Rows:")
for row in rows:
    print(row)
