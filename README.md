# Instructions to Run the App
## in order to run this application you need to have a virtual environment
 - Set up a Python virtual environment with the following command: *python3 -m venv .venv*
 - The environment (On Mac) is activated with source *.venv/bin/activate*    
 - The following modules have to be imported using *pip install*
    *flask, pandas, fpdf, smtplib, email.mime.multipart, email.mime.text, email.mime.application*
 - Run the code with following command: *flask run*

## Choosing the language & libraries
Python is chosen to apply this web dev project, for its accessible and beginner-friendly properties. In a similar manner flask is used as the API-of-choice for this project, thanks to its approachability. 
 - fpdf module is used to generate pdf file according to the database
 - email.mime.multipart, email.mime.text, email.mime.application modules are preferred to curate the email in terms of initialize an email object (sender, receiver and title), as well as its textual context and the attachment that is the pdf generated, respectively.
 - smtplib allows to connect a server and send emails accordingly.

## Database
Database is a csv file (transactions.csv) I have curated that with random 2 user emails: abby@gmail.com, cas@gmail.com,cody@gmail.com.
In order to test the program, input email address: abby@gmail.com, start date: 01/11/2023, and end date: 03/11/2023. Transaction history of 2 entries will emerge as a pdf file in the folder of the application.

### Setbacks/Limitations
I have learnt all about web dev, front end and back end, in the span of 1.5 half day, after finishing midterm and quizzes. It was quite enjoyable to dedicate myself to this new endavour and I really loved it!!
However as of this moment, even though I still have the send email function (send_email()) inside app.py, it does not work as google did not allow me to utilize my gmail account due to bad authentication (security limitations) and I was not able to make sending emails work in the given time.
 - Currently, the code downloads the pdf file instead, and that's the end.
 - I'll be working on how to make sending emails work on my side, so if you guys are willing I'm happy to share my progress later on!! 

## Authentication/Authorization
There is Flask-Login extension for managing user authentication in Flask applications. It simplifies the process of handling user sessions, login, and logout functionality. The LoginManager class inside it handles user session and authentications. An instance of LoginManager can be created and flask app must be passed as an arguement using *init_app()*. Using it, each function can be limited to access when the login is in action or the identity of the login, give access to different levels of usability, such as user and moderator, as well as keep the database updated when the same user logs in parallel.

