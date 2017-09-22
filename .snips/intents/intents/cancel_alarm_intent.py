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

class CancelAlarmIntent:

    intentName = "CancelAlarm"

    def __init__(self, alarmTime=None, alarmDescription=None):
        self.alarmTime = alarmTime
        self.alarmDescription = alarmDescription
        
    @staticmethod
    def parse(payload):
        intentName = IntentParser.get_intent_name(payload)
        if intentName != CancelAlarmIntent.intentName:
            return None
        return CancelAlarmIntent(
            IntentParser.get_slot_value(payload, "alarmTime"),
            IntentParser.get_slot_value(payload, "alarmDescription")
            )