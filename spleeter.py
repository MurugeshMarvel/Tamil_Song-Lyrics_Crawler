import os
import sys
import tqdm
import traceback

p = os.getcwd()
i_song = os.path.join(p, 'Sample/Songs')
output = os.path.join(p, 'Sample\output')
ch_dir = os.chdir('Sample/Songs')

"""_summary_
    Apply sleeter to remove the karaoke and get only vocal as wav
"""

# for file in os.listdir(i_song):
#     if file.endswith(".wav"):
        # file1 = file.split(' ')[0]
        # file_rename = f'mv {i_song}/{file} {i_song}/{file1}.mp3'
        # os.system(file_rename)
        # files = f"{i_song}/{file1}"
        # spleeter separate -o /Users/murugesan.vadivel/DEV/MyRepo/In_Isai_Paadal-Extractor/output Aasai-Aasaiyai.mp3
        # cmd = f'spleeter separate -o {output} {file}'
        # fol = file.split('.')[0]
        # vocal = f"{output}/{fol}"
        # rename_cmd = f'mv {vocal}/vocals.wav {vocal}/{fol}.wav'
        # os.system(rename_cmd)
        # mv = f'mv {vocal}/{fol}.wav {output}'
        # os.system(mv)
        # rm_cmd = f'rm -rf {vocal}'
        # os.system(rm_cmd)


def _spleeter_convert():
    for file in tqdm.tqdm(os.listdir(i_song)):
        try:
            if file.endswith('wav'):
                print(file)
                folder = file.split(".")[0]
                folder_path = f"{output}\{folder}"
                isExist = os.path.exists(folder_path)
                if not isExist:
                    cmd = f'spleeter separate -o {output} {file}'
                    os.system(cmd)
                    print(f"Spleeter executed for {file}")
        except Exception as exp:
            print(f"EXP - {exp}, \n {traceback.format_exc()}")
    return "spleeter excution completed for all songs"


if __name__ == '__main__':
    _spleeter_convert()