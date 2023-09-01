# from pydub import AudioSegment
# from pydub.silence import split_on_silence
# import os
#
# # 初始化
# audiopath = "C:\\Users\\Administrator\\Desktop\\dd.mp3"
# audiotype = 'mp3' #如果wav、mp4其他格式参看pydub.AudioSegment的API
# # 读入音频
# print('读入音频')
# sound = AudioSegment.from_file(audiopath, format=audiotype)
# sound = sound[:3*60*1000] #如果文件较大，先取前3分钟测试，根据测试结果，调整参数
# # 分割
# print('开始分割')
# chunks = split_on_silence(sound,min_silence_len=300,silence_thresh=-70)#min_silence_len: 拆分语句时，静默满0.3秒则拆分。silence_thresh：小于-70dBFS以下的为静默。
# # 创建保存目录
# filepath = os.path.split(audiopath)[0]
# chunks_path = filepath+'/chunks/'
# if not os.path.exists(chunks_path):os.mkdir(chunks_path)
# # 保存所有分段
# print('开始保存')
# for i in range(len(chunks)):
#     new = chunks[i]
#     save_name = chunks_path+'%04d.%s'%(i,audiotype)
#     new.export(save_name, format=audiotype)
#     print('%04d'%i,len(new))
# print('保存完毕')



from pydub import AudioSegment
from pydub.silence import split_on_silence
import os

init_id = 0
root = r'C:\Users\Administrator\Desktop\wav05'
file_lst = []
audiopath_lst = []


## 加载数据
def search_audio(file_dir):
    """
    递归查找音频文件
    :param file_dir:
    :return:
    """
    items = os.listdir(file_dir)
    items = [os.path.join(file_dir, item) for item in items]
    for item in items:
        if os.path.isdir(item):
            search_audio(item)
        else:
            file_lst.append(item)


search_audio(root)

for file in file_lst:
    if len(file.split('.')) == 2:
        audiopath_lst.append(file)


def read_wave(path):
    format_type = path.split(".")[-1]
    if format_type in ["wav", "WAV"]:
        wav_audio = AudioSegment.from_file(path, format="wav")
    elif format_type == "mp3":
        wav_audio = AudioSegment.from_file(path, format="mp3")
    elif format_type == "m4a":
        wav_audio = AudioSegment.from_file(path, format="mp4")

    return wav_audio, format_type


for i, audiopath in enumerate(audiopath_lst):
    audiopath = os.path.join(root, audiopath)
    print(audiopath)

    ## 读入音频

    sound, audiotype = read_wave(audiopath)

    ## 切割
    print('开始切割')
    chunks = split_on_silence(sound, min_silence_len=600, silence_thresh=-40)
    filepath = os.path.split(audiopath)[0]
    chunks_path = filepath + '\\chunks\\'
    if not os.path.exists(chunks_path):
        os.mkdir(chunks_path)

    print('开始保存音频片段')
    for j in range(len(chunks)):
        new = chunks[j]
        save_name = chunks_path + '{}_{}.{}'.format(i + init_id, j, audiotype)
        new.export(save_name, format=audiotype)
        print('{}\t{}\t{}'.format(i + init_id, j, len(new)))

    print('保存完毕')
