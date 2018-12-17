import os

from adapt.intent import IntentBuilder

from mycroft.skills.core import MycroftSkill
from mycroft.util.log import getLogger

__author__ = 'cola'

LOGGER = getLogger(__name__)


class VoiceControlSkill(MycroftSkill):
    def __init__(self):
        super(VoiceControlSkill, self).__init__(name="VoiceControlSkill")

    def initialize(self):
        thank_you_intent = IntentBuilder("ThankYouIntent"). \
            require("ThankYouKeyword").build()
        self.register_intent(thank_you_intent, self.handle_thank_you_intent)

        how_are_you_intent = IntentBuilder("HowAreYouIntent"). \
            require("HowAreYouKeyword").build()
        self.register_intent(how_are_you_intent,
                             self.handle_how_are_you_intent)

        hello_world_intent = IntentBuilder("HelloWorldIntent"). \
            require("HelloWorldKeyword").build()
        self.register_intent(hello_world_intent,
                             self.handle_hello_world_intent)

        beamer_intent = IntentBuilder("BeamerIntent"). \
            require("BeamerKeyword").build()
        self.register_intent(beamer_intent,
                             self.handle_beamer_intent)

        table_intent = IntentBuilder("TableIntent"). \
            require("TableKeyword").build()
        self.register_intent(table_intent,
                             self.handle_table_intent)

    def handle_thank_you_intent(self, message):
        self.speak_dialog("welcome")

    def handle_how_are_you_intent(self, message):
        self.speak_dialog("how.are.you")

    def handle_hello_world_intent(self, message):
        self.speak_dialog("hello.world")

    def handle_beamer_intent(self, message):
        beamer_screen()
        self.speak_dialog("changes.done")

    def handle_table_intent(self, message):
        table_screen()
        self.speak_dialog("changes.done")

    def stop(self):
        pass


def create_skill():
    return VoiceControlSkill()


def beamer_screen():
    os.system("xrandr --output DVI-I-2 --mode 1920x1080 --output  DVI-I-3 --off --output HDMI-0 --mode 1920x1080")


def table_screen():
    os.system("xrandr --output DVI-I-2 --mode 1920x1080 --output DVI-I-3 --mode 1920x1080  --right-of DVI-I-2 --output HDMI-0 --off")