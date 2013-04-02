class Command(object):
    def __init__(self, receiver):
        self.receiver = receiver    
    def execute(self):
        pass

class ConcreteCommand(Command):
    def execute(self):
        self.receiver.action()

class Invoker(object):
    def set_command(self, command):
        self.command = command

    def execute_command(self):
        self.command.execute()

class Receiver(object):
    def action(self):
        print "action!"