import matplotlib
matplotlib.use('Agg')
import datetime
from imgurpython import ImgurClient
# client_id = 'Your imgur client id'
# client_secret = 'Your imgur client secret'
# album_id = 'Your imgur album id'
# access_token = 'Your imgur access token'
# refresh_token = 'Your imgur refresh token'

client_id = '41cb541b1307080'
client_secret = 'eb53e6f10a82264a2f0f752fb0350807b9b6dfe6'
album_id = 'Wd3o8mZ'
access_token = 'b4d1885e65dc6c1550ae9fbe89c6243e86305577'
refresh_token = 'b9fcf89f5fe7e6230c17844d714b1a7836611c3'

def showImgur(fileName):
    client = ImgurClient(client_id, client_secret, access_token, refresh_token)

    config = {

        'album': album_id,
        'name': fileName,
        'title': fileName,
        'description': str(datetime.date.today())
    }

    try:
        print("[log:INFO]uploading image... ")
        imgurl = client.upload_from_path(fileName + '.png', config = config, anon = False)['link']
        print("[log:INFO]Done upload.")
    except:
        imgurl = 'https://imgur.com/zB3Mkrs'
        print("[log:ERROR]Unable upload ! ")

    return imgurl