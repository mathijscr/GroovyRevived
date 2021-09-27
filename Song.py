

class Song:
    def __init__(self):
        # initializing instance variable
        self.title = ""
        self.filename = ""
        self.duration = 0
        self.duration_in_minutes = 0
        self.url = ""

    def __init__(self, title, filename, duration, url):
        # initializing instance variable
        self.title = title
        self.filename = filename
        self.duration = duration
        parts = duration.split(":")
        self.duration_in_minutes = float(parts[0]) + float(parts[1]) / 60.0
        self.url = url

    def __str__(self):
        phrase = str(self.title) + "\n" + "duration: " + str(self.duration) + "\n url: " + str(self.url)
        return phrase

    def __repr__(self):
        phrase = str(self.title) + "\n" + "duration: " + str(self.duration) + "\n url: " + str(self.url)
        return phrase

    def get_filename(self):
        return self.filename

    def get_title(self):
        return self.title

    def get_duration(self):
        return self.duration

    def get_duration_in_minutes(self):
        return self.duration_in_minutes

    def get_url(self):
        return self.url
