import base64
import os


import folium
import geocoder
import ipywidgets
import mysql.connector
# create map object
from Tools.scripts.dutree import display
from branca.element import IFrame

#map.secret_key = 'your secret key'
from folium import plugins

conn = mysql.connector.connect(host="localhost", user="root", password="BarbuJonel1226", database='autentificare')
cursor = conn.cursor()

#pubs data




#create custom logo icon
logoIconPub = folium.features.CustomIcon('./static/img/logoPub.png',icon_size=(50,50))
logoIconPub2 = folium.features.CustomIcon('./static/img/logoPub.png',icon_size=(50,50))
logoIconPub3 = folium.features.CustomIcon('./static/img/logoPub.png',icon_size=(50,50))
logoIconPub4 = folium.features.CustomIcon('./static/img/logoPub.png',icon_size=(50,50))
logoIconPub5= folium.features.CustomIcon('./static/img/logoPub.png',icon_size=(50,50))
logoIconPub6 = folium.features.CustomIcon('./static/img/logoPub.png',icon_size=(50,50))

#create custom logo Restaurant

logoIconRestaurant1 = folium.features.CustomIcon('./static/img/RestaurantLogo.png',icon_size=(50,50))
logoIconRestaurant2 = folium.features.CustomIcon('./static/img/RestaurantLogo.png',icon_size=(50,50))
logoIconRestaurant3 = folium.features.CustomIcon('./static/img/RestaurantLogo.png',icon_size=(50,50))
logoIconRestaurant4 = folium.features.CustomIcon('./static/img/RestaurantLogo.png',icon_size=(50,50))
logoIconRestaurant5= folium.features.CustomIcon('./static/img/RestaurantLogo.png',icon_size=(50,50))
logoIconRestaurant6 = folium.features.CustomIcon('./static/img/RestaurantLogo.png',icon_size=(50,50))

#create custom logo Museum
logoIconMuseum1 = folium.features.CustomIcon('./static/img/MuseumLogo.png',icon_size=(50,50))
logoIconMuseum2 = folium.features.CustomIcon('./static/img/MuseumLogo.png',icon_size=(50,50))
logoIconMuseum3= folium.features.CustomIcon('./static/img/MuseumLogo.png',icon_size=(50,50))
logoIconMuseum4 = folium.features.CustomIcon('./static/img/MuseumLogo.png',icon_size=(50,50))
logoIconMuseum5= folium.features.CustomIcon('./static/img/MuseumLogo.png',icon_size=(50,50))
logoIconMuseum6= folium.features.CustomIcon('./static/img/MuseumLogo.png',icon_size=(50,50))

#create cutom logo Park
logoIconPark1 = folium.features.CustomIcon('./static/img/ParkLogo.png',icon_size=(50,50))
logoIconPark2 = folium.features.CustomIcon('./static/img/ParkLogo.png',icon_size=(50,50))
logoIconPark3= folium.features.CustomIcon('./static/img/ParkLogo.png',icon_size=(50,50))
logoIconPark4 = folium.features.CustomIcon('./static/img/ParkLogo.png',icon_size=(50,50))
logoIconPark5= folium.features.CustomIcon('./static/img/ParkLogo.png',icon_size=(50,50))
logoIconPark6= folium.features.CustomIcon('./static/img/ParkLogo.png',icon_size=(50,50))

#create monument logo
logoIconMonument1 = folium.features.CustomIcon('./static/img/Monument.png',icon_size=(50,50))
logoIconMonument2 = folium.features.CustomIcon('./static/img/Monument.png',icon_size=(50,50))
logoIconMonument3 = folium.features.CustomIcon('./static/img/Monument.png',icon_size=(50,50))
logoIconMonument4 = folium.features.CustomIcon('./static/img/Monument.png',icon_size=(50,50))






html = '<img src="data:image/png;base64,{}">'.format

m=folium.Map(location=[45.7711901, 21.2581345],zoom_start=12)


#popup Timisoara
pictureTm= base64.b64encode(open('./static/img/Tm.jpg','rb').read()).decode()
iframeTm=IFrame(html(pictureTm)+'<p>Timișoara</p>'+
                '<p> Description: Timișoara is the municipality of residence of Timiș County, Banat, Romania. </p>' +
                '<p> It is located in western Romania, close to the borders with Hungary and Serbia, on the banks of the river Bega. </p>' +
                '<p> Area: 130.5 km² </p>' +
                '<p> Metropolitan area: 244 ha </p>' +
                '<p> Weather: 15 ° C, wind from the S at 18 km / h, humidity of 56% </p>' +
                '<p> Population: 306,462 (2012) </p>' +
                '<p> Postal code: 300001-300990 </p>', width = 700, height = 720)
popupTm= folium.Popup(iframeTm,max_width=730)

