from command import * 

r = Receiver()
c = ConcreteCommand(r)
i = Invoker()
i.set_command(c)
i.execute_command()