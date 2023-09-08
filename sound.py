from sound_lib import output, stream
o = output.Output()


class Sound:
    def __init__(self, file: str):
        self.file = file
        self.s = stream.FileStream(file=self.file)

    def play(self):
        self.s.play()
