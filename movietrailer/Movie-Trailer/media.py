import webbrowser as wb


class Movie:
    """
    Movie class let's you instantiate movie objects
    and show their trailer directly into web browser.
    """

    def __init__(self, title, storyline, poster_image_url,
                 trailer_youtube_url):
        """
        The Constructor takes in 4 parameters that define the
        Movie object
        params:
        title: Title of the Movie
        storyline: An overview of the movie
        poster_image_url: URL of the display image
        trailer_youtube_url: URL of trailer
        """
        self.title = title
        self.storyline = storyline
        self.poster_image_url = poster_image_url
        self.trailer_youtube_url = trailer_youtube_url

    def show_trailer(self):
        """
        This function starts the trailer on web browser.
        Caution: Make sure to change the path of the web browser!
        """
        ffpath = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe'
        wb.register('chrome', None, wb.BackgroundBrowser(ffpath), 1)
        chrome = wb.get('chrome')
        chrome.open(self.trailer_youtube)
