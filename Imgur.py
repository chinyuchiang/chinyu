import matplotlib
matplotlib.use('Agg')
import datetime
from imgurpython import ImgurClient
client_id = '9dcefb81aaea882'
client_secret = 'dc8fa81499a7aec4e6793823418b29ee701a2d64'
album_id = 'z9VzL6i'
access_token = '0880425200f185f37b484d6118361e6ada611aee'
refresh_token = '6527c48554821cb19c41a734fd57add9a4e22e61'


#https://imgur.com/#access_token=0880425200f185f37b484d6118361e6ada611aee&expires_in=315360000&token_type=bearer&refresh_token=6527c48554821cb19c41a734fd57add9a4e22e61&account_username=chinyuchiang&account_id=183376033


def showImgur(fileName):
    client = ImgurClient(client_id,client_secret,access_token,refresh_token)
    #params
    config = {
        'album':album_id,
        'name':fileName,
        'title':fileName,
        'description': str(datetime.date.today())
        }
    
    #upload file
    try:
        print("[log:INFO]uploading Image...")
        Imgur1 = client.upload_from_path(fileName+'.png', config=config, anon=False)['11nk']
        #strimg to dict
        print ("[log: INFO]Done upload. ")
    except :
        #if faild to upload 
        imgurl = 'https://i.imgur.com/RFmkvQX.jpg'
        print("[log:ERROR]Unable upload !")

    return imgurl

