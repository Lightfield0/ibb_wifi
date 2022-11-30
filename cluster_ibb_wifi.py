import json,folium,requests,webbrowser
from numpy import append
from folium.plugins import MarkerCluster

adres="https://data.ibb.gov.tr/api/3/action/datastore_search?resource_id=5d0a0b1e-9e56-4038-b966-7d3e7b46f882&limit=150"

lokasyonlar = []

harita=folium.Map(location=[41.1,28.9],zoom_start=10)
wifiloc=json.loads(requests.get(adres).text)

for wifid in range(150):
    wifi=wifiloc["result"]["records"][wifid]
    ad=wifi["LOCATION_CODE"]
    enlem=wifi["LATITUDE"]
    boylam=wifi["LONGITUDE"]
    loc=wifi["LOCATION_GROUP"]
    mahalle=wifi["LOCATION"]

    info= popup=ad+"<br>"+mahalle

    if loc== "Kutuphane":
        color="green"
        icon="book"
    elif loc ==  "Kultur Merkezi":
        color="beige"
        icon="landmark-dome"
    elif loc == "Ismek":
        color="blue"
        icon="graduation-cap"
    elif loc=="Hizmet Binasi":
        color="red"
        icon="building"
    elif loc=="Metrobus Duragi":
        color="orange"
        icon="bus"
    elif loc=="Sehir Hatlari Iskelesi":
        color="black"
        icon="anchor"
    #folium.Marker(location=[enlem,boylam],popup=info,tooltip=ad,icon=folium.Icon(color=color,prefix="fa",icon=icon)).add_to(harita)
            

    lokasyonlar.append((enlem,boylam))

akdenizilleri = MarkerCluster(locations=lokasyonlar)
harita.add_child(akdenizilleri)

harita.save("tr_manuel_akdeniz.html")
webbrowser.open("tr_manuel_akdeniz.html")
