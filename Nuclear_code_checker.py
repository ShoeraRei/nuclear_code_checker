import requests;
from bs4 import BeautifulSoup;

print("\nwe are not responsible if there are other parties who aim to misuse the nuclear code\n");
launch_code = input("enter the launch code :");
print('please wait checking code:'+launch_code+"....");
code_link =["https://nhentai.net/g/"+launch_code+"/","https://www.tsumino.com/entry/"+launch_code,"https://hentaifox.com/gallery/"+launch_code+"/","https://imhentai.com/gallery/"+launch_code+"/","https://asmhentai.com/g/"+launch_code+"/","https://hentai.cafe/hc.fyi/"+launch_code,"http://www.hbrowse.com/"+launch_code+"/c00001","https://1cak.com/"+launch_code];
q = 0;
t = 1;
#2216917
list_link = [];
list_title = [];
while q < len(code_link):
  code_request = requests.get(code_link[q]);
  code_soup = BeautifulSoup(code_request.content,"html.parser");
  if code_request.status_code == 200:
    if code_soup.title == None:
      print(str(t)+" nuclear server has encountered an error or use vpn");
    else:
      title = code_soup.title.text;
      list_link.append(code_link[q]);
      list_title.append(title);
  else:
    print(str(t)+" nuclear server has encountered an error or use vpn");
    t+=1;
  q+=1;
  
if list_link == None:
  print("your input wrong code");
else:
  e = 0;
  for w in list_title:
    print("\n"+str(e)+". "+list_title[e]);
    e+= 1;
  selected = int(input("\nselect : "))
  print("\nnuclear link : "+list_link[selected]);
  print("use the nuclear code wisely");