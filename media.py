class Movie:
    """ This is a class that stores information about movies
        Attributes:
           title = stores the movie title
           poster_image_url = stores the moovie poster url from wiki
           trailer_youtube_url = stores the movie trailer url from youtube
    """
    def __init__(self, movie_title, movie_poster_url, movie_trailer_url):
        self.title = movie_title
        self.poster_image_url = movie_poster_url
        self.trailer_youtube_url= movie_trailer_url
