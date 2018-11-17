3003 SSAD

	Installation Instructions:
    install Python 3.7.X or above
    pip install django
    pip install django-widget-tweaks
		pip install geopy
		pip install twilio
		pip install python-telegram-bot


	Running Server Instructions:
		open cmd (command prompt)
		navigate to SSAD_3003 directory
			(i.e. cd ../SSAD_3003)
		input command
			python manage.py runserver
		webpage is accessible in browser
			typically http://127.0.0.1:8000/
		to end server, press CTRL + BREAK simultaneously


  Getting TelegramBot and SMS to work
    open ..\SSAD_3003\event\views.py
    uncomment sendSMS() and BotHandler()


  Run Testing
    open cmd (command prompt)
    navigate to SSAD_3003 directory
			(i.e. cd ../SSAD_3003)
    input command
  		python manage.py test --pattern="test_*.py"


	Accounts Present:
		admin
			username: admin
			password: 123456

		users
			username: responder1
			password: 1973qwER
