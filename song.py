class Song:
    def __init__(self, title, filename, duration, url):
        # initializing instance variable
        self.title = title
        self.filename = filename
        self.duration = duration
        parts = duration.split(":")
        self.duration_in_minutes = float(parts[0]) + float(parts[1]) / 60.0
        self.url = url

    def __str__(self):
        phrase = (
            str(self.title)
            + "\n"
            + "duration: "
            + str(self.duration)
            + "\n url: "
            + str(self.url)
        )
        return phrase

    def __repr__(self):
        phrase = (
            str(self.title)
            + "\n"
            + "duration: "
            + str(self.duration)
            + "\n url: "
            + str(self.url)
        )
        return phrase
