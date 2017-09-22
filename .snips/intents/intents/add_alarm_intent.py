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

class AddAlarmIntent:

    intentName = "AddAlarm"

    def __init__(self, alarmDuration=None, alarmDescription=None, alarmTime=None):
        self.alarmDuration = alarmDuration
        self.alarmDescription = alarmDescription
        self.alarmTime = alarmTime
        
    @staticmethod
    def parse(payload):
        intentName = IntentParser.get_intent_name(payload)
        if intentName != AddAlarmIntent.intentName:
            return None
        return AddAlarmIntent(
            IntentParser.get_slot_value(payload, "alarmDuration"),
            IntentParser.get_slot_value(payload, "alarmDescription"),
            IntentParser.get_slot_value(payload, "alarmTime")
            )