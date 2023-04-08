import sys
import os
import shutil as sh
import random

new_dir         = 'new'
videos_dir      = 'videos'
audios_dir      = 'audios'
templates_dir   = 'templates'
logos_dir       = 'logos'

def get_audio(filename):
    try:
        audios = os.listdir(audios_dir)
        return os.path.join(audios_dir,audios[audios.index(filename.replace('mp4','mp3'))])
    except:
        return False

videos = os.listdir(videos_dir)
if not len(videos):
    sys.exit('No Videos')

for short in os.listdir(templates_dir):
    if not short.startswith('Copied_'):
        continue
    os.rename(
        os.path.join(templates_dir,short),
        os.path.join(templates_dir,short.replace('Copied_',''))
    )

# if len(os.listdir(new_dir)):
#     sh.rmtree(new_dir)
#     os.mkdir(new_dir)

logos = os.listdir(logos_dir)
for filename in videos:
    folder = filename.rsplit('.',1)[0]
    video = os.path.join(videos_dir,filename)
    audio = get_audio(filename)
    for short in os.listdir(templates_dir):
        new_short = os.path.join(new_dir,folder,short)
        if os.path.isdir(new_short):
            continue
        sh.copytree(os.path.join(templates_dir,short),new_short)
        sh.copy(os.path.join(logos_dir,logos[random.randint(0,len(logos)-1)]),os.path.join(new_short,'logo.png'))
        sh.copy(video,os.path.join(new_short,'video.mp4'))
        if audio:
            sh.copy(audio,os.path.join(new_short,'audio.mp3'))
    print(folder)
