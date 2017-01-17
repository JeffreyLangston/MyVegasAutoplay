#! python3
#pip install pillow
#pip install pyautogui
#pip install pyperclip
#pip install numpy
#pip install pypiwin32
#pip install selenium
 #pip install C:\pywin32-220.1-cp35-cp35m-win32.whl
#/scripts> python pywin32_postinstall.py -install

import webbrowser
import pyautogui
import time
import pyperclip
import sys
import os
from enum import Enum
import win32gui, win32con
#hack needed to account for dpi 
from ctypes import windll
user32 = windll.user32
user32.SetProcessDPIAware()


class Screen:
	class Files:
		def __init__(self,fileName,clickLocation):
			self.FileName=fileName
			self.ClickLocation=clickLocation
	def __init__(self,name):
		self.Name = name
		self.FileLocations = []

class State:
	def __init__(self,name,clickLocation):
		self.Name = name
		self.ClickLocation=clickLocation

		
class StateTree:
	def __init__(self,item):
		self.item = item
		self.children=[]
		self.parent=None
	
	def pushChild(self, item):
		newItem = StateTree(item)
		self.children.append(newItem)
		newItem.parent = self
		
	def GetBottom(self):
		currentState = self
		while(len(currentState.children) != 0):
			currentState = currentState.children[0]
		return currentState
		
			
			
		
	def pushToBottom(self,item):
		currentState = self
		
		while(len(currentState.children) != 0):
			currentState = currentState.children[0]
			
		currentState.pushChild(item)
		
		
