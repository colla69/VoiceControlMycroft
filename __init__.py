
from adapt.intent import IntentBuilder

from mycroft.skills.core import MycroftSkill
from mycroft.util.log import getLogger

__author__ = 'cola'

LOGGER = getLogger(__name__)


class HelloWorldSkill(MycroftSkill):
    def __init__(self):
        super(HelloWorldSkill, self).__init__(name="HelloWorldSkill")

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

    def handle_thank_you_intent(self, message):
        self.speak_dialog("welcome")

    def handle_how_are_you_intent(self, message):
        self.speak_dialog("how.are.you")

    def handle_hello_world_intent(self, message):
        self.speak_dialog("hello.world")

    def stop(self):
        pass


def create_skill():
    return HelloWorldSkill()
