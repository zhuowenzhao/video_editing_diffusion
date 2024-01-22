from moviepy.editor import VideoFileClip

class VideoProcess:
    def __init__(self, mp4vid_path: str = None, generated_path: str = None):
        self.mp4vid_path = mp4vid_path
        self.orig_vid = VideoFileClip(self.mp4vid_path) if self.mp4vid_path is not None else self.mp4vid_path
        self.new_vid = VideoFileClip(generated_path) if generated_path is not None else generated_path
        self.audio = self.orig_vid.audio if self.orig_vid is not None else None

    def gifs2mp4(self):
        assert self.new_vid_path is not None, 'Output path is None. Please provide a valid gif file path.'
        self.new_gifs.write_videofile(f"{self.new_mp4}.mp4", codec='mpeg4')


    def video(self, out_name: str = 'edited_video.mp4'):
        audio = self.audio.subclip(0, self.new_vid.duration)
        combined_vid = self.new_vid.set_audio(audio)
        combined_vid.write_videofile(out_name, codec='libx264', audio_codec='aac')


    def mp42gifs(self, 
                 start: int = 0, 
                 end: int = 0, 
                 outname: str = 'output.gif', 
                 resize: bool = None, 
                 size: tuple = (512, 512)):

        clip = self.orig_vid
        if hasattr(self.new_vid, 'duration'):
            clip = self.orig_vid.subclip(0, self.new_vid.duration)
        
        if resize:
            clip = clip.resize(newsize=size)
        
        clip.write_gif(outname)
        

    def __repr__(self):
        """
            The print information (total frame, duration, and FPS) about an input mp4 video.
        """
        return f'Basic information about the input video {self.mp4vid_path}:\n \
                 FPS: {self.orig_vid.fps}\tDuration: {self.orig_vid.duration}\t \
                 Total frames: {int(self.orig_vid.fps*self.orig_vid.duration)}'