def Main():	
	pyautogui.PAUSE = 0
	pyautogui.FAILSAFE = True
	Frametime = 0
	parentPath = sys.path[0]	
	
	Searching = Screen('Searching')
	Wheel = Screen('Wheel')
	WheelShare = Screen('WheelShare')
	WheelNoShare = Screen('WheelNoShare')
	Ad = Screen('Ad')
	Quest = Screen('Quest')
	Gifts = Screen('Gifts')
	World = Screen('World')
	GameSelection = Screen('GameSelection')
	Game = Screen('Game')
	Deal = Screen('Deal')
	Close = Screen('Close')
	
	
	Folder = '\\Images\\'
		
	#Screens = []
	
	
	
	currentState = StateTree(Searching)
	
	#searching
		#Wheel
			#share
			#acceptAd
				#Ad
						#Ad
							#Quest
								#Games
									#world
		
	Wheel.FileLocations.append(Screen.Files(parentPath + Folder+ 'Wheel3.bmp',(25,550)))
	currentState.pushChild(Wheel)
	
	
	WheelShare.FileLocations.append(Screen.Files(parentPath + Folder+ 'WheelCollectShare.bmp',(30,30)))
	WheelShare.FileLocations.append(Screen.Files(parentPath + Folder+ 'WheelCollectShare.png',(30,30)))
	WheelShare.FileLocations.append(Screen.Files(parentPath + Folder+ 'WheelCollectShare2.bmp',(30,30)))
	WheelShare.FileLocations.append(Screen.Files(parentPath + Folder+ 'WheelCollectShare2.png',(30,30)))
	currentState.pushToBottom(WheelShare)
	
	WheelNoShare.FileLocations.append(Screen.Files(parentPath + Folder+ 'WheelCollectNoShare.bmp',(300,100)))
	WheelNoShare.FileLocations.append(Screen.Files(parentPath + Folder+ 'WheelCollectNoShare2.bmp',(300,100)))
	WheelNoShare.FileLocations.append(Screen.Files(parentPath + Folder+ 'WheelCollectNoShare3.bmp',(300,100)))
	WheelNoShare.FileLocations.append(Screen.Files(parentPath + Folder+ 'WheelCollectNoShare4.bmp',(300,100)))
	WheelNoShare.FileLocations.append(Screen.Files(parentPath + Folder+ 'WheelCollectNoShare.png',(300,100)))
	WheelNoShare.FileLocations.append(Screen.Files(parentPath + Folder+ 'WheelCollectNoShare2.png',(300,100)))
	WheelNoShare.FileLocations.append(Screen.Files(parentPath + Folder+ 'WheelCollectNoShare3.png',(300,100)))
	currentState.pushToBottom(WheelNoShare)
		
	
	#Ad.FileLocations.append(Screen.Files(parentPath + Folder+ 'ad.png',(1020,-1000)))
	#Ad.FileLocations.append(Screen.Files(parentPath + Folder+ 'ad.bmp',(1020,-1000)))
	#Ad.FileLocations.append(Screen.Files(parentPath + Folder+ 'ad2.png',(940,-1000)))
	#Ad.FileLocations.append(Screen.Files(parentPath + Folder+ 'ad2.bmp',(940,-1000)))
	#Ad.FileLocations.append(Screen.Files(parentPath + Folder+ 'ad3.png',(860,-1000)))
	#Ad.FileLocations.append(Screen.Files(parentPath + Folder+ 'ad3.bmp',(860,-1000)))
	#Ad.FileLocations.append(Screen.Files(parentPath + Folder+ 'ad4.png',(860,-1000)))
	#Ad.FileLocations.append(Screen.Files(parentPath + Folder+ 'ad4.bmp',(860,-1000)))
	#Ad.FileLocations.append(Screen.Files(parentPath + Folder+ 'ad5.png',(860,-1000)))
	#Ad.FileLocations.append(Screen.Files(parentPath + Folder+ 'ad5.bmp',(860,-1000)))
	#currentState.pushToBottom(Ad)
	#Screens[Ad.Name].FileLocations.append(Screen.Files(parentPath + Folder+ 'CloseImageSmall.png',(0,0)))
	#Screens[Ad.Name].FileLocations.append(Screen.Files(parentPath + Folder+ 'CloseImageSmall2.png',(0,0)))
	#Screens[Ad.Name].FileLocations.append(Screen.Files(parentPath + Folder+ 'Close.bmp',(0,0)))
	
	
	#Quest.FileLocations.append(Screen.Files(parentPath + Folder+ 'Quest.png',(90,20)))
	#Quest.FileLocations.append(Screen.Files(parentPath + Folder+ 'Quest.bmp',(90,20)))
	#currentState.pushToBottom(Quest)
	
	#Gifts.FileLocations.append(Screen.Files(parentPath + Folder+ 'Gifts.png',(650,-1000)))
	#Gifts.FileLocations.append(Screen.Files(parentPath + Folder+ 'Gifts.bmp',(650,-1000)))
	#currentState.pushToBottom(Gifts)
		
	Close.FileLocations.append(Screen.Files(parentPath + Folder+ 'Close.png',(10,10)))
	Close.FileLocations.append(Screen.Files(parentPath + Folder+ 'Close.bmp',(10,10)))
	currentState.pushToBottom(Close)
	
	closeState = currentState.GetBottom()
	closeState.pushChild(Close)
	World.FileLocations.append(Screen.Files(parentPath + Folder+ 'MapCollect.png',(10,10)))
	World.FileLocations.append(Screen.Files(parentPath + Folder+ 'MapCollect.bmp',(10,10)))
	closeState.pushChild(World)
	
	
	#Deal.FileLocations.append(Screen.Files(parentPath + Folder+ 'Deal1.png',(0,520)))
	#currentState.pushToBottom(Deal)
	#should always be last

	#print(Screens[State.StateName.Wheel].FileLocations)
	#currentState = State('Searching',(0,0))
		
	#print('opening android emulator...')
	#D:\AndriodEmulator\Droid4X\Droid4X.exe


	print('Welcome to MyVegas Autoplay!')
	print('Press Ctrl-C to quit.')
	width, height =pyautogui.size()

	print('Screen: ' + str(width) + ' X ' + str(height))

	url = 'https://apps.facebook.com/playmyvegas'
	ie = webbrowser.get(webbrowser.iexplore)
	ie.open_new(url)


	time.sleep(5)
	hwnd = win32gui.GetForegroundWindow()
	win32gui.ShowWindow(hwnd, win32con.SW_MAXIMIZE)
	from timeit import default_timer as timer
	timeAtLastFrame = timer()		
			
	def isOnScreen(ScreenType):
		for screen in ScreenType.FileLocations:
			onScreen = pyautogui.locateOnScreen(screen.FileName, grayscale=True)
			if onScreen != None:
				clickLocation = (onScreen[0]+screen.ClickLocation[0],onScreen[1]+screen.ClickLocation[1])
				return clickLocation;	
		return None
		
	def DetectStateChange(currentState):
		print(currentState.item.Name)
		TempLocation = None
		print('Detecting Changes...')
		
		for screen in currentState.children:
			print(screen.item.Name)
			TempLocation = isOnScreen(screen.item)
			if TempLocation != None:
				print('Found!')
				print(TempLocation)
				if len(screen.children)>0:
					currentState=screen
				Action(screen, TempLocation)
				return currentState
			else:
				print('Not Found...')
		return currentState

	def Action(currentState, clickLocation):
		if clickLocation == None:
			return
		print('Found!' + currentState.item.Name)

		pyautogui.moveTo(clickLocation[0], clickLocation[1], 1)
		try:
			pyautogui.click()
		except:
			pass
			
		
		return
	try:
		numberOfMissing = 0
		print(currentState)
		while numberOfMissing<20:
			
			timeSinceLastFrame = timer() - timeAtLastFrame
			
			if(timeSinceLastFrame > Frametime):
				#currentState.item.Name = Searching.Name
				#currentState.item.ClickLocation = None
				
				timeAtLastFrame = timer();
				currentState = DetectStateChange(currentState)
				if(currentState.item.Name == Searching.Name):
					pyautogui.screenshot('missing'+str(numberOfMissing)+'.png')
					numberOfMissing = numberOfMissing +1
				#Action(currentState)
				
			
	except KeyboardInterrupt:
		print('\nExiting My Vegas Autoplay...')


Main()




#time.sleep(5)
#pyautogui.position()
#pyautogui.moveTo(100,100, duration=0.25)
#pyautogui.moveRel(200,100, duration=0.25)
#pyautogui.click(100,150,button='left')
#pyautogui.mouseDown()
#pyautogui.mouseUp()
#pyautogui.doubleClick
#pyautogui.dragTo()
#pyautogui.dragRel()
#pyautogui.scroll(200)
#pyperclip.copy(numbers)
#im = pyautogui.screenshot()
#im.getpixel((0,0)) gets color of pixel
#pyautogui.pixelMatchesColor(50, 200, (130, 135, 144))
#pyautogui.locateOnScreen('submit.png')
#pyautogui.typewrite('Hello world!')
#pyautogui.keyDown('shift'); pyautogui.press('4'); pyautogui.keyUp('shift')
#pyautogui.hotkey('alt', '3')


#ie = webbrowser.get(webbrowser.iexplore)
#ie.open('google.com')

#https://apps.facebook.com/playmyvegas
#http://myvegasfreechips.com/

