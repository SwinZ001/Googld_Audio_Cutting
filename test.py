# from pytube import YouTube
# # 爬取字幕
# link = 'https://www.youtube.com/watch?v=JKwHZnk1ZNs'
# src = YouTube(link)
#
# # prints all available captions in various languages.
# print('Captions Available: ', src.captions)
# print()
#
# # Getting only English captions by specifying 'en' as parameter
# en_caption = src.captions.get_by_language_code('en')
# print(en_caption.xml_captions)
#
# # Instead of Captions in XML format we are converting it to string format.
# en_caption_convert_to_srt = (en_caption.generate_srt_captions())
# print(en_caption_convert_to_srt)


# # 下载视频
# yt = YouTube("https://www.youtube.com/watch?v=vib5s3eDr7o", use_oauth=True, allow_oauth_cache=True)
#
# # 显示下载的视频文件的文件名(视频标题)
# print(yt.title)
#
# storePath = "E:\youtube小视频"  #视频保存路径
# # #选择下载分辨率最高的视频，storePath
# yt.streams.filter().get_highest_resolution().download(storePath,filename='')
# # # 选择下载指定分辨率的视频
# # yt.streams.filter().get_by_resolution('720p').download(storePath,filename='')


from pytube import YouTube

link = 'https://www.youtube.com/watch?v=iTgqmhhFyyI'
src = YouTube(link, use_oauth=True, allow_oauth_cache=True)

# prints all available captions in various languages.
print('Captions Available: ', src.captions)
print()

# Getting only English captions by specifying 'en' as parameter
en_caption = src.captions.get_by_language_code('zh-Hant')
print(en_caption.xml_captions)

# Instead of Captions in XML format we are converting it to string format.
en_caption_convert_to_srt = (en_caption.generate_srt_captions())
print(en_caption_convert_to_srt)












