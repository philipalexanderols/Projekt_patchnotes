from html.parser import HTMLParser
import urllib.request

readData = False
filename = ""
class MyHTMLParser(HTMLParser): 

    def handle_starttag(self, tag, attrs):
        if tag == "p" or tag == "div":
            if(attrs):
               
                attr_name = [x[1] for x in attrs][0]
                if(attr_name == "name" or attr_name == "god--name"):
                    global readData
                    readData = True
 
        if(tag == "img"):
            if(attrs):
                attr = [x[1] for x in attrs]
                name = ""
                if(len(attr) > 1):
                    name = attr[1]
                    save_image(attr[0], name)
                else:
                    global filename
                    filename = attr[0]
                

    def handle_data(self, data):
        global readData
        if readData:
            print(data)
            global filename
            save_image(filename, data)
            filename = ""
            readData = False

    
def save_image(pic_url, name):
    urllib.request.urlretrieve(pic_url, "images/"+name+".png")
    
parser = MyHTMLParser()
infil = open("SmiteNotes.html", "r", encoding="utf-8")
for line in infil:
    clean_line = line.strip() 
    parser.feed(clean_line)




infil.close()