import webbrowser

class Video():
    
    def __init__(self,video_title,video_duration):
        print("Parent Constructor called")
        self.title = video_title
        self.duration = video_duration
        
class Movie(Video):
    """ This class provides a way to store movie related information """
    VALID_RATINGS = ["G","PG","PG-13","R"]
    
    def __init__(self,movie_title, movie_duration, movie_storyline, poster_image,trailer_youtube):
        print("Child Movie Constructor called")
        Video.__init__(self,movie_title, movie_duration)
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)

class Program(Video):
    """ This class provides a way to store TV program related information """
    VALID_RATINGS = ["G","PG","PG-13","R"]
    
    def __init__(self,program_title, program_duration, movie_storyline, poster_image,trailer_youtube):
        print("Child TV Constructor called")
        Video.__init__(self,program_title, program_duration)
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
