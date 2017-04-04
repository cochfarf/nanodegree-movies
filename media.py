import webbrowser

class Movie ():
    """
    This class provides a way to store movie related information
    It currently initializes the title, storyline, url to an image of the poster,
    and the url to a trailer on youtube.
    To initialize an instant:
    instance_name = media.Movie("[title]","[story line text]","[url to poster]",
    "[url to trailer]")

    The class also contains the function show_trailer which opens the trailer in
    a web browser with the built in webbrowser module.
    """
    #VALID_RATINGS = ["G", "PG", "PG-13", "R"] ratings not used in current code
    def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube):
        #uper(self).__init__()
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
