# Mindful Homework WebApp
Mindful is a webapp that is designed to help students schedule their time better for homework. Our approach streamlines the homework session experience. 

We use the Canvas API to pull a students assignments and present them in a minimal, distraction-free interface.

Our goal is to help students be more mindful about how they do their homework. To facilitate this goal we built a dedicated mindfulness page to help them relax and take meaningful study breaks.


## Getting Started
1. Download Required Software
2. Create virtual environment named "env". [Tutorial](https://docs.python.org/3/library/venv.html)
3. Create accessToken.json file inside ```hw_session/static```
   1. Contents: ```{"token" : "Your token here", "user_id" : "Your ID here"}```
4. Create Canvas API token.
   1. In Canvas navigate to: Account --> Settings --> Approved Integrations --> New Access Token --> Follow Steps to Create Token
   2. Paste the Token into the JSON file from step 3.
5. Copy unique User ID from Canvas.
   1. Navigate to any currently enrolled course --> People --> Click on your Own Name --> Copy last six digit number of the url after the last "/".
   2. Paste User ID into JSON file from step 3.
6. run server with ```python manage.py runserver```


### Development Environment
- Python (v3.9+) [Download Python](https://www.python.org/downloads/)
- Django-admin (v3.2.8) ```pip install django-admin```
- Django (v3.2.8) ```pip install django```
- Canvasapi (v2.2.0) ```pip install canvasapi```
- Plotly (v5.4.0) ```pip install plotly```

## Our Team
### Contributors
- Reece Poulsen [LinkedIn](https://www.linkedin.com/in/reece-poulsen), [GitHub](https://github.com/Reecepoulsen)
- Joshua Staples [LinkedIn](https://www.linkedin.com/in/joshua-s-81100986/), [GitHub](https://github.com/joshua-staples)
- Christian Martinez [LinkedIn](www.linkedin.com/in/christian-martinez-28868a222), [GitHub](https://github.com/FinestTurtle)
- Bryton Peterson [LinkedIn](https://www.linkedin.com/in/bryton-petersen-a44b32223/), [GitHub](https://github.com/BrytonPetersen)
### Contact
- Message us on LinkedIn

## Future Plans
- Custom Assignments
- Dynamic Mindfulness Page
- Login/Authentication with Canvas
- Cloud database in place of SQLite
- Local storage for assignment

## Useful Websites
- [Django Documentation](https://docs.djangoproject.com/en/4.0/)
- [Canvas Rest API Documentation](https://canvas.instructure.com/doc/api/courses.html)
- [Canvas Documentation](https://canvasapi.readthedocs.io/en/stable/course-ref.html)
