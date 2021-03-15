#for seven different languages
#sudo pip3 install googletrans
# if error of group class then install 
#pip3 install googletrans==3.1.0a0
import googletrans as gt
#print(gt.LANGUAGES) # all the languages available with their code
trans=gt.Translator()
#change_trans=trans.translate("I am A Lovely coder",dest='es')
#print(change_trans.text)
# for audio and voice command
# google text to speech for different language
#sudo pip3 install gTTS
# for playing audio we can use python playsoun
# sudo pip3 install playsound

# for conversion of recognise class google train the google translated by searching from speech recognizer and add language = variable in google recognize
# 
import gtts
import playsound as ps
import speech_recognition as sr
import pyttsx3 as pt

recognizer=sr.Recognizer()
# speak
language="es"
#spanish change to any you want by finding code of language using 

#def talk(text):
def conv_talk(language):
	try:
		with sr.Microphone() as source:
			print("Speak Now")
			voice=recognizer.listen(source)
			text= recognizer.recognize_google(voice)
			t_es=trans.translate(text,dest=language) # converting text to spanish
			print(t_es.text)
			cva=gtts.gTTS(t_es.text,lang=language) #converting to audio file
			cva.save('convert1.mp3') # saveing audio in mp3 format
			ps.playsound('convert1.mp3') #playing the sound stored in the user

	except:
		pass

conv_talk(language)