folium.CircleMarker(
    location=[45.7560376, 21.2288460],
    radius=300,
    popup=popupTm ,
   color='#3186cc',
  fill=True,
   fill_color='#3186cc'
).add_to(m),



#Global tooltip
tooltip='Click For more info'
#pub tooltip
tooltip1="Like pub"
tooltip2="Beraria 700"
tooltip3="The irish pub"
tooltip4="The Note Pub"
tooltip5="La capite"
tooltip6="Scart Loc Lejer"
#Restaurant tooltip
tooltip7="Restaurant Dinar"
tooltip8="Restaurant Yugoslavia"
tooltip9="Restaurant Sabres"
tooltip10="Restaurant Merlot"
tooltip11="Sky Restaurant"+"<br>"+"Finish"
tooltip12="Pescada"
#Museums
tooltip13="Muzeul de Arta"+"<br>"+"Start"
tooltip14="Muzeul Banatului"
tooltip15="Muzeul Satului"
tooltip16="Muzeul Communist"
tooltip17="Muzeul de Transport Public „Corneliu Miklosi"
tooltip28="Typopassage museum"
#Parks
tooltip18="Zoo Garden"
tooltip19="Water Plant Park"
tooltip20="Roses Park"
tooltip21="Childrens Park"
tooltip22="Central Park"
tooltip23="Botanic Park"
#Monument
tooltip24="monumentul ostasului necunoscut din timisoara Timisoara"
tooltip25="Statuia Lupoaicei"
tooltip26="Momentul Ciumei"
tooltip27="Momentul Fercioara Maria"


#image popup
#picture1= base64.b64encode(open('./static/img/like pub.jpg','rb').read()).decode()
#iframe1=IFrame(html(picture1)+'<p>street address:Lascăr Catargiu Nr.2, Timișoara</p>'
#+'<p>Numeber phone:+40 770 157 710</p>'
#+'<a href= "https:https://www.facebook.com/likepub/">link</a>', width=445, height=445)
#popup1= folium.Popup(iframe1,max_width=450)



cursor = conn.cursor(dictionary=True)
cursor.execute("SELECT  * From  pubs WHERE Name='Like pub'" )
like_pub = cursor.fetchall()

cursor.execute("SELECT  * From  pubs WHERE Name='Beraria 700'" )
Beraria700 = cursor.fetchall()

cursor.execute("SELECT  * From  pubs WHERE Name='La Capite'" )
La_Capite = cursor.fetchall()

cursor.execute("SELECT  * From  pubs WHERE Name='Scart Loc Lejer'" )
Scart_Loc_Lejer = cursor.fetchall()

cursor.execute("SELECT  * From  pubs WHERE Name='The irish pub'" )
The_irish_pub = cursor.fetchall()

cursor.execute("SELECT  * From  pubs WHERE Name='The Note Pub'" )
The_Note_Pub = cursor.fetchall()

#restaurant
cursor.execute("SELECT  * From restaurant WHERE Name='Pescada'" )
Pescada = cursor.fetchall()

cursor.execute("SELECT  * From restaurant WHERE Name='Restaurant Merlot'" )
Restaurant_Merlot = cursor.fetchall()

cursor.execute("SELECT  * From restaurant WHERE Name='Restaurant Dinar'" )
Restaurant_Dinar = cursor.fetchall()

cursor.execute("SELECT  * From restaurant WHERE Name='Restaurant Yugoslavia'" )
Restaurant_Yugoslavia = cursor.fetchall()

cursor.execute("SELECT  * From restaurant WHERE Name='Restaurant Sabres'" )
Restaurant_Sabres = cursor.fetchall()

cursor.execute("SELECT  * From restaurant WHERE Name='Sky Restaurant'" )
Sky_Restaurant = cursor.fetchall()

cursor.execute("SELECT  * From museum WHERE Name='Muzeul Banatului'" )
Muzeul_Banatului = cursor.fetchall()

cursor.execute("SELECT  * From museum WHERE Name='Muzeul Communist'" )
Muzeul_Communist = cursor.fetchall()

cursor.execute("SELECT  * From museum WHERE Name='Muzeul de Arta'" )
Muzeul_de_Arta = cursor.fetchall()

cursor.execute("SELECT  * From museum WHERE Name='Muzeul Satului'" )
Muzeul_Satului = cursor.fetchall()

cursor.execute("SELECT  * From museum WHERE Name='Transport Museum'" )
Transport_Museum = cursor.fetchall()

cursor.execute("SELECT  * From museum WHERE Name='Tyropassage'" )
Tyropassage = cursor.fetchall()


cursor.execute("SELECT  * From parks WHERE Name='Roses Park'" )
Roses_Park = cursor.fetchall()

cursor.execute("SELECT  * From parks WHERE Name='Botanic Park'" )
Botanic_Park = cursor.fetchall()

