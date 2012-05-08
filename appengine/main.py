import webapp2
import os

def main():
    application = webapp2.WSGIApplication([('/', MainPage)],
                                         debug=True)


if __name__ == '__main__':
    main()
