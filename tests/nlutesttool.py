# -*-: coding utf-8 -*-
"""The run command."""
# pylint: disable=too-few-public-methods,import-error

import os
import subprocess
import time
import json
import threading

from sys import path

import paho.mqtt.client as mqtt

from socket import error as socket_error
from gtts import gTTS

path.append(".snips/intents")
path.append(".snips/intents/intents")

from snipsskillscore.logging import debug_log

from snipsskillscore.audio_player import AudioPlayer

from snipsskills.utils.snipsfile_parser import Snipsfile, SnipsfileParseException, \
    SnipsfileNotFoundError
from snipsskills.utils.snips import Snips, SnipsNotFound, SnipsRuntimeFailure

from snipsskillscore.logging import log, log_success, log_warning, log_error
from snipsskillscore.server import Server
from snipsskillscore.instant_time import InstantTime
from snipsskillscore.time_interval import TimeInterval

from snipsskills.commands.base import Base, SNIPSFILE


# pylint: disable=wrong-import-position,wrong-import-order
from intent_registry import IntentRegistry
# pylint: disable=wildcard-import,wrong-import-position,wrong-import-order
from intents import *

BINDINGS_FILE = "bindings.py"
INTENT_REGISTRY_FILE = ".snips/intents/intent_registry.py"




class NluTestTool():

    intentsPending={};
    intentsMatched={};
        
    # pylint: disable=undefined-variable,exec-used,eval-used
    def run(self,questions,test):
        self.questions = questions
        self.test = test
        """ Command runner. """
        '''
                fo = open("vocabulary_tests.json", "r+")
                str = fo.read(10);
               print "Read String is : ", str
                # Close opend file
                fo.close()
        '''    
        snipsfile_path = SNIPSFILE
        #snipsfile_path = "tests/{}".format(SNIPSFILE)
        try:
            self.snipsfile = Snipsfile(snipsfile_path)
        except SnipsfileNotFoundError:
            log_error("Snipsfile not found. Please create one.")
            return
        except SnipsfileParseException as err:
            log_error(err)
            return

        self.locale = self.snipsfile.locale.split("_")[0]
        self.mqtt_topic = "hermes/nlu/query"
        self.mqtt_client = mqtt.Client("SnipsTTS")
        #log("speak")
        try:
            self.mqtt_client.connect(self.snipsfile.mqtt_hostname, self.snipsfile.mqtt_port)
            #log("connected")
            self.mqtt_client.loop_start()
            self.mqtt_client.subscribe('/hermes/nlu/intentParsed')
            self.mqtt_client.on_message = self.on_message
            
        except (socket_error, Exception) as e:
            #log("connect error")
            time.sleep(5)
        #time.sleep (3)
        for question in self.questions:
            self.speak(question['text'])
            questionSlots={}
            for slot in question['response']['slots']:
                questionSlots[slot['slotName']] = slot
            pendingIntent = {'intent':question['response']['intent'], 'slots':questionSlots}
            self.intentsPending[question['text']] = pendingIntent
            time.sleep(2)
            
        time.sleep (20)
        #print('responses')
        #print(self.intentsPending)
        #print('matches')
        #print(self.intentsMatched)
        # did we match all the questions?
        return self.intentsMatched
        

    def on_message(self,client, userdata, msg):
        print("ONMESSAGE")
        #print(msg.topic+" "+str(msg.payload))
        payload = json.loads(msg.payload)
        # index incoming payload slots by slotname
        payloadSlots={}
        #print(payload['slots'])
        for slot in payload['slots']:
            payloadSlots[slot['slotName']] = slot['value']
            payloadSlots[slot['slotName']]['slotName'] = slot['slotName']

        # slots/[]/slotName,value/kind,value/value
        # is there a pending request that matches ?
        if self.intentsPending[payload['input']] is not None:
            expectedResponse = self.intentsPending[payload['input']]
            print('EXPECT INTENT')
            print(expectedResponse['intent'])
            print('EXPECT')
            print(expectedResponse)
            print('GOT INTENT')
            print(payload['intent']['intentName'])
            print('GOT SLOTS')
            print(payloadSlots)
                
            # check for intent match
            if payload['intent']['intentName'].endswith(expectedResponse['intent']):
                # check slot matches
                slotFailed = False
                for slot in expectedResponse['slots']:
                    print('EXPECT SLOT')
                    print(slot)
                    
                    #slotName = expectedResponse['slots'][slot]['slotName']
                    if slot in payloadSlots and payloadSlots[slot] is not None:
                        matchingSlot = payloadSlots[slot]
                        #print('MATCH {}'.format(matchingSlot))
                        for slotField in expectedResponse['slots'][slot]:
                            if slotField in matchingSlot and matchingSlot.get(slotField) is not None and expectedResponse['slots'][slot].get(slotField) == matchingSlot.get(slotField) :
                                pass #
                                print("SLOT match {}".format(slotField))
                            else:
                                print("SLOT fail {}".format(slotField))
                                slotFailed = True
                                
                if not slotFailed:
                    #self.test.assertEqual(expectedResponse['slots'][slot].get(slotField),matchingSlot.get(slotField))
                    print('slot found')
                    del self.intentsPending[payload['input']]
                    self.intentsMatched[payload['input']] = payload
                else: 
                    pass
                    print('slot failed')
            else:
                pass
                print('NO MATCH ON INTENT')
        else:
            pass
            #print('found not')
        print "------------------------------------------------------"
        
    
    def speak(self, sentence):
        log("PUBLISH - {}".format(sentence))   
        # 4.511 - seconds
        self.mqtt_client.publish(
            self.mqtt_topic,
            payload=json.dumps({'likelihood': 1.0, 'seconds': len(sentence)/2.5, "text": sentence}),  
            qos=0,
            retain=False)