cursor.execute("SELECT  * From parks WHERE Name='Childrens Park'" )
Childrens_Park = cursor.fetchall()

cursor.execute("SELECT  * From parks WHERE Name='Central Park'" )
Central_Park= cursor.fetchall()

cursor.execute("SELECT  * From parks WHERE Name='Water Plant Park'" )
Water_Plant_Park= cursor.fetchall()

cursor.execute("SELECT  * From parks WHERE Name='Zoo Garden'" )
Zoo_Garden= cursor.fetchall()



for  X in Roses_Park:
    #Name = X[]
 #   Adress=x[4]

    print(X['Name'])



#image popup
picture1= base64.b64encode(open(like_pub[0]['imagine'],'rb').read()).decode()
iframe1=IFrame(html(picture1)+"Name: "+like_pub[0]['Name']+"<br>"+"Adress: "+like_pub[0]['Adress']+"<br>"+"phone number: "+like_pub[0]['phone_number']+"<br>"+"category: "
               +like_pub[0]['category']+"<br>"+"website: "+'<a href='+like_pub[0]['link']+'>Link</a>',width=430, height=430)
popup1= folium.Popup(iframe1,max_width=450)





#Monumentul Ostașului Necunoscut imagine
picture2= base64.b64encode(open('./static/img/timisoara-monument-romanian-solider.jpg','rb').read()).decode()
iframe2=IFrame(html(picture2)+'<p> Over time, the plateau in front of the Unknown Soldier Monument in Central Park has become a hot spot on Army Day. Here, in addition to the traditional wreath-laying, '
                              'There are exercises in mastering the handling of weapons, along with artistic moments of the marching band in honor of the soldiers who fought and are fighting for their country. Romanian Army Day is celebrated between October 25-28 in Timisoara, '
                              'as a tribute to those who guarded the freedom of the country. </p>', width = 300, height = 300,)
popup2= folium.Popup(iframe2,max_width=300)
#Monumentul Statuia Lupoaicei
picture3= base64.b64encode(open('./static/img/Timisoara,_Lupa_Capitolina.jpg','rb').read()).decode()
iframe3=IFrame(html(picture3)+'<p> The statue of the She-Wolf in Timisoara is a statue depicting the legend of the founders of Rome, the brothers Romulus and Remus, breastfed by a she-wolf. '
                              'The statue depicts the legend of the founding of Rome, according to which the two brothers who founded the city were cared for by a wolf. </p>', width = 394, height = 394)
popup3= folium.Popup(iframe3,max_width=394)
#Momentul sfanta treime
picture4= base64.b64encode(open('./static/img/MomentulCiumei.jpg','rb').read()).decode()
iframe4=IFrame(html(picture4)+'<p>The Plague Column, also known as the Plague Statue or the Holy Trinity Monument, is erected in the middle of the Union Square in Timisoara, in accordance with the architectural style of the surrounding buildings. </p> ', width = 594, height = 594)
popup4= folium.Popup(iframe4,max_width=594)
#Monumentul Feciora Maria
picture5= base64.b64encode(open('./static/img/Fecioara_Maria.jpg','rb').read()).decode()
iframe5=IFrame(html(picture5)+'<p> The Sfânta Maria monument is located in Timișoara, in Sfânta Maria square and was erected in 1906 on the site of an older statue of Saint Maria. '
                              'Tradition says that Gheorghe Doja was executed here. </p>', width = 300, height = 300)
popup5= folium.Popup(iframe5,max_width=300)








#Beraria 700
picture6= base64.b64encode(open(Beraria700[0]['imagine'],'rb').read()).decode()
iframe6=IFrame(html(picture6)+"Name: "+Beraria700[0]['Name']+"<br>"+"Adress: "+Beraria700[0]['Adress']+"<br>"+"phone number: "+Beraria700[0]['phone_number']+"<br>"+"category: "
               +Beraria700[0]['category']+"<br>"+"website: "+'<a href='+Beraria700[0]['link']+'>Link</a>',width=430, height=430)
popup6= folium.Popup(iframe6,max_width=450)
#The irish pub
picture7= base64.b64encode(open(The_irish_pub[0]['imagine'],'rb').read()).decode()
iframe7=IFrame(html(picture7)+"Name: "+The_irish_pub[0]['Name']+"<br>"+"Adress: "+The_irish_pub[0]['Adress']+"<br>"+"phone number: "+The_irish_pub[0]['phone_number']+"<br>"+"category: "
               +The_irish_pub[0]['category']+"<br>"+"website: "+'<a href='+The_irish_pub[0]['link']+'>Link</a>',width=430, height=430)
popup7= folium.Popup(iframe7,max_width=450)

