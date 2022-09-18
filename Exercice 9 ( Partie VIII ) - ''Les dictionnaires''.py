from PIL import Image
def get_exif(filename):
    return(Image.open(filename)._getexif())

code_image=get_exif("help.jpg")
gps1=code_image[34853]

def gps_for_maps(gps):
    latitude=str(code_image[34853][2][0][0])+"°"+str(code_image[34853][2][1][0])+"'"+str(code_image[34853][2][2][0]/1000000)+'"'+str(code_image[34853][1])
    longitude=str(code_image[34853][4][0][0])+"°"+str(code_image[34853][4][1][0])+"'"+str(code_image[34853][4][2][0]/1000000)+'"'+str(code_image[34853][3])
    coordonnees=latitude+" "+longitude
    return(coordonnees)




coord=gps_for_maps(gps1)


print("La personne à secourir se trouve en ",coord)

print(code_image[34853])