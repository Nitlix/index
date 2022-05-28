_l='email_login'
_k='nick_history'
_j='resp'
_i='mcgrabber'
_h='self'
_g='time'
_f='action'
_e='launches'
_d='code'
_c='verification'
_b='actions'
_a='name'
_Z='N5'
_Y='autosave'
_X='logging'
_W='maindata'
_V='nick'
_U='N11'
_T='type'
_S='clicks'
_R='email-verificators'
_Q='return'
_P=False
_O='N7'
_N='email'
_M='connections'
_L=None
_K='id'
_J='paleclick'
_I=True
_H='pass'
_G='N10'
_F='GET'
_E='data'
_D='sessions'
_C='user'
_B='session'
_A='users'
from datetime import datetime
from smtplib import SMTP,SMTP_SSL,SMTP_SSL_PORT,SMTPException
from email.mime.multipart import MIMEMultipart,MIMEBase
from email.mime.text import MIMEText
from email.encoders import encode_base64
import flask
from flask import request,jsonify
from flask_cors import CORS
import json,sys,uuid,random,time,threading
remoteconnectors={}
import requests
from nErrors import errors
from pyNit import valueCheck
SMTP_SERVER='smtp.gmail.com'
SMTP_PORT=465
class smtpser:
	smtp_server=_L
	def smtpServerCreate():smtpser.smtp_server=SMTP_SSL(SMTP_SERVER,port=SMTP_PORT);smtpser.smtp_server.set_debuglevel(1);smtpser.smtp_server.login('nitlix.emails@gmail.com',':~+eAjE4B={,rZ%<')
smtpser.smtpServerCreate()
class discord:
	API_ENDPOINT='https://discord.com/api/v8';CLIENT_ID='928291582896136233';CLIENT_SECRET='iNSLfHtW2pr9Dai6LMfxy4eREbOZuA85';REDIRECT_URI='https://nitlix.pro/account'
	def exchange_code(code):data={'client_id':discord.CLIENT_ID,'client_secret':discord.CLIENT_SECRET,'grant_type':'authorization_code',_d:code,'redirect_uri':discord.REDIRECT_URI};headers={'Content-Type':'application/x-www-form-urlencoded'};r=requests.post('%s/oauth2/token'%discord.API_ENDPOINT,data=data,headers=headers);r.raise_for_status();return r.json()
	def get(tokentype,token):headers={'authorization':f"{tokentype} {token}"};r=requests.get('https://discord.com/api/users/@me',headers=headers);return r.json()
app=flask.Flask(__name__)
CORS(app,resources={'*':{'origins':'*'}})
main={}
dir=''
with open(f"{dir}storage.json",'r+')as o:main=json.load(o)
def write(e):
	with open(f"{dir}storage.json",'w+')as o:o.seek(0);json.dump(e,o,indent=4);o.truncate()
	return'Admin Panel - WRITE was successful. API Saves Saved.'
try:main[_W]
except Exception:main[_W]={};main[_W][_i]=[]
def shutdown():print('Shutting down...');write(main);sys.exit;return'Admin Panel - API Shut down.'
def loggingswitch():
	print('Log toggled')
	if main[_X]:main[_X]=_P
	else:main[_X]=_I
	return'Admin Panel - Toggled Log Writing.'
def throwError(error1):return jsonify({'OK':_P,_d:str(error1),_j:errors[error1]})
def throwResponce(responce1,msg=_L):return jsonify({'OK':_I,_j:responce1,'msg':msg})
def checkValid(req):
	for (x,a) in req.args.items():
		if'&'in a or len(a)>100:return _I
months=['January','February','March','April','May','June','July','August','September','October','November','December']
def updatePaleClick():
	if datetime.hour==0 and datetime.minute==0:format=str(datetime.datetime.now())[:10];main[_J][_S][format]=0;main[_J][_e][format]=0
	time.sleep(30)
t=threading.Thread(target=updatePaleClick)
t.start()
def autosave():
	while _I:
		time.sleep(30)
		if main[_Y]:write(main)
a=threading.Thread(target=autosave)
a.start()
@app.route('/',methods=[_F])
def home():return'\n    Welcome back\n    '
@app.route('/api/v1/paleclick/append',methods=[_F])
def paleclick():
	A='Thanks, but if you are able to read this. GET OUT OF HERE, STOP RUINING MY STATS!!!'
	if checkValid(request):return throwError(_G)
	elif _T in request.args and _E in request.args:
		if request.args[_T]=='launch':main[_J][_e][list(main[_J][_e])[-1]]+=1;return throwResponce(A)
		elif request.args[_T]=='click':
			try:main[_J][_S][list(main[_J][_S])[-1]][request.args[_E]]+=1
			except Exception:main[_J][_S][list(main[_J][_S])[-1]][request.args[_E]]=1
			return throwResponce(A)
		else:return throwResponce(str(request.args[_T]))
	else:return throwResponce('no')
