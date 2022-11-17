def CSDF(path):
    #Design and develop a tool for digital forensic of images
    #GEOLOCATION IMAGE MAPPING FORENSICS

    # print(url_for(path))
    from PIL import Image,ImageFile
    # ImageFile.LOAD_TRUNCATED_IMAGES = True
    # print(type(path))
    # img=Image.open(path)
    # img.show()

    from PIL.ExifTags import TAGS
    from GPSPhoto import gpsphoto
    # import gradio as gr
    # Get the data from image file and return a dictionary
    #from PIL import ImageFile
    #ImageFile.LOAD_TRUNCATED_IMAGES = True
    #im = Image.open(r'C:/Users/91932/Pictures/IMG_7449.JPG')
    #im.show()





    # data = gpsphoto.getGPSData('C:/Users/91932/Pictures/IMG_7449.JPG')
    tagArr=[]
    data = gpsphoto.getGPSData(path)
    print("Latitude                 :",        data['Latitude'])
    print("Longitude                :",        data['Longitude'])
    print("Altitude                 :",        data['Altitude'])
    tagArr.append("Latitude                 :"+str(data['Latitude']))
    tagArr.append("Longitude                :"+str(data['Longitude']))
    tagArr.append("Altitude                 :"+str(data['Altitude']))


    # Path to the image or video
    # imagename = "C:/Users/91932/Pictures/IMG_7449.JPG"


    # Read the image data using PIL
    image = Image.open(path)

    # Extract EXIF data
    exifdata = image.getexif()

    dataArr=[]
    # iterating over all EXIF data fields
    for tag_id in exifdata:
        # get the tag name, instead of human unreadable tag id
        tag = TAGS.get(tag_id, tag_id)
        data = exifdata.get(tag_id)
        # decode bytes 
        if isinstance(data, bytes):
            data = data.decode()
        temp=tag+":"+str(data)
        tagArr.append(temp)
    return tagArr

