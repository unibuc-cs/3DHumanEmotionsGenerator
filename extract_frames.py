import os
import subprocess


RES_DIR = 'dataset/'
FRAMES_DIR = os.path.join(RES_DIR, 'frames/RadaPaul/scared2')

os.makedirs(FRAMES_DIR, exist_ok=True)

ffmpeg_command = [
    'ffmpeg', '-i', 'dataset/Rada Paul/Data (videos)/scared/scared2.mp4', '-vf', f'fps={2}', '-qscale:v', '2', os.path.join(FRAMES_DIR,'frame%d.png')
]
subprocess.run(ffmpeg_command)