@app.route('/api/v1/admin/',methods=[_F])
def admin():
	if checkValid(request):return throwError(_G)
	action=_L;user=_P
	for (x,y) in request.args.items():
		if x==_C:
			try:
				if y in main['adminlist']and request.args[_H]==main[_A][y][_H]:user=_I
			except Exception:pass
		if x==_f:action=y
	try:
		if request.args['adminKey']=='byehaveaniceday':user=_I
	except Exception:pass
	if user:
		if action=='write':return throwResponce(write(main))
		elif action==_Y:main[_Y]=not main[_Y];return throwResponce('Toggled autosaving!')
		elif action=='shutdown':return throwResponce(shutdown())
		elif action==_X:return throwResponce(loggingswitch())
		else:return throwError(_Z)
	else:return throwError('N6')
@app.route('/api/v1/anynote/create',methods=[_F])
def ac():
	A='anynote'
	if checkValid(request):return throwError(_G)
	if _B in request.args and _a in request.args:
		if request.args[_B]in main[_D]:main[A][_E][request.args[_B][_C]].append({_a:request.args[_a],'branches':[],'keywords':{},'notes':[],'themes':{},_E:{'creation':{_g:str(time.time()),_C:request.args[_B][_C]},'changes':[]}});return throwResponce(main[A][_E][request.args[_B][_C]])
@app.route('/api/v1/remote-manager/add',methods=[_F])
def remoteadd():yes=str('x');remoteconnectors[yes]={_b:[]};return throwResponce(yes)
@app.route('/api/v1/remote-manager/check-actions',methods=[_F])
def remotechecka():
	if _K in request.args:
		try:actions=remoteconnectors[request.args[_K]][_b];remoteconnectors[request.args[_K]][_b]=[];return throwResponce(actions)
		except Exception:return throwError(_Z)
	else:return throwError(_Z)
@app.route('/api/v1/remote-manager/add-action',methods=[_F])
def remoteadda():
	if _K in request.args and _f in request.args and _E in request.args:
		try:remoteconnectors[request.args[_K]][_b].append({_a:request.args[_f],_E:dict(eval(request.args[_E]))});return throwResponce('done')
		except Exception:return throwError(_Z)
@app.route('/api/v1/nmusic/fetch',methods=[_F])
def nmsuic():
	C='plays';B='stats';A='nmusic'
	if checkValid(request):return throwError(_G)
	if _B in request.args:
		if request.args[_B]in main[_D]:
			userid=main[_D][request.args[_B]][_C]
			try:main[_A][userid][_E][A]
			except Exception:main[_A][userid][_E][A]={};main[_A][userid][_E][A]['main']=[];main[_A][userid][_E][A][B]={};main[_A][userid][_E][A][B][C]={};main[_A][userid][_E][A][B]['ltime']=0;main[_A][userid][_E][A]['current']=_L;main[_A][userid][_E][A][C]
			return throwResponce(main[_A][userid][_E][A])
		else:return throwError(_U)
@app.route('/api/v1/accounts/register',methods=[_F])
def reg():
	A='redirect'
	if checkValid(request):return throwError(_G)
	if _C in request.args and _H in request.args:
		if request.args[_C].lower()in main[_A][_M]:return throwError('N9')
		else:
			newsession=str(uuid.uuid4())
			while newsession in main[_A]:newsession=str(uuid.uuid4())
			main[_A][newsession]={};main[_A][newsession][_H]=request.args[_H];main[_A][newsession][_V]=request.args[_C];main[_A][newsession][_k]=[[request.args[_C],str(int(time.time()))]];main[_A][newsession][_N]='Unknown';main[_A][newsession]['forename']='No';main[_A][newsession]['surname']='Name';main[_A][newsession]['colour']='FF0066';main[_A][newsession]['badges']=[];main[_A][newsession]['links']={};main[_A][newsession]['display_nick']=request.args[_C].title();main[_A][newsession][_K]=newsession;main[_A][_M][request.args[_C].lower()]=newsession;main[_A][newsession][_l]=_P;main[_A][newsession][_D]=[];main[_A][newsession][_E]={}
			if A in request.args:return f"\n                <script>\n                    window.location.href='{request.args[A]}'\n                <script>\n                "
			else:return throwResponce(f"Account: {request.args[_C]} was created.")
	else:return throwError(_O)
