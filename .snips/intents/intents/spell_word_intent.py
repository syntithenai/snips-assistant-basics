# -*-: coding utf-8 -*-
""" Auto-generated intent class. """

# *****************************************************************************
# *****************************************************************************
# *****************************************************************************
#
# WARNING: THIS IS AN AUTO-GENERATED FILE
# DO NOT ATTEMPT TO EDIT IT, AS CHANGES WILL BE OVERWRITTEN.
#
# *****************************************************************************
# *****************************************************************************
# *****************************************************************************

# pylint: disable=line-too-long

from snipsskillscore.intent_parser import IntentParser

class SpellWordIntent:

    intentName = "SpellWord"

    def __init__(self, wordToSpell=None):
        self.wordToSpell = wordToSpell
        
    @staticmethod
    def parse(payload):
        intentName = IntentParser.get_intent_name(payload)
        if intentName != SpellWordIntent.intentName:
            return None
        return SpellWordIntent(
            IntentParser.get_slot_value(payload, "wordToSpell")
            )