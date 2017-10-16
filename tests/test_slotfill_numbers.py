from unittest import TestCase
from nlutesttool import NluTestTool

class SlotFillingNumbersTest(TestCase):
    questions=[ 
    
    #A 
    # times 3 
    # OK but not for voice tests - certainty value ???
    {'text':'seven times three','response':{'intent':'BasicMaths','slots':[{'slotName':'numberA','kind':'Number','value':7.0},{'slotName':'numberB','kind':'Number','value':3.0},{'slotName':'mathsOperator','value':'multiplied by'}]}} \
    # times by or multipled by works fine
    ,{'text':'seven times by three','response':{'intent':'BasicMaths','slots':[{'slotName':'numberA','kind':'Number','value':7.0},{'slotName':'numberB','kind':'Number','value':3.0},{'slotName':'mathsOperator','value':'multiplied by'}]}} \
    # also 7,8 OK but not for voice
    # FAIL - ident as whatisthetime intent
    ,{'text':'seven times eight','response':{'intent':'BasicMaths','slots':[{'slotName':'numberA','kind':'Number','value':7.0},{'slotName':'numberB','kind':'Number','value':8.0},{'slotName':'mathsOperator','value':'multiplied by'}]}} \
    # OK
    ,{'text':'seven times by seven','response':{'intent':'BasicMaths','slots':[{'slotName':'numberA','kind':'Number','value':7.0},{'slotName':'numberB','kind':'Number','value':7.0},{'slotName':'mathsOperator','value':'multiplied by'}]}} \
    
    # B
    # plus and minus are absorbed into adjacent number slots
    # SOLN: assume addition where operator is not recognised 
    # FAIL - value -47
    ,{'text':'seven minus seven','response':{'intent':'BasicMaths','slots':[{'slotName':'numberA','kind':'Number','value':7.0},{'slotName':'numberB','kind':'Number','value':7.0},{'slotName':'mathsOperator','value':'minus'}]}} \
    # OK
    ,{'text':'seven plus seven','response':{'intent':'BasicMaths','slots':[{'slotName':'numberA','kind':'Number','value':7.0},{'slotName':'numberB','kind':'Number','value':7.0},{'slotName':'mathsOperator','value':'plus'}]}} \
    
    #C 
    # to and for are not absorbed into slots as numbers
    # OK but not for voice tests
    ,{'text':'two plus to','response':{'intent':'BasicMaths','slots':[{'slotName':'numberA','kind':'Number','value':2.0},{'slotName':'numberB','kind':'Number','value':2.0},{'slotName':'mathsOperator','value':'plus'}]}} \
    # FAIL
    ,{'text':'two plus for','response':{'intent':'BasicMaths','slots':[{'slotName':'numberA','kind':'Number','value':2.0},{'slotName':'numberB','kind':'Number','value':4.0},{'slotName':'mathsOperator','value':'plus'}]}} \
    
    #D
    # minus has strange interpretation into slot as multiplication - five minus two = -10
    # FAIL
    ,{'text':'five minus two','response':{'intent':'BasicMaths','slots':[{'slotName':'numberA','kind':'Number','value':5.0},{'slotName':'numberB','kind':'Number','value':2.0},{'slotName':'mathsOperator','value':'minus'}]}} \
    ]
    
    def test_run(self):
        tool = NluTestTool()
        matches = tool.run(self.questions,self)
        #print('MATCHES {}'.format(matches))
        #self.assertEqual(len(self.questions),len(matches))


"""

[14:56:14.531870] - hermes/nlu/intentParsed
{
  "input": "money five dollars and twenty three cents",
  "intent": {
    "intentName": "user_Kr5A7b4OD__TestAmountOfMoney",
    "probability": 1.0
  },
  "slots": [
    {
      "entity": "snips/amountOfMoney",
      "range": {
        "end": 41,
        "start": 6
      },
      "rawValue": "five dollars and twenty three cents",
      "slotName": "money1",
      "value": {
        "kind": "AmountOfMoney",
        "precision": "Exact",
        "unit": "$",
        "value": 5.23
      }
    }
  ]
}

"""