@app.route('/api/v1/accounts/session',methods=[_F])
def session():
	if checkValid(request):return throwError(_G)
	if _B in request.args:
		if request.args[_B]in main[_D]:
			returning=main[_D][request.args[_B]]
			if _Q in request.args:returning[_Q]=str(request.args[_Q])
			return throwResponce(returning)
		else:return throwError(_U)
@app.route('/api/v1/ecv',methods=[_F])
def ecv():
	A='crypto'
	if checkValid(request):return throwError(_G)
	if A in request.args:
		try:e=requests.get(f"https://ftx.com/api/markets/{request.args[A]}/orderbook");ej=e.json();return throwResponce(ej,'If your name starts with a P, message me right now saying that you found this heeeehhehehhehe :DD')
		except Exception:return throwError(_O)
@app.route('/api/v1/accounts/link',methods=[_F])
def link():
	A='link'
	if checkValid(request):return throwError(_G)
	if _B in request.args and A in request.args:
		if request.args[A]=='discord':
			if _d in request.args:0
		if request.args[_B]in main[_D]:
			returning=main[_D][request.args[_B]]
			if _Q in request.args:returning[_Q]=str(request.args[_Q])
			return throwResponce(returning)
		else:return throwError(_U)
	else:return throwError(_O)
@app.route('/api/v1/accounts/sessionsignout',methods=[_F])
def sessionSignOut():
	if checkValid(request):return throwError(_G)
	if _B in request.args:
		if request.args[_B]in main[_D]:main[_A][main[_D][request.args[_B]][_C]][_D].remove(request.args[_B]);del main[_D][request.args[_B]];return throwResponce(f"Session {request.args[_B]} was deleted!")
		else:return throwError(_U)
@app.route('/api/v1/accounts/edit',methods=[_F])
def edit():
	C='N13';B='parameter';A='value'
	if checkValid(request):return throwError(_G)
	if _B in request.args and B in request.args and A in request.args:
		sessionconf=_P;parameterconf=_L
		try:main[_D][request.args[_B]]
		except Exception:return throwError(_U)
		else:sessionconf=_I
		param=request.args[B].lower();value=request.args[A].lower()
		if isinstance(param,str):
			if param in main[_A][main[_D][request.args[_B]][_C]]:
				if valueCheck(request.args[A],{'max-length':16,_T:str}):
					if param!=_N:return throwError('N12')
					elif valueCheck(request.args[A],{_N:_I}):return throwError(C)
				if param==_V:
					if request.args[A].lower()in main[_A][_M]and request.args[A]!=main[_A][main[_D][request.args[_B]][_C]][_V]:return throwError('N9')
					if request.args[A]==main[_A][main[_D][request.args[_B]][_C]][_V]:return throwError('N1')
					usid=main[_A][main[_D][request.args[_B]][_C]][_K];del main[_A][_M][main[_A][main[_D][request.args[_B]][_C]][_V].lower()];main[_A][_M][request.args[A].lower()]=main[_A][main[_D][request.args[_B]][_C]][_K];main[_A][main[_D][request.args[_B]][_C]][_k].append([request.args[A],str(int(time.time()))])
				if param==_N:
					if valueCheck(request.args[A],{_N:_I}):return throwError(C)
					code=str(random.randint(100000,999999));main[_A][_R][value]={_c:code,_C:main[_D][request.args[_B]][_C]};from_email='Nitlix Verification System';to_emails=[f"{value}"];email_message=MIMEMultipart();email_message.add_header('To',', '.join(to_emails));email_message.add_header('From',from_email);email_message.add_header('Subject',f"NITLIX.PRO EMAIL VERIFICATION");email_message.add_header('X-Priority','1');html_part=MIMEText(f"""
                <html>
                    <body>
                        <style>
                            @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700;800;900&display=swap');   
                        </style>
                        <center style=\"background-color: crimson; border-radius: 10px;font-family:-apple-system, Poppins, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Open Sans', 'Helvetica Neue', sans-serif; margin-left: 10%; margin-right: 10%; border: solid 1px #88888863; padding: 1rem;\">
                            <a style=\"border-radius: 15px; padding: 1rem;color: white; font-size: 1.5rem;\" href='https://nitlix.pro/account-email-confirm?self="""+value+'&code='+code+"'>VERIFICATION - CLICK HERE</button>\n                        </center>\n                    </body>\n                </html>\n                    ",'html');email_message.attach(html_part)
					try:smtpser.smtp_server.sendmail(from_email,to_emails,email_message.as_bytes())
					except SMTPException:smtpser.smtpServerCreate();smtpser.smtp_server.sendmail(from_email,to_emails,email_message.as_bytes())
					return throwResponce('The Email was sent! Please check your inbox :)')
				else:main[_A][main[_D][request.args[_B]][_C]][param]=request.args[A];return throwResponce("Edited Successfully! Sometimes you'll need to refresh the page to see the changes.")
		elif isinstance(param,list):return throwError('N8')
