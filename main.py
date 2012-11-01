#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import webapp2

userlist = {};
lurkers = {};
def adduser(username,ip):
  if (username == "$block[username]"):
   return
  if (username == "Guest"):
    lurkers[ip] = 1
  userlist[username] = 1

def getuserlist():

  counter = 0
  guests = len(lurkers)
  
  html = "<html><body><b>" + str(len(userlist) + guests) + " Recent Visitors: </b>"
  html += "Lurker (" + str(guests) + ") "
  for key, value in userlist.iteritems():
    if(key == "Guest"):
     continue
    html += key + " "  
  html += "</body></html>"  
  return html

class MainHandler(webapp2.RequestHandler):
    def get(self):
        curuser = self.request.get('u')
        ip = self.request.remote_addr
        adduser(curuser,ip)
        outfile = getuserlist()
        self.response.out.write(outfile)

app = webapp2.WSGIApplication([('/', MainHandler)],
                              debug=True)
