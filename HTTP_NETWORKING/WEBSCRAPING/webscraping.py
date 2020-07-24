#pip install requests 
#pip install lxml
#pip install bs4 (beautiful soup version 4) grab infromation from htm docuuments
#lxml parser
import requests as req
import bs4
#using the req.get () to get the sites source
res=req.get("https://en.wikipedia.org/wiki/Jonas_Salk")
soup=bs4.BeautifulSoup(res.text,"lxml")
#selecting a p tag
print(soup.select("p")[1].getText())
#selecting a h1 tag
print(soup.select("h1")[0].getText())

#slecting with class name
print("\nItem list from site-:\n")
for item in soup.select(".toctext"):
    print(item.getText())

#selecting the image
img_url=soup.select(".thumbimage")[0]["src"]
#downloading the image into a file
img_src=req.get("https:"+img_url)
f=open("image.jpg","wb")
f.write(img_src.content)
f.close()