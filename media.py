import webbrowser
# class named Movie which serves as a blue print for the moive attributes
""" a class movie is created whose value
self relates the init function  to the
entertainment_center.py and lets to
create differentinstances of class Movie"""


class Movie():
    def __init__(self, movie_title,
                 movie_storyline, poster_image,
                 trailer_youtube):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