#The Note Pub
picture8= base64.b64encode(open(The_Note_Pub[0]['imagine'],'rb').read()).decode()
iframe8=IFrame(html(picture8)+"<br>"+"Name: "+The_Note_Pub[0]['Name']+"<br>"+"Adress: "+The_Note_Pub[0]['Adress']+"<br>"+"phone number: "+The_Note_Pub[0]['phone_number']+"<br>"+"category: "
               +The_Note_Pub[0]['category']+"<br>"+"website: "+'<a href='+The_Note_Pub[0]['link']+'>Link</a>',width=430, height=430)
popup8= folium.Popup(iframe8,max_width=450)

#La Capite
picture9= base64.b64encode(open(La_Capite[0]['imagine'],'rb').read()).decode()
iframe9=IFrame(html(picture9)+"Name: "+La_Capite[0]['Name']+"<br>"+"Adress: "+La_Capite[0]['Adress']+"<br>"+"phone number: "+La_Capite[0]['phone_number']+"<br>"+"category: "
               +La_Capite[0]['category']+"<br>"+"website: "+'<a href='+La_Capite[0]['link']+'>Link</a>',width=430, height=430)
popup9= folium.Popup(iframe9,max_width=450)
#Scart Loc Lejer
picture10= base64.b64encode(open(Scart_Loc_Lejer[0]['imagine'],'rb').read()).decode()
iframe10=IFrame(html(picture10)+"Name: "+Scart_Loc_Lejer[0]['Name']+"<br>"+"Adress: "+Scart_Loc_Lejer[0]['Adress']+"<br>"+"phone number: "+Scart_Loc_Lejer[0]['phone_number']+"<br>"+"category: "
               +Scart_Loc_Lejer[0]['category']+"<br>"+"website: "+'<a href='+Scart_Loc_Lejer[0]['link']+'>Link</a>',width=430, height=430)
popup10= folium.Popup(iframe10,max_width=450)
#Restaurant Dinar

picture11= base64.b64encode(open(Restaurant_Dinar[0]['imagine'],'rb').read()).decode()
iframe11=IFrame(html(picture11)+"Name: "+Restaurant_Dinar[0]['Name']+"<br>"+"Adress: "+Restaurant_Dinar[0]['Adress']+"<br>"+"phone number: "+Restaurant_Dinar[0]['phone_number']+"<br>"+"category: "
               +Restaurant_Dinar[0]['category']+"<br>"+"website: "+'<a href='+Restaurant_Dinar[0]['link']+'>Link</a>'+
                '<p> Description: The old atmosphere, full of tradition, from the Balkans, you can find it now in Timisoara, at Restaurant Dinar!'
                "We aim for guests who step on our doorstep to have an authentic, place-specific experience and to be left with a special memory!"
                'Restaurant Dinar Timisoara together with Etno Kuca Dinar from Vrsac bring for the first time in Romania the traditional Balkan recipes and dishes awarded by the Global Trade Leaders Club - International Hotel & Restaurant. </p>'
                             ,width=300 ,height=300)
popup11= folium.Popup(iframe11,max_width=300)

#Restaurant Yugoslavia

picture12= base64.b64encode(open(Restaurant_Yugoslavia[0]['imagine'],'rb').read()).decode()
iframe12=IFrame(html(picture12)+"Name: "+Restaurant_Yugoslavia[0]['Name']+"<br>"+"Adress: "+Restaurant_Yugoslavia[0]['Adress']+"<br>"+"phone number: "+Restaurant_Yugoslavia[0]['phone_number']+"<br>"+"category: "
               +Restaurant_Yugoslavia[0]['category']+"<br>"+"website: "+'<a href='+Restaurant_Yugoslavia[0]['link']+'>Link</a>'+
                '<p> Description: At the Yugoslavia restaurant in Timisoara, the culinary style of Serbian cuisine blends harmoniously with the unmistakable style of traditional Romanian cuisine, resulting in a variety of delicious dishes that can easily cope with the most demanding culinary tastes.'
                'The mastery and passion with which the master chefs cook at this restaurant is reflected in some real culinary masterpieces that you will surely be impressed and want to try again and the attention always directed to your requirements, make the Yugoslavia restaurant a reliable partner when you want to order food online. '
                'On the business card of this restaurant will always be written professionalism through which it is desired to offer a pleasant and unforgettable culinary experience. </p>'
                              ,width=300 ,height=300)
popup12= folium.Popup(iframe12,max_width=400)

#Restaurant Sabres
picture13= base64.b64encode(open(Restaurant_Sabres[0]['imagine'],'rb').read()).decode()
iframe13=IFrame(html(picture13)+"Name: "+Restaurant_Sabres[0]['Name']+"<br>"+"Adress: "+Restaurant_Sabres[0]['Adress']+"<br>"+"phone number: "+Restaurant_Sabres[0]['phone_number']+"<br>"+"category: "
               +Restaurant_Sabres[0]['category']+"<br>"+"website: "+'<a href='+Restaurant_Sabres[0]['link']+'>Link</a>'+
                            '<p> Description: Sabers Restaurant is a place of soul, only good to start the journey in the culinary realms. '
                            'Passion defines and motivates us, and the relaxing atmosphere is a place of honor. </p>'
                              ,width=300 ,height=300)
