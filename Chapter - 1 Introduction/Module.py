# code written by other we just use them for saving our time, beacuse if you start writing manually it will take plenty time
import pyttsx3
import pyjokes
joke = pyjokes.get_joke()
print(joke)


engine = pyttsx3.init()
engine.say("i will speak this text")
engine.runAndWait()


# this is single line comment
'''
this is multiline commment
'''
"""this is also multiline comment and docstring"""
# print multiline by using tipple single qoute or tripple double qoute