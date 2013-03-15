class Singleton(object):
    instance = None

    def __init__(self):
        pass

    @staticmethod
    def get_instance():
        if Singleton.instance is None:
            Singleton.instance = Singleton()

        return Singleton.instance
