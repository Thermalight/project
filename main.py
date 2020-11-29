import invoerscherm
import puntenscherm
screenSize = [1080, 720]
count = 1
state = "start"


def settings():
    if state == "start":
        size(screenSize[0], screenSize[1])

def setup():
    global state
    
    if state == "start":
        invoerscherm.setup()
        
def draw():
    global state
    
    if state == "start":
        invoerscherm.draw()
    elif state == "createGame":
        puntenscherm.setup(invoerscherm.getNames())
        print(invoerscherm.getNames())
        
        #state = "startGame"
    elif state == "startGame":
        puntenscherm.draw()
    
    if not invoerscherm.d.navigationButtons[0].selected:
        invoerscherm.draw()
    else:
        state = "createGame"
    print(state)
def keyTyped():
    for i in range(4):
        invoerscherm.d.textInputs[i].addText(key)