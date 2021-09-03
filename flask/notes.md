# Flask
## Virtual Environment

- sandbox style to play in...
- container

---
- assignment 1 -> open terminal here
  - pipfile
  - pipfile.lock
- assignment 2
  - pipfile
  - pipfile.lock


# Guide on how to build a Virtual Environment w/Flask
---
1. open terminal in assignment folder location
2. install Virtual Environment
    ```
    pipenv install pipenv
    ```
---
3. install Flask
    ```
    pipenv install flask
    ```
---
4. open & run Virtual Environment
    ```
    pipenv shell
    ```

---
5. Create file structure --> (MVC)
    - server.py
    - template folder
        - html file
    - static folder
        - styles and such
---

6. Server.py file -> wil change in time
    ```py
    from flask import Flask, render_template, redirect, request, session

    app= Flask(__name__)
    app.secret_key='wizard'

    @app.route('/')
    def home():
        return render_template('index.html')

    @app.route('/return')
    def return_response():
        return render_template('return.html')

    if __name__=="__main__":
        app.run(debug=True)
    ## explination
    '@' = decorator; used in @classmethod @staticmethod
    ```
---
7. start server
    ```
    python <server file name = usually 'server.py'>
    ```
---
## Other Notes: Routes

### Routes
- display route -> render view
- action route - > perform action(s)
    - should never display views!!

### Views
- What is rendered to the page


### Static Files
- Have a specific way of thow they are displayed in html and linked: 
    ```py
    <!-- based on the folder structure on the right -->
    <!-- linking a css style sheet -->
    <link rel="stylesheet" type="text/css" href="{{ url_for('static', filename='my_style.css') }}">
    <!-- linking a javascript file -->
    <script type="text/javascript" src="{{ url_for('static', filename='my_script.js') }}"></script>
    <!-- linking an image -->
    <img src="{{ url_for('static', filename='my_img.png') }}">
    ```

### Methods ?
- funtion inside a class..
- It is the way in which information is passed to the server file.
    - GET
        - info passed through the URL
    - POST
        - using FORMS - to submit methods

## What is a form?
- a way to capture info from the end-user
- 