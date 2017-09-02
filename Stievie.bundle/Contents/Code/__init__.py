import requests
from lxml import html
channels = SharedCodeService.channels

####################################################################################################
PREFIX = "/video/stievie"
NAME = "Stievie"
ICON = "stievie.png"
####################################################################################################

def Start():
    Dict.Reset()
    ObjectContainer.title1 = NAME

@handler(PREFIX, NAME, thumb=ICON, art=ICON)
def MainMenu():

    if not Dict['loggedIn']:
        Authenticate()

    oc = ObjectContainer()
    for channel in channels.channelList:
        if Prefs['premium'] or not channel.premium:
            do_channel = VideoClipObject(
                url= StreamURL(channel.url_name),
                title = channel.name,
                thumb = channel.logo_name
            )
            oc.add(do_channel)

    return oc

def StreamURL(channel):

    authorization_header = {
        'Authorization' : "access_token=" + Dict['accessToken']
    }

    stream_url = 'http://stream-live.medialaan.io/stream-live/v1/channels/' + channel + '/episodes/current/video/?deviceId=' + Prefs['deviceId']
    stream_url_resp = requests.get(stream_url, headers=authorization_header)
    return  stream_url_resp.json()['response']['url']['hls']

def Authenticate():

    if Prefs['username'] and Prefs['password']:
        try:
            login_data = {
                'loginID' : Prefs['username'],
                'password' : Prefs['password'],
                'APIKey' : '3_OEz9nzakKMkhPdUnz41EqSRfhJg5z9JXvS4wUORkqNf2M2c1wS81ilBgCewkot97'
            }
            login_resp = requests.post('https://accounts.eu1.gigya.com/accounts.login', login_data)
            uid=login_resp.json()['UID']
            uidSignature=login_resp.json()['UIDSignature']
            signatureTimestamp=login_resp.json()['signatureTimestamp']

            search_page_resp = requests.get('http://watch.stievie.be')
            search_page_resp_xml = html.fromstring(search_page_resp.content)
            script_tag = search_page_resp_xml.xpath("//body//script")[0].text
            config_js_url = "http://static.watch.stievie.be/config-" + script_tag.split('config-')[1].split('"')[0]
            config_js_resp = requests.get(config_js_url)
            apiKey = config_js_resp.content.split('medialaan:{apiKey:"')[1].split('"')[0]

            token_data = {
                'database': 'stievie-sso',
                'uid': uid,
                'signature': uidSignature,
                'timestamp': signatureTimestamp
            }
            token_header = {
                'Authorization' : "apikey=" + apiKey
            }
            token_resp = requests.get('http://user.medialaan.io/user/v1/gigya/request_token', headers=token_header, params = token_data)

            Dict['loggedIn']=True
            Dict['accessToken']=token_resp.json()['response']

        except:
            Dict['loggedIn']=False
            Log.Exception("Login Failed")

    return True
