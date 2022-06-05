import os
import sys

p = os.getcwd()
i_song = os.path.join(p, 'Songs/Songs')
output = os.path.join(p, 'Songs/output')
ch_dir = os.chdir('Songs/Songs')
# for file in os.listdir(ch_dir):
#     if file.endswith(".mp3"):
#         file1 = file.split(' ')[0]
#         file_re = f'{file1}.mp3'
#         os.rename(file, file_re)
        
for f_song in os.listdir(i_song):
    if f_song.endswith(".mp3"):
        files = f"{i_song}/{f_song}"
        cmd = f'spleeter separate -o {output} {files}'
        os.system(cmd)
        
for fv_song in os.listdir(i_song):
    if fv_song.endswith('mp3'):
        s_name = fv_song.split('.mp3')[0]
        vocal = f"{output}/{s_name}"
        rename_cmd = f'mv {vocal}/vocals.wav {vocal}/{s_name}.mp3'
        os.system(rename_cmd)
        mv = f'mv {vocal}/{s_name}.mp3 {output}'
        os.system(mv)
        rm_cmd = f'rm -rf {vocal}'
        os.system(rm_cmd)


# for file in os.listdir(i_song):
#     if file.endswith(".mp3"):
        
#         file1 = file.split(' ')[0]
#         file_rename = f'mv {i_song}/{file} {i_song}/{file1}.mp3'
#         os.system(file_rename)
#         files = f"{i_song}/{file1}"
#         # spleeter separate -o /Users/murugesan.vadivel/DEV/MyRepo/In_Isai_Paadal-Extractor/output Aasai-Aasaiyai.mp3
#         cmd = f'spleeter separate -o {output} {files}'
#         os.system(cmd)
#         fol = file.split('.')[0]
#         vocal = f"{output}/{fol}"
#         rename_cmd = f'mv {vocal}/vocals.wav {vocal}/{fol}.mp3'
#         os.system(rename_cmd)
#         mv = f'mv {vocal}/{fol}.mp3 {output}'
#         os.system(mv)
#         rm_cmd = f'rm -rf {vocal}'
#         os.system(rm_cmd)