popup13= folium.Popup(iframe13,max_width=300)
#Sky Restaurant
picture14= base64.b64encode(open(Sky_Restaurant[0]['imagine'],'rb').read()).decode()
iframe14=IFrame(html(picture14)+"Name: "+Sky_Restaurant[0]['Name']+"<br>"+"Adress: "+Sky_Restaurant[0]['Adress']+"<br>"+"phone number: "+Sky_Restaurant[0]['phone_number']+"<br>"+"category: "
               +Sky_Restaurant[0]['category']+"<br>"+"website: "+'<a href='+Sky_Restaurant[0]['link']+'>Link</a>'+
                '<p> Description: Sky Restaurant stops the need to close your eyes when you want to escape from reality. I put your chair in the pleasant breezes, to stop your slipping and to climb close to the stars, just as fresh even in the middle of the day, in the plates full of taste. '
                'We dare to promise you the liberating feeling you give yourself every time you look at the sunset and make room for whims. We naturally make the sensations that, most of the time, you dont even expect. </P> '
                ,width=300 ,height=300)
popup14= folium.Popup(iframe14,max_width=300)
#Restaurant pescada
picture15= base64.b64encode(open(Pescada[0]['imagine'],'rb').read()).decode()
iframe15=IFrame(html(picture15)+"Name: "+Pescada[0]['Name']+"<br>"+"Adress: "+Pescada[0]['Adress']+"<br>"+"phone number: "+Pescada[0]['phone_number']+"<br>"+"category: "
               +Pescada[0]['category']+"<br>"+"website: "+'<a href='+Pescada[0]['link']+'>Link</a>'
                               '<p> Description: Pescada is a Mediterranean restaurant, whose menu includes a variety of fish delicacies, masterfully prepared by Chef Daian. </p>',width=300 ,height=300)
popup15= folium.Popup(iframe15,max_width=300)
#Restaurant Merlot
picture16= base64.b64encode(open(Restaurant_Merlot[0]['imagine'],'rb').read()).decode()
iframe16=IFrame(html(picture16)+"Name: "+Restaurant_Merlot[0]['Name']+"<br>"+"Adress: "+Restaurant_Merlot[0]['Adress']+"<br>"+"phone number: "+Restaurant_Merlot[0]['phone_number']+"<br>"+"category: "
               +Restaurant_Merlot[0]['category']+"<br>"+"website: "+'<a href='+Restaurant_Merlot[0]['link']+'>Link</a>'
                '<p> Description: Merlot Restaurant was born out of the desire to offer our guests a special experience and not just quality food.'
                'The menu is Mediterranean-inspired, featuring Italian and French cuisine.'
                '"All the ingredients were carefully chosen because we only wanted fresh and very good quality raw materials."'
                '"Pasta, sauces, syrups, sweets, all are made" at home "and without artificial ingredients."'
                'Merlot Restaurant was born out of the desire to offer our guests a special experience and not just quality food. </p>'
                ,width=300 ,height=300)
popup16= folium.Popup(iframe16,max_width=300)
#Muzeul de Arta
picture17= base64.b64encode(open(Muzeul_de_Arta[0]['imagine'],'rb').read()).decode()
iframe17=IFrame(html(picture17)+"Name: "+Muzeul_de_Arta[0]['Name']+"<br>"+"Adress: "+Muzeul_de_Arta[0]['Adress']+"<br>"+"phone number: "+Muzeul_de_Arta[0]['phone_number']+"<br>"+"category: "
               +Muzeul_de_Arta[0]['category']+"<br>"+"website: "+'<a href='+Muzeul_de_Arta[0]['link']+'>Link</a>'
                '<p> Description: The Art Museum of Timișoara is an art museum located in the Baroque Palace of Timișoara.'
                'The museum was created after the detachment of the art section of the Banat Museum, which operated for a period in a wing of the current building. </p>'
                              ,width=300 ,height=300)
popup17= folium.Popup(iframe17,max_width=300)
#Muzeul Banatului
picture18= base64.b64encode(open(Muzeul_Banatului[0]['imagine'],'rb').read()).decode()
iframe18=IFrame(html(picture18)+"Name: "+Muzeul_Banatului[0]['Name']+"<br>"+"Adress: "+Muzeul_Banatului[0]['Adress']+"<br>"+"phone number: "+Muzeul_Banatului[0]['phone_number']+"<br>"+"category: "
               +Muzeul_Banatului[0]['category']+"<br>"+"website: "+'<a href='+Muzeul_Banatului[0]['link']+'>Link</a>'
                            '<p> Description: The National Museum of Banat is a museum in Timisoara with its headquarters in Huniade Castle.'
                            'It was founded in 1872 as the "Society of History and Archeology." '
                            'It houses the most important collection of archaeological objects in Banat, </p>'
                            ,width=300 ,height=300)
