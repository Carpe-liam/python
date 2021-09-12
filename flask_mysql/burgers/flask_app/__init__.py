from flask import Flask, render_template, session, flash
app= Flask(__name__)
app.secret_key = "wizard"