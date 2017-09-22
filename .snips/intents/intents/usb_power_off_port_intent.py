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

class UsbPowerOffPortIntent:

    intentName = "UsbPowerOffPort"

    def __init__(self, usbPortIdentifier=None):
        self.usbPortIdentifier = usbPortIdentifier
        
    @staticmethod
    def parse(payload):
        intentName = IntentParser.get_intent_name(payload)
        if intentName != UsbPowerOffPortIntent.intentName:
            return None
        return UsbPowerOffPortIntent(
            IntentParser.get_slot_value(payload, "usbPortIdentifier")
            )