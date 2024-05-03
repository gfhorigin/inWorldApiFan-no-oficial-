#from deep_translator import GoogleTranslator
import requests


class Chacters:
    def __init__(self,chacterId, tokenKey):
        self.chacterId = chacterId
        self.tokenKey = tokenKey
    def openSession(self, endUserID="1",givenName="user"):
        url = f'https://api.inworld.ai/v1/{self.chacterId}:openSession'
        headers = {"Content-Type": "application/json"
            , "authorization": f"Basic {self.tokenKey}"}
        myobj = {"character": self.chacterId
            , "user": {"endUserId": endUserID,"givenName":givenName}}

        req = requests.post(url, json = myobj, headers=headers)
        self.reqJ = req.json()
        print(self.reqJ)
    def sendText(self,text):


        sessionID = self.reqJ["name"]
        url = f'https://api.inworld.ai/v1/workspaces/default-kscfc5427wqjrybituptaq/sessions/{sessionID }/sessionCharacters/{self.reqJ["sessionCharacters"][0]["character"]}:sendText'

        headers = {"Content-Type": "application/json"
            , "authorization": f"Basic {self.tokenKey}"
            , "Grpc-Metadata-session-id": sessionID}
        myobj = {"text": text}

        req = requests.post(url, json = myobj, headers=headers)
        reqJ = req.json()
        return reqJ
    def simpleText(self,text,endUserFullname="user",endUserId="12345"):
        url = f'https://api.inworld.ai/v1/{self.chacterId}:simpleSendText'
        headers = {"Content-Type": "application/json"
                   ,"authorization": f"Basic {self.tokenKey}"}
        myobj = {"character": self.chacterId
                , "text": text
                ,"endUserFullname":endUserFullname, "endUserId":endUserId}

        req = requests.post(url, json=myobj, headers=headers)
        reqJ = req.json()
        return reqJ











"""while True:
        a= input()
        translator = GoogleTranslator(source='auto', target='en')
        forBot = translator.translate(a)
       # print(forBot)
        myobj = {"character":"workspaces/default-kscfc5427wqjrybituptaq/characters/andrei", "text":forBot,"session_id":f'{m["name"]}'}
        translator = GoogleTranslator(source='auto', target='ru')
        x = requests.post(url, json = myobj, headers=headers)
       # print(x)
        m=x.json()
        print(m)
        message =m['textList']

        #print(translator.translate(str(message)))
        for i in message:
            print(translator.translate(i))"""