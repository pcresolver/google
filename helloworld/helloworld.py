# webapp2 is s framework - used to deal with low level tasks.
import webapp2

from google.appengine.api import users
# This is main program and is called when MainPage is called
# Starts with 'get' function to deal with input	

class MainPage(webapp2.RequestHandler):

    def get(self):
        user = users.get_current_user() # If no current user returns none

        if user:
            self.response.headers['Content-Type'] = 'text/plain'
            self.response.write('Hello, ' + user.nickname())
        else:
            self.redirect(users.create_login_url(self.request.uri)) # passes self.request.url so that Google knows where to return user to after logging in


# The following calls an instance of 'Main Page' 
# The '/' says to use mainpage when a call is made to the root url
# Debug = True is to show error reports etc . Turn off when go live.
app = webapp2.WSGIApplication([('/', MainPage)],
                              debug=True)