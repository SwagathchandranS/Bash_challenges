import requests

url = "https://blog.bi0s.in/2024/01/05/Misc/Year-in-Review-2023/title.png"
response = requests.get(url)

if response.status_code == 200:
    with open("logo.png", "wb") as f:
        f.write(response.content)
    print("Image downloaded successfully as logo.png")
else:
    print(f"Failed to download the image. Status code: {response.status_code}")

