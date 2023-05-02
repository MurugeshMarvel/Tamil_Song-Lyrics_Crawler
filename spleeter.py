import os
import sys
import tqdm
import traceback

p = os.getcwd()
i_song = os.path.join(p, 'Sample/Songs')
output = os.path.join(p, 'Sample/output')
ch_dir = os.chdir('Sample/Songs')

"""_summary_
    Apply sleeter to remove the karaoke and get only vocal as wav
"""

def _spleeter_convert():
    for file in tqdm.tqdm(os.listdir(i_song)):
        try:
            if file.endswith('wav'):
                print(f"Spleeter running for {file}")
                folder = file.split(".")[0]
                folder_path = f"{output}/{folder}"
                print("folder path is:- ", folder_path)
                isExist = os.path.exists(folder_path)
                print(isExist)
                if not isExist:
                    cmd = f'spleeter separate -o {output} {file}'
                    os.system(cmd)
                    print(f"Spleeter executed for {file}")
                else:
                    vocal = f"{output}/{folder}"
                    rename_cmd = f'mv {vocal}/vocals.wav {vocal}/{folder}.wav'
                    os.system(rename_cmd)
                    mv = f'mv {vocal}/{folder}.wav {output}'
                    os.system(mv)
                    rm_cmd = f'rm -rf {vocal}'
                    os.system(rm_cmd)

        except Exception as exp:
            print(f"EXP - {exp}, \n {traceback.format_exc()}")
    return "spleeter excution completed for all songs"


if __name__ == '__main__':
    _spleeter_convert()
