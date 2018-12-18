
from adapt.intent import IntentBuilder
from mycroft.skills.core import MycroftSkill
from mycroft.util.log import getLogger

import os
import pynput
keyboard = pynput.keyboard.Controller()

__author__ = 'cola'

LOGGER = getLogger(__name__)


class VoiceControlSkill(MycroftSkill):
    def __init__(self):
        super(VoiceControlSkill, self).__init__(name="VoiceControlSkill")

    def initialize(self):

        beamer_intent = IntentBuilder("BeamerIntent"). \
            require("BeamerKeyword").build()
        self.register_intent(beamer_intent,
                             self.handle_beamer_intent)

        table_intent = IntentBuilder("TableIntent"). \
            require("TableKeyword").build()
        self.register_intent(table_intent,
                             self.handle_table_intent)

        typewriter_intent = IntentBuilder("TypeWriterIntent"). \
            require("TypeWriterKeyword").build()
        self.register_intent(typewriter_intent,
                             self.handle_typewriter_intent)

    def handle_beamer_intent(self, message):
        beamer_screen()
        self.speak_dialog("changes.done")

    def handle_table_intent(self, message):
        table_screen()
        self.speak_dialog("changes.done")

    def handle_typewriter_intent(self, message):
        type(message)
        self.speak_dialog("changes.done")

    def stop(self):
        pass

def create_skill():
    return VoiceControlSkill()


def type( message ):
    print( " start typing " )
    print( dir(message) )
    #keyboard.type(message)

def beamer_screen():
    os.system("xrandr --output DVI-I-2 --mode 1920x1080 --output  DVI-I-3 --off --output HDMI-0 --mode 1920x1080")


def table_screen():
    os.system("xrandr --output DVI-I-2 --mode 1920x1080 --output DVI-I-3 --mode 1920x1080  --right-of DVI-I-2 --output HDMI-0 --off")