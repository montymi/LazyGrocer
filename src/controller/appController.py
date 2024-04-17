import logging

from model.enums.scripts import InsertScripts, SelectScripts

class AppController:
    def __init__(self):
        """
        Services:
        1. Display LIST OF Recipe, Ingredient
        """
        self.commands = []
        self.main = []
        self.selected = []
