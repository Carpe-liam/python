# Flask
## Virtual Env

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
    from flask import Flask, render template  # Import Flask to allow us to create our app
    app = Flask(__name__)    # Create a new instance of the Flask class called "app"
    @app.route('/')          # The "@" decorator associates this route with the function immediately following
    def hello_world():
        return 'Hello World!'  # Return the string 'Hello World!' as a response
    if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
        app.run(debug=True)    # Run the app in debug mode.
    

    ## explination
    '@' = decorator; used in @classmethod @staticmethod
    ```
---
7. start server
    ```
    python <server file name = usually 'server.py'>
    ```

8. Routes
    - display route -> render view
    - action route - > perform action(s)
        - should never display views!!

9. Views
    - What is rendered to the page
    - 