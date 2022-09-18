from requests import *

reponse = 'http://Wikipedia.org/'
jsp=get(reponse)
print("url :"+jsp.request.url)
print("method :"+jsp.request.method)
print("headers :"+str(jsp.request.headers))
print("body :"+str(jsp.request.body))
