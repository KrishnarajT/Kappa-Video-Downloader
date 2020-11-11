import pytube as pt
tags = {
    313: '2160p',
    271: '1440p',
    137: '1080p',
    22: '720p',
    18: '360p',
    278: '144p',
    140: 'MP4 128kb/s (only audio)',
    249: 'webm 50Kb/s (only audio)',
    251: 'webm 160kb/s (onlu audio)',
}


def get_available_qualities(url):
    video = pt.YouTube(url)
    qualities = []
    for i in tags.keys():
        if video.streams.get_by_itag(i):
            qualities.append(tags.get(i))
    return qualities


def get_available_qualities_with_obj(youtube_obj):
    qualities = []
    for i in tags.keys():
        if youtube_obj.streams.get_by_itag(i):
            qualities.append(tags.get(i))
    return qualities


#print( list( tags.keys() )[ list( tags.values() ).index( '720p' ) ] )
