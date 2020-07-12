# Web.py Tutorial
# By: Caleb Capps and Nick Germaine (Udemy - The Complete Python 3 CourseL Beginner to Advanced!)
# Date: 7/9/2020
#
# Description:
# This program demonstrates the usage of the web package (from part of web.py) as it relates to
# the implementation of HTML code and how it may be integrated with Python logic to create dynamic
# websites using Python.


import web

urls = (
    '/(.*)/(.*)', 'index' # route and name of class, in this case the route is the root of the app
)

myTemplate = web.template.render("Resources/")
app = web.application(urls, globals())

class index:
    def GET(self, name, age):
        return myTemplate.main(name, age)


if __name__ == "__main__":
    app.run()