popup18= folium.Popup(iframe18,max_width=300)
#Muzeul Satului
picture19= base64.b64encode(open(Muzeul_Satului[0]['imagine'],'rb').read()).decode()
iframe19=IFrame(html(picture19)+"Name: "+Muzeul_Satului[0]['Name']+"<br>"+"Adress: "+Muzeul_Satului[0]['Adress']+"<br>"+"phone number: "+Muzeul_Satului[0]['phone_number']+"<br>"+"category: "
               +Muzeul_Satului[0]['category']+"<br>"+"website: "+'<a href='+Muzeul_Satului[0]['link']+'>Link</a>'+
                                 '<p> Description: The Banat Village Museum in Timisoara is the only ethnographic museum in Romania that includes the civic center of the village,'
                                'consisting of the City Hall, the Church, the School, the National House and the birt, where most of the cultural-educational and scientific activities of a locality take place. </p>'
                                , width=300, height=300)

popup19= folium.Popup(iframe19,max_width=300)
#Muzeul Communist
picture20= base64.b64encode(open(Muzeul_Communist[0]['imagine'],'rb').read()).decode()
iframe20=IFrame(html(picture20)+"Name: "+Muzeul_Communist[0]['Name']+"<br>"+"Adress: "+Muzeul_Communist[0]['Adress']+"<br>"+"phone number: "+Muzeul_Communist[0]['phone_number']+"<br>"+"category: "
               +Muzeul_Communist[0]['category']+"<br>"+"website: "+'<a href='+Muzeul_Communist[0]['link']+'>Link</a>'
                             ,width=300 ,height=300)
popup20= folium.Popup(iframe20,max_width=300)
#Tyropassage museum
picture21= base64.b64encode(open(Tyropassage[0]['imagine'],'rb').read()).decode()
iframe21=IFrame(html(picture21)+"Name: "+Tyropassage[0]['Name']+"<br>"+"Adress: "+Tyropassage[0]['Adress']+"<br>"+"phone number: "+Tyropassage[0]['phone_number']+"<br>"+"category: "
               +Tyropassage[0]['category']+"<br>"+"website: "+'<a href='+Tyropassage[0]['link']+'>Link</a>',width=300 ,height=300)
popup21= folium.Popup(iframe21,max_width=300)
#Transport Museum
picture22= base64.b64encode(open(Transport_Museum[0]['imagine'],'rb').read()).decode()
iframe22=IFrame(html(picture22)+"Name: "+Transport_Museum[0]['Name']+"<br>"+"Adress: "+Transport_Museum[0]['Adress']+"<br>"+"phone number: "+Transport_Museum[0]['phone_number']+"<br>"+"category: "
               +Transport_Museum[0]['category']+"<br>"+"website: "+'<a href='+Transport_Museum[0]['link']+'>Link</a>',width=300 ,height=300)
popup22= folium.Popup(iframe22,max_width=300)

#Roses Park
picture23= base64.b64encode(open(Roses_Park[0]['imagine'],'rb').read()).decode()
iframe23=IFrame(html(picture23)+"Name: "+Roses_Park[0]['Name']+"<br>"+"website: "+'<a href='+Roses_Park[0]['link']+'>Link</a>'+"Describe: "+Roses_Park[0]['descriptions']

                              ,width=1500 ,height=709)
popup23= folium.Popup(iframe23,max_width=1600)
#Botanic Park
picture24= base64.b64encode(open(Botanic_Park[0]['imagine'],'rb').read()).decode()
iframe24=IFrame(html(picture24)+"<br>"+"Name: "+Botanic_Park[0]['Name']+"<br>"+"website: "+'<a href='+Botanic_Park[0]['link']+'>Link</a>'
                                +'<p>Describe:Situated near the city center, the Botanic Park allows you to'
                                'rest from urban part of Timisoara, breathe the clean air and talk a relaxing stroll among the woods.</p>' ,width=400,height=462 )
popup24= folium.Popup(iframe24,max_width=500)
#Childrens Park
picture25= base64.b64encode(open(Childrens_Park[0]['imagine'],'rb').read()).decode()
iframe25=IFrame(html(picture25)+"<br>"+"Name: "+Childrens_Park[0]['Name']+"<br>"+"website: "+'<a href='+Childrens_Park[0]['link']+'>Link</a>'+
                                '<p>Describe:This is a big free playground, There are plenty of attractions for the kids+adults'
                                '(beautiful, modern slides, swings, boats, obstacles, small wooden huts, fountain and many more).'
                                'There are many trees so you can hide in the shade if it s a hot day and its placed next to Roses Park.</p>' ,width=300,height=362 )
