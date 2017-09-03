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

    oc = ObjectContainer()
    for channel in channels.channelList:
        if Prefs['premium'] or not channel.premium:
            do_channel = VideoClipObject(
                url= 'https://stream-live.medialaan.io/stream-live/v1/channels/' + channel.url_name + '/episodes/current/video/?deviceId=' + Prefs['deviceId'],
                title = channel.name,
                thumb = channel.logo_name
            )
            oc.add(do_channel)

    return oc
