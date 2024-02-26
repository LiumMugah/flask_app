from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)


@app.route('/')
def root():
  return render_template('root.html')


if __name__ == '__main__':
  app.run(host='0.0.0.0', port=8080)
