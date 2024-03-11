# imports
import logging
from collections import deque

from model.enums.loadStatus import LoadStatus
from model.enums.services import Services
from controller.listController import ListController
# declarations

DEQUE_MAXLEN=10

class AppController():
    def __init__(self, model, view):
        self.model = model 
        self.view = view
        self.model_history = deque(maxlen=DEQUE_MAXLEN)

    def run(self):
        if self.model.load() == -1:
            logging.error("Error loading model")
            return self._retry_previous_model_()
        self.view.display()
        self._handle_input_(self._get_input_())
        
    def _get_input_(self) -> tuple:
        cin = self.view.getInput()
        return (cin[0], cin[1])

    def _handle_input_(self, service, data):
        match service:
            case Services.RECIPES | Services.INGREDEINTS | Services.FAVORITES | Services.RECIPE | Services.INGREDIENT:
                new_model = self.model.load(service, data)
                if new_model:
                    self.model_history.append(self.model)
                    self.model = new_model
                    self.view = self._load_view_(service)
                    self.run()
            case Services.RECIPELISTS | Services.INGREDIENTLISTS:
                new_model = self.model.load(service, data)
                lc = ListController(service, new_model)
                if new_model & new_model != self.model:
                    new_model, service = lc.run()
                self.run()
            case Services.UPDATE:
                self.model.update(data)
                self.run()
            case Services.SELECT:
                self.model.create(data)
            case Services.ADD:
                self.model.add(data)
            case Services.OPEN:
                self.model.load(service, data)
            case Services.DELETE:
                self._retry_previous_model_(service)
            case _:
                logging.error("Invalid input:", service, data)
    
    def _retry_previous_model_(self, service=None):
        if self.model_history:
            previous_model = self.model_history.pop()
            if previous_model is not None:
                if service is Services.DELETE:
                    self.model.delete()
                    logging.debug()
                logging.info("Retrying previous model...")
                self.model = previous_model
                self.run()
        else:
            logging.error("No previous model to retry.")
            return -1
