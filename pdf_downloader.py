import requests

file_path = r"C:\projects\newspaper_to_modern_articles\URL.txt"  # Update with the file path containing the URLs
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36"
}

with open(file_path, "r") as file:
    pdf_urls = [line.strip() for line in file.readlines()]
i = 1
for url in pdf_urls:
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        file_name = str(i) + '__' + url.split("/")[-2] + ".pdf"
        print("file_name: ", file_name)
        with open(file_name, 'wb') as file:
            file.write(response.content)
        print(f"Downloaded {file_name} successfully!")
    else:
        print(f"Failed to download {url}")
        continue
    i += 1
