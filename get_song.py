import os
from youtubesearchpython import VideosSearch


class GetSongs(object):
    def __init__(self,
                 save_dir: str):
        self.save_dir = save_dir
        self.vid_base_link = 'https://www.youtube.com/watch?v='

    @staticmethod
    def _get_vid_id(song_name: str,
                    limit: int,
                    get_all_ids: bool = False
                    ):

        vidsearch = VideosSearch(song_name, limit=limit)
        vid_ids_res = vidsearch.result()['result']
        ids_inds = [i for i in range(len(vid_ids_res))] if get_all_ids else [0]

        vid_ids = [vid_ids_res[i]['id'] for i in ids_inds]
        return vid_ids

    def _construct_cli_cmnd(self,
                            vid_link: str,
                            out_format: str = 'mp3',
                            save_name: str = None,
                            verbose: bool = False
                            ):
        base_cmnd = 'youtube-dl -x'
        if verbose == True:
            base_cmnd += ' -q'

        base_cmnd += f' --audio-format {out_format} '
        base_cmnd += vid_link

        if save_name:
            save_path = os.path.join(self.save_dir, save_name)
            base_cmnd += f" -o '{save_path}/.%(ext)s'"
        else:
            base_cmnd += f" -o '{self.save_dir}/%(title)s.%(ext)s'"

        return base_cmnd

    def _save_from_youtube(self, song_name, parse_limit=2):

        vid_ids = self._get_vid_id(song_name=song_name,
                                   limit=parse_limit)

        # Download audio format of those videoids
        def get_vid_link(x): return f'{self.vid_base_link}{x}'
        vid_links = [get_vid_link(vidi) for vidi in vid_ids]

        for vid_link in vid_links:
            youtube_dl_cmnd = self._construct_cli_cmnd(vid_link=vid_link)
            print(youtube_dl_cmnd)
            os.system(youtube_dl_cmnd)
            # print(f'### Downloaded Song - {vid_link} to {self.save_dir}}')

    def download_songs(self,
                        song_names: list
                        ):
        for song_name in song_names:
            self._save_from_youtube(song_name=song_name)
            print(f"## Downloaded Song - {song_name}")