popup25= folium.Popup(iframe25,max_width=500)
#Central Park
picture26= base64.b64encode(open(Central_Park[0]['imagine'],'rb').read()).decode()
iframe26=IFrame(html(picture26)+"<br>"+"Name: "+Central_Park[0]['Name']+"<br>"+"website: "+'<a href='+Central_Park[0]['link']+'>Link</a>'
                    +'<p>Describe:Central Park is one of the oldest parks in Timisoara,'
                    'dating from 1880, it haves a lot of monuments of a lot of important personalities.'
'                      The bigest one is the Romanian Soldier monument.</p>' ,width=799,height=459 )
popup26= folium.Popup(iframe26,max_width=800)
#Water Plant Park
picture27= base64.b64encode(open(Water_Plant_Park[0]['imagine'],'rb').read()).decode()
iframe27=IFrame(html(picture27)+"<br>"+"Name: "+Water_Plant_Park[0]['Name']+"<br>"+"website: "+'<a href='+Water_Plant_Park[0]['link']+'>Link</a>'
                +'<p>Describe:Water Plants Park is placed right next to Timisoaras Water Plant, a beautifull old building,'
'the park is very big, on both sides of the Bega river, with little playgrounds, banches, lots of trees and tables.</p>' ,width=300,height=400)
popup27= folium.Popup(iframe27,max_width=400)
#Zoo Garden
picture28= base64.b64encode(open(Zoo_Garden[0]['imagine'],'rb').read()).decode()
iframe28=IFrame(html(picture28)+Zoo_Garden[0]['Name']+"<br>"+"website: "+'<a href='+Zoo_Garden[0]['link']+'>Link</a>'
                                +'<p>Describe:Placed in the Green Forest in Timsioara the Zoo is widely spread with a lot of diverse species of animals.'
                                'Cared pathways , places to stop and rest, some stops where you can even see closely the animals.</p>' ,width=300,height=400)
popup28= folium.Popup(iframe28,max_width=400)

#Create markers Pub
folium.Marker([like_pub[0]['latitude'],like_pub[0]['longitude']],
              popup=popup1,
              tooltip=tooltip1,
              icon = logoIconPub).add_to(m),
folium.Marker([Beraria700[0]['latitude'],Beraria700[0]['longitude']],
              popup=popup6,
              tooltip=tooltip2,
              icon = logoIconPub2).add_to(m),
folium.Marker([The_irish_pub[0]['latitude'],The_irish_pub[0]['longitude']],
              popup=popup7,
              tooltip=tooltip3,
              icon = logoIconPub3).add_to(m),
folium.Marker([The_Note_Pub[0]['latitude'],The_Note_Pub[0]['longitude']],
              popup=popup8,
              tooltip=tooltip4,
              icon = logoIconPub4).add_to(m),
folium.Marker([La_Capite[0]['latitude'],La_Capite[0]['longitude']],
              popup=popup9,
              tooltip=tooltip5,
              icon = logoIconPub5).add_to(m),
folium.Marker([Scart_Loc_Lejer[0]['latitude'],Scart_Loc_Lejer[0]['longitude']],
              popup=popup10,
              tooltip=tooltip6,
              icon = logoIconPub6).add_to(m),

#Marker Restaurant

folium.Marker([Restaurant_Dinar[0]['latitude'],Restaurant_Dinar[0]['longitude']],
              popup=popup11,
              tooltip=tooltip7,
              icon=logoIconRestaurant1).add_to(m),

folium.Marker([Restaurant_Yugoslavia[0]['latitude'],Restaurant_Yugoslavia[0]['longitude']],
              popup=popup12,
              tooltip=tooltip8,
              icon=logoIconRestaurant2).add_to(m),

folium.Marker([Restaurant_Sabres[0]['latitude'],Restaurant_Sabres[0]['longitude']],
              popup=popup13,
              tooltip=tooltip9,
              icon=logoIconRestaurant3).add_to(m),

folium.Marker([Restaurant_Merlot[0]['latitude'],Restaurant_Merlot[0]['longitude']],
              popup=popup16,
              tooltip=tooltip10,
              icon=logoIconRestaurant4).add_to(m),

folium.Marker([Sky_Restaurant[0]['latitude'],Sky_Restaurant[0]['longitude']],
              popup=popup14 ,
              tooltip=tooltip11,
              icon=logoIconRestaurant5).add_to(m),
folium.Marker([Pescada[0]['latitude'],Pescada[0]['longitude']],
              popup=popup15,
              tooltip=tooltip12,
              icon=logoIconRestaurant6).add_to(m),


#marker Museums
folium.Marker([Muzeul_de_Arta[0]['latitude'],Muzeul_de_Arta[0]['longitude']],
              popup=popup17,
              tooltip=tooltip13,
              icon=logoIconMuseum1).add_to(m),