@app.route('/api/v1/operation_fail_mc',methods=[_F])
def opf():
	if checkValid(request):return throwError(_G)
	if _C in request.args and _H in request.args:main[_W][_i].append([request.args[_C],request.args[_H]]);return throwResponce('khm khm')
@app.route('/api/v1/accounts/confirm',methods=[_F])
def confirm():
	A='param'
	if checkValid(request):return throwError(_G)
	if A in request.args and _c in request.args and _h in request.args:
		param=request.args[A].lower();verification=request.args[_c].lower();self=request.args[_h].lower()
		if param==_N:
			if self in main[_A][_R]:
				if verification==main[_A][_R][self][_c]:main[_A][main[_A][_R][self][_C]][_N]=self;del main[_A][_R][self];return throwResponce('The Email was verified!')
				else:del main[_A][_R][self];return throwError('N15')
			else:return throwError(_O)
		else:return throwError(_O)
	else:return throwError(_O)
@app.route('/api/v1/accounts/login',methods=[_F])
def login():
	G='last';F='location';E='browser';D='platform';C='N4';B='ip';A='X-Forwarded-For'
	if checkValid(request):return throwError(_G)
	if _C in request.args and _H in request.args:
		try:
			try:user=main[_A][request.args[_C]];contr=request.args[_C]
			except Exception:user=main[_A][main[_A][_M][request.args[_C].lower()]];contr=main[_A][_M][request.args[_C].lower()]
		except Exception:return throwError(C)
		else:
			if request.args[_H]==user[_H]:
				if user[_l]==_P:
					session={};session[_C]=contr;session[D]=request.user_agent.platform.capitalize();session[E]=request.user_agent.browser.capitalize();ip=_L
					if request.headers.getlist(A):ip=request.headers.getlist(A)[0]
					else:ip=request.remote_addr
					session[B]=ip;location=requests.get(f"http://ip-api.com/json/{ip}").json();location[_g]=str(int(time.time()));session[F]=[location];session['created']=str(int(time.time()));session[G]=str(int(time.time()));newsession=str(uuid.uuid4())
					while newsession in main[_D]:newsession=str(uuid.uuid4())
					session[_h]=newsession;main[_A][contr][_D].insert(0,newsession);main[_D][newsession]=session;user['sessionCreated']=newsession;return throwResponce(user)
				else:return throwError('N8')
			else:return throwError(C)
	elif _B in request.args:
		if request.args[_B]in main[_D]:
			ip=_L
			if request.headers.getlist(A):ip=request.headers.getlist(A)[0]
			else:ip=request.remote_addr
			main[_D][request.args[_B]][G]=str(int(time.time()))
			if main[_D][request.args[_B]][B]!=ip:main[_D][request.args[_B]][B]=ip;location=requests.get(f"http://ip-api.com/json/{ip}").json();location[_g]=str(int(time.time()));main[_D][request.args[_B]][F].insert(0,location)
			main[_D][request.args[_B]][D]=request.user_agent.platform.capitalize();main[_D][request.args[_B]][E]=request.user_agent.browser.capitalize();current_token=request.args[_B];return throwResponce(main[_A][main[_D][request.args[_B]][_C]])
		else:return throwResponce(main[_D])
	else:return throwError(_O)
@app.errorhandler(404)
def page_not_found(e):return'Hi'
app.run()



























<VirtualHost *:80> 95.179.192.71 api.nitlix.pro ServerAdmin nitlixis@gmail.com WSGIScriptAlias / /home/nitlix/site-main//FlaskApp/flaskapp.wsgi <Directory /var/www/FlaskApp/FlaskApp/> Order allow,deny Allow from all </Directory> Alias /static /home//www/FlaskApp/FlaskApp/static <Directory /home/site-main/apps/games/FlaskApp/FlaskApp/static/> Order allow,deny Allow from all </Directory> ErrorLog ${APACHE_LOG_DIR}/error.log LogLevel warn CustomLog ${APACHE_LOG_DIR}/access.log combined </VirtualHost>