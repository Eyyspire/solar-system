from src.Controllers.Controller import Controller

class Test_Controller : 

    def setup_method(self):
        self.controller = ControllerMock()
        for _ in range(10):
            self.controller.subscribe(Subscriber())

    def test_controller_notifies_its_subscribers(self):
        for i in range(10):
            self.controller.notify_all()
            assert all(subscriber.call_acc == i+1 for subscriber in self.controller.subscribers)



class ControllerMock(Controller):

    def notify(self, subscriber):
        subscriber.increase()
        
class Subscriber:

    def __init__(self):
        self.call_acc = 0
    
    def increase(self):
        self.call_acc += 1