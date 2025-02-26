import requests

url = "https://zirtech.site/identifiers/mushrooms/identify.php"
image_path = "/Users/ksenia/Developer/3.1 Проекты тестовые/ДЗ/homework/image12.jpg"

with open(image_path, 'rb') as img_file:
    files = {'image': img_file}
    response = requests.post(url, files=files)

print(response.text)