#!/usr/bin/env python3

import sys
import RPi.GPIO as GPIO
from flask import Flask, render_template, request
app = Flask(__name__)

GPIO.setmode(GPIO.BOARD)
GPIO.cleanup()
# Create a dictionary called pins to store the pin number, name, and pin state:
pins = {
   37 : {'name' : 'GPIO 37', 'state' : GPIO.LOW},
   33 : {'name' : 'GPIO 33', 'state' : GPIO.LOW}
   }

# Set each pin as an output and make it low:
for pin in pins:
   GPIO.setup(pin, GPIO.OUT)
   GPIO.output(pin, GPIO.LOW)

@app.route("/")
def main():
   # For each pin, read the pin state and store it in the pins dictionary:
   for pin in pins:
      pins[pin]['state'] = GPIO.input(pin)
   # Put the pin dictionary into the template data dictionary:
   templateData = {
      'pins' : pins
      }
   # Pass the template data into the template main.html and return it to the user
   return render_template('main.html', **templateData)

# The function below is executed when someone requests a URL with the pin number and action in it:
@app.route("/<changePin>/<action>")
def action(changePin, action):

   changePin = int(changePin)

   deviceName = pins[changePin]['name']

   if action == "on":

      GPIO.output(changePin, GPIO.HIGH)

      message = "Turned " + deviceName + " on."
   if action == "off":
      GPIO.output(changePin, GPIO.LOW)
      message = "Turned " + deviceName + " off."

   for pin in pins:
      pins[pin]['state'] = GPIO.input(pin)

   templateData = {
      'pins' : pins
   }

   return render_template('main.html', **templateData)

if __name__ == '__main__':
    try:
        app.run(host='0.0.0.0', port=80, debug=True)
    except KeyboardInterrupt:
        GPIO.cleanup()
        sys.exit(1)
    except Exception as e:
        print('Exited with error: {}'.format(e))
        GPIO.cleanup()
        sys.exit(1)