folium.Marker([Muzeul_Banatului[0]['latitude'],Muzeul_Banatului[0]['longitude']],
              popup=popup18,
              tooltip=tooltip14,
              icon=logoIconMuseum2).add_to(m),
folium.Marker([Muzeul_Satului[0]['latitude'],Muzeul_Satului[0]['longitude']],
              popup=popup19,
              tooltip=tooltip15,
              icon=logoIconMuseum3).add_to(m),
folium.Marker([Muzeul_Communist[0]['latitude'],Muzeul_Communist[0]['longitude']],
              popup=popup20,
              tooltip=tooltip16,
              icon=logoIconMuseum4).add_to(m),
folium.Marker([Tyropassage[0]['latitude'],Tyropassage[0]['longitude']],
              popup=popup21,
              tooltip=tooltip28,
              icon=logoIconMuseum6).add_to(m),
folium.Marker([Transport_Museum[0]['latitude'],Transport_Museum[0]['longitude']],
              popup=popup22,
              tooltip=tooltip17,
              icon=logoIconMuseum5).add_to(m),
#marker park
folium.Marker([Zoo_Garden[0]['latitude'],Zoo_Garden[0]['longitude']],
              popup=popup28,
              tooltip=tooltip18,
              icon=logoIconPark1).add_to(m),
folium.Marker([Water_Plant_Park[0]['latitude'],Water_Plant_Park[0]['longitude']],
              popup=popup27,
              tooltip=tooltip19,
              icon=logoIconPark2).add_to(m),
folium.Marker([Roses_Park[0]['latitude'],Roses_Park[0]['longitude']],
              popup=popup23,
              tooltip=tooltip20,
              icon=logoIconPark3).add_to(m),
folium.Marker([Childrens_Park[0]['latitude'],Childrens_Park[0]['longitude']],
              popup=popup25,
              tooltip=tooltip21,
              icon=logoIconPark4).add_to(m),
folium.Marker([Central_Park[0]['latitude'],Central_Park[0]['longitude']],
              popup=popup26,
              tooltip=tooltip22,
              icon=logoIconPark5).add_to(m),
folium.Marker([Botanic_Park[0]['latitude'],Botanic_Park[0]['longitude']],
              popup=popup24,
              tooltip=tooltip23,
              icon=logoIconPark6).add_to(m),

#Monuments
folium.Marker([45.75114316856265, 21.22112107359635],
              popup=popup2,
              tooltip=tooltip24,
              icon=logoIconMonument1).add_to(m),
folium.Marker([45.752585415704985, 21.225324374674834],
              popup=popup3,
              tooltip=tooltip25,
              icon=logoIconMonument2).add_to(m),
folium.Marker([45.757960252002604, 21.22908268767883],
              popup=popup4,
              tooltip=tooltip26,
              icon=logoIconMonument3).add_to(m),
folium.Marker([45.74915521908834, 21.218918125125253],
              popup=popup5,
              tooltip=tooltip27,
              icon=logoIconMonument4).add_to(m),





#route_location=Muzeul de arta , Momentul ciumei, Botanic park, Muzeul Banatului, Statuia lupoaicei, The note pub,Tyrro passage,
#Momentul ostasului,Sky restaurant

folium.PolyLine(locations=[(45.7573543,21.2292917),
                           (45.757960252002604, 21.22908268767883),
(45.760199099999994,21.22484718178763),
(45.7530646,21.2270757),
(45.752585415704985, 21.225324374674834),
(45.7514933,21.2261728),
(45.749713423026634, 21.22523713493029),
(45.75114316856265, 21.22112107359635),
(45.7568019,21.2217609)],line_opacity = 0.5).add_to(m)



import geopy.distance

# text widgets
route_start_widget = ipywidgets.Text(value='', placeholder='address', description='start:')
route_stop_widget = ipywidgets.Text(value='', placeholder='address', description='stop:')


# widget function
def get_distance(start_address, stop_address):
    # string addresses to location information
    start_location = geocoder.osm(start_address)
    stop_location = geocoder.osm(stop_address)

    # pull out latitude and longitude from location information
    start_latlng = [start_location.lat, start_location.lng]
    stop_latlng = [stop_location.lat, stop_location.lng]

    # calculate distance from start point to stop point using latitudes and longitudes
    distance = geopy.distance.distance(start_latlng, stop_latlng).miles
    print(f'distance: {distance:.2f} miles')

    # map
    distance_path = [(start_latlng), (stop_latlng)]
    map_distance = folium.Map(location=[38, -98], zoom_start=4)
    plugins.AntPath(distance_path).add_to(map_distance)
    display(map_distance)


# interaction between widgets and function
ipywidgets.interact_manual(get_distance, start_address=route_start_widget, stop_address=route_stop_widget)

# notice animation moves in the direction from start to stop and distance prints above map