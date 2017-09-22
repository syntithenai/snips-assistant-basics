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

class BasicMathsIntent:

    intentName = "BasicMaths"

    def __init__(self, numberA=None, numberB=None, mathsOperator=None):
        self.numberA = numberA
        self.numberB = numberB
        self.mathsOperator = mathsOperator
        
    @staticmethod
    def parse(payload):
        intentName = IntentParser.get_intent_name(payload)
        if intentName != BasicMathsIntent.intentName:
            return None
        return BasicMathsIntent(
            IntentParser.get_slot_value(payload, "numberA"),
            IntentParser.get_slot_value(payload, "numberB"),
            IntentParser.get_slot_value(payload, "mathsOperator")
            )