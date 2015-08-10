from .classify import Classify

class App(object):

    def run(self):
        classify = Classify()
        classify.extract()
