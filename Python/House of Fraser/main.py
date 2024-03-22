from bs4  import BeautifulSoup as Soup
import httpx
url = "https://www.imdb.com/list/ls058011111/"

headers = {
    "User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Mobile Safari/537.36"
}

url = "https://www.houseoffraser.co.uk/men/hoodies-and-sweatshirts#dcp=2&dppp=59&OrderBy=rank" 

response = httpx.get(url, headers=headers)
soup = Soup(response.content, "html.parser")
brand = soup.find_all(attrs={"class": "productdescriptionbrand"})
name = soup.find_all(attrs={"class": "productdescriptionname"}) 
price = soup.find_all(attrs={"class": "CurrencySizeLarge curprice"})  
print(brand[0].text)
print(price[0].text)
for item in range(59):
    print(f"The brand name is : {brand[item].text}, the name of the product is : {name[item].text}, and the price  is: {price[item].text}")

