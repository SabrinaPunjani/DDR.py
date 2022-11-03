#Sabrina Punjani

add_library('minim')
screen = 0
great = 0
tostart = 0
topimg = 0
leftpr=0
rightpr=0
uppr=0
stepchartCM = 0
congrat = 0
playerC = 0
downpr = 0
topleft = 0
topdown = 0
topup = 0
topright = 0
lefton = 0
downon = False
upon = False
righton = False
stepchart = 0
bpmXE = 170
bpmCE = 165
y = 0
x = 0
left = 0 # you must create global
up = 0
down = 0
right = 0
top = 0
score= 0
bg = 0
stepchartCE= 0

bpm = 550.0#170.0
mpb = ( 60 / bpm  * 1000) # millis per beat
#print mpb

bg1 = 0
pika1=0
pika2=0
pika3=0
pika4=0
jump=0
#score ranking
name1 = "0"
name2 = 0
name3 = 0
score1 = 0
score2 = 0
score3 = 0
song1 = "0"
song2 = "0"
song3 = "0"
leaderboardscr = 0
highscore = 0
goback = 0
pokemonwall = 0
themeoriginal = True
themepokemon = False
pokemonlogo = 0
themewall = 0
themesetup = 0
original = 0
gamestart = 0
gamestart1 =0
instructions = 0
instructions1 = 0
theme = 0
theme1 = 0
leaderboard = 0
leaderboard1 = 0
mode = 10
dance = 0
cdbg = 0
dance1 = 0
logo = 0
name = 0
menuselection = 0
gamewall = 0
xepher = 0
xepher1 = 0
songsel = 0
songmode = 50
cd = 0
cd1 = 0
howtosong = 0
level = 0
level1 = 0
level2 = 0
level3 = 0
levelsel = 0
levelmode = 50
stepchart = 0
y = 0
x = 0
left = 0 # you must create global
up = 0
down = 0
right = 0
top = 0
score= 0
Xbg = 0
player3 = 0
player4 = 0
themesel = 0
themehow = 0
ipic = 0
bpm = 550.0
mpb =( 60 / bpm  * 1000) 

def setup():
    size(900,700)
    background(255,255,255)
    frameRate(200)
    global stepchartCM,ipic,congrat,stepchartCE,bpmCE,cdbg,playerC,tostart,bpmXE,stepchartXE,player4, minim,left, top, right, up, down, stepchartXH,Xbg, topup, topdown,topleft,topright, great, screen,highscore,leaderboardscr,goback,pika1,pika2,pika3,pika4,player3,minim,themepokemon,pokemonwall,themehow,original,pokemonlogo,themesetup,themewall,minum,levelsel,levelmode,level,level1,level2,level3,howtolevel,howtosong,cd,cd1,butterfly,butterfly1,songsel,xepher1,xepher,gamewall,name,minum,player,player3, gamestart, gamestart1, logo, menuselection, instructions, instructions1, theme, theme1,bg, leaderboard, leaderboard1, dance1, dance2, dance3, dance4, dance5, dance6, dance7,player1,left, top, right, up, down, stepchart,bg1
    
    #-------------------LOADING MUSIC-------------------------------------------------------------------------------------------------------
    minim = Minim(this)
    player = minim.loadFile("xepher.mp3")
    minum = Minim(this) 
    player3 = minim.loadFile("pokemon.mp3")
    playerC = minum.loadFile("Caramelldancing.mp3")
    #-------------------LOADING STEPCHART------------------------------------------------------------------------------------------------------
    stepchartCM = [0,0,0,1]#too big
    stepchartCE = [[0,0,0,0],
[0,0,0,0],
[0,0,0,0],
[0,0,0,0],

[0,0,0,0],
[0,0,0,0],
[0,0,0,0],
[0,0,0,0],

[0,0,0,0],
[0,0,0,0],
[0,0,0,0],
[0,0,0,0],

[0,0,0,0],
[0,0,0,0],
[0,0,0,0],
[0,0,0,0],

[1,0,0,0],
[0,0,0,0],
[0,0,0,1],
[0,0,1,0],

[0,0,0,1],
[0,0,0,0],
[1,0,0,0],
[0,1,0,0],

[1,0,0,0],
[0,0,0,0],
[0,0,1,0],
[0,1,0,0],

[0,0,1,0],
[0,0,0,0],
[0,0,1,0],
[0,0,0,0],

[0,1,0,0],
[0,0,0,0],
[0,1,0,0],
[0,0,0,0],

[0,1,0,0],
[0,0,0,1],
[0,1,0,0],
[0,0,0,0],

[1,0,0,0],
[0,0,0,0],
[1,0,0,0],
[0,0,0,0],

[1,0,0,0],
[0,0,1,0],
[1,0,0,0],
[0,0,0,0],

[0,1,0,0],
[0,0,0,0],
[0,1,0,0],
[0,0,0,0],

[0,1,0,0],
[0,0,1,0],
[0,1,0,0],
[0,0,0,0],

[0,0,1,0],
[0,0,0,0],
[0,0,1,0],
[0,0,0,0],

[0,0,0,1],
[0,0,1,0],
[0,1,0,0],
[1,0,0,0],

[0,0,0,1],
[0,0,0,0],
[0,0,0,1],
[0,0,0,0],

[1,0,0,1],
[0,0,0,0],
[1,0,0,1],
[0,0,0,0],

[1,0,0,0],
[0,1,0,0],
[1,0,0,0],
[0,0,0,0],

[1,0,0,1],
[0,0,0,0],
[1,0,0,1],
[0,0,0,0],

[0,0,1,0],
[0,0,0,0],
[0,0,0,0],
[0,0,0,0],

[0,1,0,0],
[0,0,0,0],
[0,1,0,0],
[0,0,1,0],

[0,1,0,0],
[0,0,0,0],
[0,0,0,0],
[0,0,0,0],

[1,0,0,0],
[0,0,0,1],
[1,0,0,0],
[0,0,0,0],

[1,0,0,0],
[0,1,0,0],
[1,0,0,0],
[0,0,0,0],

[0,1,0,0],
[0,0,1,0],
[0,0,0,1],
[0,0,0,0],

[1,0,0,0],
[0,0,0,1],
[1,0,0,0],
[0,0,0,0],

[0,0,0,1],
[0,0,1,0],
[0,1,0,0],
[0,0,0,0],

[0,0,1,0],
[0,0,1,0],
[0,0,1,0],
[0,0,0,0],

[0,0,0,1],
[0,1,0,0],
[0,0,0,1],
[0,0,0,0],

[0,1,0,0],
[0,0,1,0],
[1,0,0,0],
[0,0,0,0],

[0,1,0,0],
[0,1,0,0],
[0,1,0,0],
[0,1,0,0],

[1,0,0,1],
[0,0,0,0],
[1,0,0,1],
[0,0,0,0],

[0,1,0,0],
[0,0,0,0],
[0,0,0,0],
[0,0,0,0],

[0,1,1,0],
[0,0,0,0],
[0,1,1,0],
[0,0,0,0],

[0,0,0,1],
[0,0,0,0],
[0,0,0,0],
[0,0,0,0],

[1,0,0,1],
[0,0,0,0],
[1,0,0,1],
[0,1,0,0],

[0,0,1,0],
[0,0,0,0],
[0,0,1,0],
[0,0,0,0],

[0,1,1,0],
[0,0,0,0],
[0,1,1,0],
[0,0,0,0],

[1,0,0,0],
[0,0,0,0],
[1,0,0,0],
[0,0,0,0],

[0,0,0,1],
[0,0,0,0],
[0,0,0,1],
[0,0,0,0],

[0,0,0,1],
[1,0,0,0],
[0,0,0,1],
[0,0,0,0],

[1,0,0,0],
[0,0,0,0],
[1,0,0,0],
[0,0,0,0],

[1,0,0,0],
[0,0,1,0],
[1,0,0,0],
[0,0,0,0],

[0,1,0,0],
[0,0,0,0],
[0,1,0,0],
[0,0,0,0],

[0,0,1,0],
[0,0,1,0],
[0,0,0,1],
[0,0,0,0],

[0,0,1,0],
[0,0,0,0],
[0,0,1,0],
[0,0,0,0],

[0,1,0,0],
[0,1,0,0],
[1,0,0,0],
[0,0,0,0],

[1,0,0,0],
[0,1,0,0],
[1,0,0,0],
[0,0,0,0],

[0,0,0,1],
[0,1,0,0],
[0,0,0,1],
[0,0,0,0],

[0,0,1,0],
[0,0,0,1],
[0,0,1,0],
[0,0,0,0],

[1,0,0,0],
[0,1,0,0],
[1,0,0,0],
[0,0,0,0],

[1,0,0,0],
[0,0,0,1],
[1,0,0,0],
[0,0,0,0],

[1,0,0,0],
[0,1,0,0],
[0,0,0,0],
[0,0,0,0],


[0,0,0,0],
[0,0,0,0],
[1,0,0,0],
[0,1,0,0],

[1,0,0,0],
[0,1,0,0],
[0,0,0,0],
[0,0,0,0],

[0,0,1,0],
[0,0,1,0],
[0,0,0,1],
[0,0,0,0],

[1,0,0,0],
[0,0,0,1],
[1,0,0,0],
[0,0,0,0],

[0,1,0,0],
[1,0,0,0],
[0,0,1,0],
[0,0,0,0],

[0,1,0,0],
[1,0,0,0],
[0,0,1,0],
[0,0,0,0],

[0,0,1,0],
[0,0,1,0],
[0,0,0,1],
[0,0,0,0],

[1,0,0,0],
[1,0,0,0],
[0,1,0,0],
[0,0,0,0],

[1,0,0,0],
[0,1,0,0],
[0,0,1,0],
[0,0,0,0],

[0,0,0,1],
[1,0,0,0],
[0,0,0,1],
[1,0,0,0],

[1,0,0,1],
[0,0,1,0],
[0,0,0,0],
[0,0,1,0],

[0,0,0,0],
[0,0,1,0],
[0,0,0,0],
[0,0,1,0],

[0,0,0,0],
[0,0,1,0],
[0,0,0,0],
[0,0,1,0],

[0,0,0,0],
[0,0,1,0],
[0,0,0,0],
[0,0,1,0],

[1,0,0,1],
[0,0,0,0],
[0,0,0,0],
[0,0,0,0],

[1,0,0,0],
[0,0,0,0],
[1,0,0,0],
[0,0,0,0],

[0,1,0,0],
[0,0,0,0],
[0,0,0,0],
[0,0,0,0],

[0,0,0,1],
[0,0,0,0],
[0,0,0,1],
[0,0,0,0],

[1,0,0,1],
[0,0,0,0],
[0,0,0,0],
[0,0,0,0],

[1,0,0,1],
[0,0,0,0],
[0,0,0,0],
[0,0,0,0],

[0,0,1,0],
[0,0,1,0],
[0,0,1,0],
[0,0,0,0],

[0,0,0,1],
[0,1,0,0],
[0,0,0,1],
[0,0,0,0],

[1,0,0,0],
[1,0,0,0],
[1,0,0,0],
[0,0,0,0],

[0,0,1,0],
[1,0,0,0],
[0,0,1,0],
[0,0,0,0],

[0,1,0,0],
[0,1,0,0],
[0,1,0,0],
[0,0,0,0],

[0,0,1,0],
[0,0,0,1],
[1,0,0,0],
[0,0,0,0],

[0,0,1,0],
[0,0,1,0],
[0,0,1,0],
[0,0,0,0],

[0,1,0,0],
[1,0,0,0],
[0,0,0,1],
[1,0,0,0],

[0,0,0,1],
[0,0,0,0],
[0,0,0,1],
[0,0,0,0]]
    
    stepchartXE =[[0,0,0,0],
[0,0,0,0],
[0,0,0,0],
[0,0,0,0],

[0,0,0,0],
[0,0,0,0],
[0,0,0,0],
[0,0,0,0],

[0,0,0,0],
[0,0,0,0],
[0,0,0,0],
[0,0,0,0],

[0,0,0,0],
[0,0,0,0],
[0,0,0,0],
[0,0,0,0],

[0,0,0,0],
[0,0,0,0],
[0,0,0,0],
[0,0,0,0],

[0,0,0,0],
[0,0,0,0],
[0,0,0,0],
[0,0,0,0],

[1,0,0,0],
[0,0,0,0],
[0,0,0,0],
[1,0,0,1],

[0,0,0,0],
[0,0,0,0],
[0,0,0,0],
[0,1,1,0],

[0,0,0,0],
[0,0,0,0],
[0,0,0,0],
[1,0,0,0],

[0,0,0,0],
[0,1,0,0],
[0,0,0,0],
[0,0,1,0],

[0,0,0,0],
[0,0,0,0],
[0,0,0,0],
[0,0,0,1],

[0,0,0,0],
[0,0,0,0],
[0,0,0,0],
[0,1,1,0],

[0,0,0,0],
[0,0,0,0],
[0,0,0,0],
[0,0,1,0],

[0,0,0,0],
[0,0,1,0],
[0,0,0,0],
[0,1,0,0],

[0,0,0,0],
[0,1,1,0],
[0,0,0,0],
[0,1,0,0],

[0,0,0,0],
[1,0,0,0],
[0,0,0,0],
[0,0,1,0],

[0,0,0,0],
[0,0,0,1],
[0,0,0,0],
[1,0,0,0],

[0,0,0,0],
[0,1,0,0],
[0,0,0,0],
[0,1,0,0],

[0,1,0,0],
[0,0,0,0],
[0,0,0,1],
[0,0,0,0],

[1,0,0,0],
[0,0,0,0],
[0,0,0,1],
[0,0,0,0],

[0,0,0,1],
[0,0,0,0],
[0,0,0,1],
[0,0,0,0],

[0,0,1,0],
[0,0,0,0],
[0,0,0,1],
[0,0,0,0],

[0,0,1,0],
[0,0,0,0],
[0,0,1,0],
[0,0,0,0],

[1,0,0,0],
[0,0,0,0],
[0,0,1,0],
[0,0,0,0],

[0,0,0,1],
[0,0,0,0],
[0,0,0,0],
[0,0,0,0],

[0,0,1,0],
[0,0,0,0],
[0,1,0,0],
[0,0,0,0],

[1,0,0,0],
[0,0,0,0],
[0,1,0,0],
[0,0,0,0],

[0,0,1,0],
[0,0,0,0],
[0,0,1,0],
[0,0,0,0],

[1,0,0,0],
[0,0,0,0],
[0,0,1,0],
[0,0,0,0],

[0,0,1,0],
[0,0,0,0],
[0,1,0,0],
[0,0,0,0],

[1,0,0,0],
[0,0,0,0],
[1,0,0,0],
[0,0,0,0],

[0,0,0,1],
[0,0,0,0],
[0,0,1,0],
[0,0,0,0],

[0,1,0,0],
[0,0,0,0],
[0,1,0,0],
[0,0,0,0],

[1,0,0,0],
[0,0,0,0],
[0,0,1,0],
[0,0,0,0],

[1,0,0,0],
[0,0,0,0],
[0,1,0,0],
[0,0,0,0],

[0,1,0,0],
[0,0,0,0],
[0,0,0,0],
[1,0,0,0],

[0,0,0,0],
[0,0,0,0],
[0,0,0,0],
[0,1,0,0],

[0,0,0,0],
[0,0,0,0],
[0,0,0,0],
[0,0,1,0],

[0,0,0,0],
[0,1,0,0],
[0,0,0,0],
[0,0,1,0],

[0,0,0,0],
[0,0,0,0],
[0,0,0,0],
[0,1,0,0],

[0,0,0,0],
[0,0,0,0],
[0,0,0,0],
[1,0,0,1],

[0,0,0,0],
[0,0,0,0],
[0,0,0,0],
[0,1,1,0],

[0,0,0,0],
[0,0,1,0],
[0,0,0,0],
[0,1,0,0],

[0,0,0,0],
[0,0,0,0],
[0,0,1,0],
[0,0,0,0],

[0,1,0,0],
[0,0,0,0],
[1,0,0,0],
[0,0,0,0],

[0,0,0,1],
[0,0,0,0],
[0,1,0,0],
[0,0,0,0],

[0,0,1,0],
[0,0,0,0],
[1,0,0,0],
[0,0,0,0],

[0,0,0,1],
[0,0,0,0],
[1,0,0,0],
[0,0,0,0],

[0,0,0,1],
[0,0,0,0],
[0,0,1,0],
[0,0,0,0],

[0,0,0,1],
[0,0,0,0],
[0,1,0,0],
[0,0,0,0],

[0,1,0,0],
[0,0,0,0],
[0,0,1,0],
[0,0,0,0],

[1,0,0,0],
[0,0,0,0],
[1,0,0,0],
[0,0,0,0],

[0,0,0,1],
[0,0,0,0],
[0,1,0,0],
[0,0,0,0],

[1,0,0,0],
[0,0,0,0],
[0,1,0,0],
[0,0,0,0],

[1,0,0,0],
[0,0,0,0],
[0,0,1,0],
[0,0,0,0],

[0,1,0,0],
[0,0,0,0],
[0,1,0,0],
[0,1,0,0],

[0,0,0,0],
[0,0,1,0],
[0,0,0,0],
[0,0,0,1],

[0,0,0,0],
[0,0,0,1],
[0,0,0,0],
[0,0,1,0],

[0,0,0,0],
[0,0,1,0],
[0,0,0,0],
[0,1,0,0],

[0,0,0,0],
[0,0,1,0],
[0,0,0,0],
[0,0,0,1],

[0,0,0,0],
[1,0,0,1],
[0,0,0,0],
[0,0,0,1],

[0,0,0,0],
[0,1,0,0],
[0,1,0,0],
[0,0,0,0],

[0,0,0,1],
[0,0,0,0],
[1,0,0,0],
[0,0,0,0],

[0,0,1,0],
[0,0,0,0],
[0,0,0,0],
[0,1,0,0],

[0,0,0,0],
[0,0,0,0],
[0,0,0,0],
[0,1,0,0],

[0,0,0,0],
[0,0,0,0],
[0,0,0,0],
[0,0,1,0],

[0,0,0,0],
[0,0,0,0],
[0,0,0,0],
[0,0,1,0],
[0,0,0,0],
[0,0,0,0],
[0,0,0,0],
[1,0,0,0],

[0,0,0,0],
[0,0,0,0],
[0,0,0,0],
[0,0,0,0],

[0,1,1,0],
[0,0,0,0],
[0,0,0,0],
[0,0,0,0],

[1,0,0,1],
[0,0,0,0],
[0,0,0,0],
[0,0,0,0],

[0,0,0,0],
[0,0,0,0],
[0,0,0,0],
[0,0,0,0]]
    
    stepchartXH = [[0,0,0,0],

[0,0,0,0],
[0,0,0,0],
[0,0,0,0],
[0,0,0,0],
[0,0,0,0],
[0,0,0,0],
[0,0,0,0],
[0,0,0,0],
[0,0,0,0],
[0,0,0,0],
[0,0,0,0],
[0,0,0,0],

[0,0,0,0],
[0,0,0,0],
[0,0,0,0],
[0,0,0,0],

[0,0,0,0],
[0,0,0,0],
[0,0,0,0],
[0,0,0,0],

[0,0,0,0],
[0,0,0,0],
[0,0,0,0],
[0,0,0,0],

[0,0,0,0],
[0,0,0,0],
[0,0,0,0],
[0,0,0,0],
[0,0,0,0],
[0,0,0,0],
[0,0,0,0],
[0,0,0,0],
    [0,0,0,0],#here
[0,0,0,0],
[0,0,0,0],
[0,0,0,0],

[0,0,0,0],
[0,0,0,0],
[0,0,0,0],
[0,0,0,0],

[0,0,0,0],
[0,0,0,0],
[0,0,0,0],
[0,0,0,0],

[0,0,0,0],
[0,0,0,0],
[0,0,0,0],
[0,0,0,0],

[0,0,0,0],
[0,0,0,0],
[0,0,0,0],
[0,0,0,0],
[0,0,0,0],
[0,0,0,0],
[0,0,0,0],
[0,0,0,0],

[1,0,0,0],
[0,0,0,0],
[0,0,0,0],
[0,1,0,0],
[0,0,0,0],
[0,0,0,0],
[0,0,1,0],
[0,0,0,0],
[0,0,0,0],
[0,0,0,1],
[0,0,0,0],
[0,0,0,0],
[1,1,0,0],
[0,0,0,0],
[0,0,0,0],
[0,0,0,0],

[0,0,0,1],
[0,0,0,0],
[0,0,0,0],
[0,1,0,0],
[0,0,0,0],
[0,0,0,0],
[0,0,1,0],
[0,0,0,0],
[0,0,0,0],
[1,0,0,0],
[0,0,0,0],
[0,0,0,0],
[0,1,0,1],
[0,0,0,0],
[1,0,0,0],
[0,0,0,0],

[0,1,0,0],
[0,0,0,0],
[0,0,0,0],
[1,0,0,0],
[0,0,0,0],
[0,0,0,0],
[0,0,1,0],
[0,0,0,0],
[0,0,0,0],
[1,0,0,0],
[0,0,0,0],
[0,0,0,0],
[0,1,1,0],
[0,0,0,0],
[0,0,0,0],
[0,0,0,0],

[0,0,1,0],
[0,1,0,0],
[0,0,0,1],
[0,1,0,0],
[1,0,0,0],
[0,0,0,1],
[0,1,0,0],
[0,0,1,0],

[1,0,0,0],
[0,0,0,0],
[0,0,0,0],
[0,0,1,0],
[0,0,0,0],
[0,0,0,0],
[1,0,0,0],
[0,0,0,0],
[0,0,0,0],
[0,1,0,0],
[0,0,0,0],
[0,0,0,0],
[0,0,1,1],
[0,0,0,0],
[0,0,0,0],
[0,0,0,0],

[0,1,0,0],
[0,0,0,0],
[0,0,0,0],
[0,0,1,0],
[0,0,0,0],
[0,0,0,0],
[1,0,0,0],
[0,0,0,0],
[0,0,0,0],
[0,0,0,1],
[0,0,0,0],
[0,0,0,0],
[0,0,1,1],
[0,0,0,0],
[1,0,0,0],
[0,0,0,0],

[0,1,0,0],
[0,0,0,0],
[0,0,0,0],
[0,0,0,1],
[0,0,0,0],
[0,0,0,0],
[0,0,1,0],
[0,0,0,0],
[0,0,0,0],
[0,0,0,1],
[0,0,0,0],
[0,0,0,0],
[1,0,0,1],
[0,0,0,0],
[0,0,0,0],
[0,0,0,0],

[1,0,0,0],
[0,0,1,0],
[1,0,0,0],
[0,1,0,0],
[0,0,1,0],
[0,0,0,1],
[0,1,0,0],
[0,0,0,0],

[1,0,1,0],
[0,0,0,0],
[0,1,0,1],
[0,0,0,0],
[0,0,1,0],
[0,1,0,0],
[1,0,0,0],
[0,0,1,0],

[0,1,0,0],
[0,0,1,0],
[1,0,0,0],
[0,1,0,0],
[0,0,1,0],
[0,1,0,0],
[1,0,0,0],
[0,0,1,0],

[0,1,0,1],
[0,0,0,0],
[0,1,1,0],
[0,0,0,0],
[0,0,1,0],
[0,1,0,0],
[0,0,0,1],
[1,0,0,0],

[0,1,0,0],
[0,0,1,0],
[0,0,0,1],
[0,1,0,0],
[1,0,0,0],
[0,1,0,0],
[0,0,0,1],
[0,0,0,0],

[1,1,0,0],
[0,0,0,0],
[0,1,0,1],
[0,0,0,0],
[0,0,1,0],
[0,1,0,0],
[0,0,0,1],
[0,0,1,0],

[1,1,0,0],
[0,0,0,0],
[0,1,0,1],
[0,0,0,0],
[1,0,0,0],
[0,0,0,1],
[0,1,0,0],
[0,0,0,1],

[0,0,1,0],
[0,1,0,0],
[1,0,0,0],
[0,0,0,1],
[0,0,1,0],
[0,0,0,1],
[0,1,0,0],
[0,0,1,0],

[0,1,0,0],
[0,0,0,1],
[0,0,1,0],
[0,1,0,0],
[0,0,0,1],
[0,1,0,0],
[1,0,0,0],
[0,0,0,0],

[0,0,1,0],
[0,0,0,1],
[1,0,0,0],
[0,1,0,0],
[0,0,0,1],
[1,0,0,0],
[0,1,0,0],
[0,0,1,0],

[0,0,0,1],
[0,1,0,0],
[0,0,0,1],
[0,0,1,0],
[1,0,0,0],
[0,0,0,1],
[0,1,0,0],
[1,0,0,0],

[0,0,0,1],
[0,0,0,0],
[0,0,0,0],
[1,0,0,1],

[0,0,1,0],
[0,1,0,0],
[1,0,0,0],
[0,0,0,1],
[0,1,0,0],
[0,0,0,1],
[0,0,1,0],
[0,1,0,0],

[1,0,0,0],
[0,0,1,0],
[0,1,0,0],
[0,0,0,1],
[1,0,0,0],
[0,1,0,0],
[0,0,0,1],
[0,1,0,0],

[1,0,0,0],
[0,0,1,0],
[0,1,0,1],
[0,0,0,0],
[0,0,0,1],
[0,0,1,0],
[1,1,0,0],
[0,0,0,0],

[1,0,0,0],
[1,0,0,0],
[0,0,0,1],
[0,1,0,0],
[0,0,1,0],
[0,1,0,0],
[0,0,0,1],
[0,0,1,0],

[0,1,0,0],
[0,1,0,0],
[0,0,0,1],
[0,1,0,0],
[1,0,0,0],
[0,0,1,0],
[1,0,0,0],
[0,1,0,0],

[0,0,1,0],
[0,0,1,0],
[0,0,0,1],
[1,0,0,0],
[0,0,1,0],
[0,1,0,0],
[0,0,0,1],
[0,0,1,0],

[0,0,0,1],
[1,0,0,0],
[0,1,0,0],
[1,0,0,0],
[1,0,0,0],
[0,0,0,1],
[0,1,0,0],
[0,0,0,1],

[0,0,1,0],
[0,1,0,0],
[1,0,0,0],
[0,0,1,0],
[0,0,1,0],
[0,1,0,0],
[0,0,0,1],
[1,0,0,0],

[0,1,0,0],
[1,0,0,0],
[1,0,0,0],
[1,0,0,0],
[1,0,0,0],
[1,0,0,0],
[1,1,0,0],
[0,0,0,1],

[0,1,0,0],
[0,0,0,1],
[0,0,0,1],
[0,0,0,1],
[0,0,0,1],
[0,0,0,1],
[0,1,0,1],
[0,0,0,0],

[0,0,1,0],
[0,0,0,0],
[0,0,0,0],
[1,0,0,0],
[0,0,0,0],
[0,0,0,0],
[0,1,0,0],
[0,0,0,0],
[0,0,0,0],
[0,0,1,0],
[0,0,0,0],
[0,0,0,0],
[1,0,0,1],
[0,0,0,0],
[0,0,0,0],
[0,0,0,0],

[0,0,0,1],
[0,0,0,0],
[0,0,0,0],
[0,0,1,0],
[0,0,0,0],
[0,0,0,0],
[1,0,0,0],
[0,0,0,0],
[0,0,0,0],
[0,0,1,0],
[0,0,0,0],
[0,0,0,0],
[0,1,0,1],
[0,0,0,0],
[1,0,0,0],
[0,0,0,0],

[0,0,0,1],
[0,0,0,0],
[0,0,0,0],
[0,1,0,0],
[0,0,0,0],
[0,0,0,0],
[0,0,1,0],
[0,0,0,0],
[0,0,0,0],
[1,0,0,0],
[0,0,0,0],
[0,0,0,0],
[0,1,1,0],
[0,0,0,0],
[0,0,0,0],
[0,0,0,0],

[0,0,1,0],
[0,0,0,1],
[0,1,0,0],
[0,0,0,1],
[1,0,0,0],
[0,1,0,0],
[0,0,1,0],
[0,1,0,0],

[1,0,0,0],
[0,0,0,0],
[0,0,0,0],
[0,1,0,0],
[0,0,0,0],
[0,0,0,0],
[0,0,1,0],
[0,0,0,0],
[0,0,0,0],
[0,0,0,1],
[0,0,0,0],
[0,0,0,0],
[1,1,0,0],
[0,0,0,0],
[0,0,0,0],
[0,0,0,0],

[0,0,0,1],
[0,0,0,0],
[0,0,0,0],
[1,0,0,0],
[0,0,0,0],
[0,0,0,0],
[0,1,0,0],
[0,0,0,0],
[0,0,0,0],
[0,0,1,0],
[0,0,0,0],
[0,0,0,0],
[0,1,0,1],
[0,0,0,0],
[1,0,0,0],
[0,0,0,0],

[0,0,1,0],
[0,0,0,0],
[0,0,0,0],
[0,1,0,0],
[0,0,0,0],
[0,0,0,0],
[0,0,0,1],
[0,0,0,0],
[0,0,0,0],
[1,0,0,0],
[0,0,0,0],
[0,0,0,0],
[0,1,1,0],
[0,0,0,0],
[0,0,0,0],
[0,0,0,0],

[0,0,0,1],
[0,0,1,0],
[0,1,0,0],
[1,0,0,0],
[0,0,0,1],
[1,0,0,0],
[0,0,1,0],
[0,1,0,0],

[0,0,0,1],
[0,1,0,0],
[0,0,0,1],
[0,0,0,0],
[1,0,0,1],
[0,1,0,0],
[1,0,0,0],
[0,0,0,0],

[1,0,1,0],
[0,1,0,0],
[0,0,1,0],
[0,0,0,0],
[1,0,1,0],
[0,0,0,1],
[1,0,0,0],
[0,0,0,0],

[1,0,0,1],
[0,0,1,0],
[0,0,0,1],
[0,0,0,0],
[0,1,0,1],
[0,0,1,0],
[0,1,0,0],
[0,0,0,0],

[0,1,1,0],
[1,0,0,0],
[0,0,1,0],
[0,0,0,0],
[1,0,1,0],
[0,0,0,1],
[0,0,1,0],
[0,1,0,0],
[1,0,0,0],
[0,1,0,0],
[1,0,0,0],
[0,1,0,0],
[0,0,0,1],
[0,1,0,0],
[0,0,0,1],
[0,1,0,0],
[0,0,1,0],
[0,1,0,0],
[0,0,0,1],
[0,1,0,0],
[1,0,0,0],
[0,1,0,0],
[0,0,1,0],
[0,0,0,1],

[1,0,0,0],
[0,0,1,0],
[1,0,0,0],
[0,0,1,0],
[0,0,0,1],
[0,0,1,0],
[0,0,0,1],
[0,0,1,0],

[0,1,0,0],
[0,0,1,0],
[0,0,0,1],
[0,0,1,0],
[1,0,0,0],
[0,0,1,0],
[0,1,0,0],
[0,0,0,1],

[0,0,1,0],
[0,0,0,1],
[0,1,0,0],
[0,0,0,1],
[0,0,1,0],
[0,0,0,1],
[0,1,0,0],
[0,0,0,1],

[0,0,1,0],
[0,1,0,0],
[1,0,0,0],
[0,0,0,1],
[0,1,0,0],
[0,0,1,0],
[1,0,0,0],
[0,0,0,1],

[0,1,0,0],
[0,0,1,0],
[0,1,0,0],
[0,0,0,1],
[0,0,1,0],
[0,1,0,0],
[1,0,0,0],
[0,0,1,0],

[1,0,0,0],
[0,1,0,0],
[1,0,0,0],
[0,0,0,1],
[0,0,1,0],
[0,0,0,1],
[1,0,0,0],
[0,1,0,0],

[0,0,1,0],
[0,1,0,0],
[1,0,0,1],
[0,0,0,0],
[1,0,0,0],
[0,0,1,0],
[0,1,0,1],
[0,0,0,0],

[0,0,1,0],
[0,1,0,0],
[0,0,0,1],
[1,0,0,0],
[0,1,0,0],
[0,0,0,1],
[0,1,0,0],
[1,0,0,0],

[0,1,0,0],
[0,0,1,0],
[0,0,0,1],
[0,0,1,0],
[0,1,0,0],
[1,0,0,0],
[0,0,1,0],
[0,0,0,1],

[1,0,0,0],
[0,1,0,0],
[0,0,1,0],
[1,0,0,0],
[0,1,0,0],
[1,0,0,0],
[0,0,0,1],
[0,1,0,0],

[0,0,0,1],
[0,0,1,0],
[0,1,0,0],
[1,0,0,0],
[0,0,0,1],
[1,0,0,0],
[0,0,1,0],
[0,1,0,0],

[0,0,0,1],
[0,0,1,0],
[1,0,0,1],
[0,0,0,0],
[0,0,0,1],
[0,0,1,0],
[1,1,0,0],
[0,0,0,0],

[1,0,0,0],
[0,0,0,1],
[0,1,1,0],
[0,0,0,0],
[0,0,1,0],
[1,0,0,0],
[0,1,0,1],
[0,0,0,0],

[1,0,1,0],
[0,0,1,0],
[1,0,1,0],
[0,0,0,0],
[0,1,0,1],
[0,1,0,0],
[0,1,0,1],
[0,0,0,0],

[0,0,0,1],
[0,0,1,0],
[0,0,0,1],
[0,0,1,0],
[0,0,0,1],
[0,0,0,0],
[0,0,1,0],
[0,0,0,0],
[0,0,0,0],
[0,1,0,0],
[0,0,0,0],
[0,0,0,0],
[1,0,0,0],
[0,0,0,0],
[0,0,1,0],
[0,0,0,0],

[0,1,0,0],
[0,0,1,0],
[0,1,0,0],
[0,0,1,0],
[0,1,0,0],
[0,0,0,0],
[0,0,0,1],
[0,0,0,0],
[0,0,0,0],
[1,0,0,0],
[0,0,0,0],
[0,0,0,0],
[0,1,0,0],
[0,0,0,0],
[0,0,1,0],
[0,0,0,0],

[0,0,0,1],
[0,1,0,0],
[0,0,0,1],
[0,1,0,0],
[0,0,0,1],
[0,0,0,0],
[0,0,1,0],
[0,0,0,0],
[0,0,0,0],
[0,0,0,1],
[0,0,0,0],
[0,0,0,0],
[1,0,0,0],
[0,0,0,0],
[0,0,1,0],
[0,0,0,0],

[1,0,0,0],
[0,0,0,1],
[1,0,0,0],
[0,0,0,1],
[1,0,0,0],
[0,0,0,0],
[0,0,1,0],
[0,0,0,0],
[0,0,0,0],
[0,1,0,0],
[0,0,0,0],
[0,0,0,0],
[0,0,0,1],
[0,0,0,0],
[0,0,1,0],
[0,0,0,0],

[0,1,0,0],
[1,0,0,0],
[0,1,0,0],
[1,0,0,0],
[0,1,0,0],
[0,0,0,0],
[1,0,0,0],
[0,0,0,0],
[0,0,0,0],
[0,0,0,1],
[0,0,0,0],
[0,0,0,0],
[0,1,1,0],
[0,0,0,0],
[1,0,0,1],
[0,0,0,0],

[0,0,0,0],
[0,0,0,0],
[0,0,0,0],
[1,0,0,1],

[0,0,1,0],
[0,1,0,0],
[0,0,0,1],
[1,0,0,0],
[0,1,0,0],
[0,0,1,0],
[0,0,0,1],
[0,1,0,0],

[1,0,0,1],
[0,0,0,0],
[0,0,0,0],
[0,0,0,0],

[0,0,0,0],
[0,0,0,0],
[0,0,0,0],
[0,0,0,0]]
    
     #-------------------LOADING PICS / RESIZING---------------------------------------------------------------------------------------------------------------------------------------------------------------------

    top = loadImage("topchart.png")
    ipic = loadImage("ipic.png")
    left = loadImage("left.png")
    down = loadImage("down.png")
    up = loadImage("up.png")
    right = loadImage("right.png")
    Xbg = loadImage("Xepher-bg.png")  
    topleft = loadImage("topleft.png")  
    topright = loadImage("topright.png")
    topup = loadImage("topup.png")
    topdown = loadImage("topdown.png")
    great = loadImage("great.png")
    tostart = loadImage("tostart.png")
    leaderboardscr = loadImage("DDR.jpeg")
    highscore = loadImage("highscore.png")
    goback = loadImage("goback.png")
    pika1 = loadImage("pika1.png")
    pika2 = loadImage("pika2.png")   
    pika3 = loadImage("pika3.png")   
    pika4 = loadImage("pika4.png")   
    original = loadImage("original.png")
    gamewall = loadImage("gamescreenwall.jpg")
    themesetup= loadImage("themesetup.png")
    pokemonlogo = loadImage("pokemonlogo.png")
    xepher = loadImage("Xepher.png")
    xepher1 = loadImage("Xepher(1).png")
    cd = loadImage("CD.png")
    cd1 = loadImage("CD1.png")
    themehow = loadImage("themehow.png")
    howtosong = loadImage("howtosong.png")
    howtolevel = loadImage("howtolevel.png")
    level = loadImage("level.png")
    level1 = loadImage("level1.png")
    level2 = loadImage("level2.png")
    level3 = loadImage("level3.png")
    bg1 = loadImage("bg1.png")
    cdbg = loadImage("Caramelldancing-bg.png")
    themewall = loadImage("themewall.jpg")
    themehow.resize(450,270)
    themesetup.resize(400,90)
    pokemonwall = loadImage("pokemonwall.png")
    gamewall.resize(900,700)
    themewall.resize(900,700)
    congrat = loadImage("congrat.png")
    congrat.resize(300,100)
    xepher.resize(280,100)
    xepher1.resize(280,100)
    cd.resize(280,100)
    cd1.resize(280,100)
    howtosong.resize(350,50)
    howtolevel.resize(350,50)
    pokemonlogo.resize(350,150)
    original.resize(350,150)
    level.resize(240,240)
    level1.resize(240,240)
    level2.resize(240,240)
    level3.resize(240,240)
    pokemonwall.resize(900,700)
    leaderboardscr.resize(1200,700)
    goback.resize(200,60)
    highscore.resize(370,170)
    tostart.resize(210,30)
    left.resize(100,100)
    down.resize(100,100)
    up.resize(100,100)
    right.resize(100,100) 
    great.resize(200,90)
    if mode == 10:
        if themeoriginal:
            minim = Minim(this)
            player4 = minim.loadFile("BUTTERFLY.mp3")
            player4.loop()
    
        gamestart = loadImage("gamestart.png")
        gamestart1 = loadImage("gamestart(1).png")
        instructions = loadImage("instructions.png")
        instructions1 = loadImage("instructions(1).png")
        theme = loadImage("theme.png")
        theme1 = loadImage("theme(1).png")
        leaderboard = loadImage("leaderboard.png")
        leaderboard1 = loadImage("leaderboard(1).png")
        logo = loadImage("DDRLogo.png")
        name = loadImage("name.png")
        bg = loadImage("wallpaper.jpg")
        dance1 = loadImage("dance1.png")
        dance2 = loadImage("dance2.png") 
        dance3 = loadImage("dance3.png")
        dance4 = loadImage("dance4.png")
        dance5 = loadImage("dance5.png")
        dance6 = loadImage("dance6.png")
        dance7 = loadImage("dance7.png")
        logo.resize(300,100)
        gamestart.resize(300,100)
        gamestart1.resize(300,100)
        instructions.resize(300,100)
        instructions1.resize(300,100)
        theme.resize(300,100)
        theme1.resize(300,100)
        leaderboard.resize(300,100)
        leaderboard1.resize(300,100)
        bg.resize(900,700)
        
        name.resize(270,100)

        
def draw():
    global stepchartCM,ipic,congrat,stepchartCE,bpmCE,playerC, cdbg,tostart,bpmXE,stepchartXE,Xbg,screen,great,topimg,topup, topdown,topleft,topright,lefton, downon, righton, upon,pos, x, y, top, left, up, right, down, bg, displaying,stepchartXH,player1,name1, name2,name3,score1,score2,score3,song1,song2,song3,highscore,goback,jump,pika1,pika2,pika3,pika4, player3,themepokemon,pokemonwall,original,themesel,themeorignal,themesetup,themewall,levelsel,levelmode,level,level1,level2,level3, howtolevel,howtosong,cd,cd1,songmode, songsel,mode,xeher1,gamewall,player,gamestart, gamestart1,logo, name, theme, theme1, instructions, instrctions1, menuselection,bg,leaderboard, leaderboard1,dance1, dance2, dance3, dance4, dance5, dance6, dance7, dance, x, y, dy, left, up, right, down, stepchart,bg1, displaying
    if mode == 1:
        image(ipic,0,0)
        image(goback,100,610)
        
    
    if mode == 0:
        background(255,255,255)
        image(gamewall, 0,0)
        image(howtosong,420,30)
        image(howtolevel,50,30)
        image(level,20,200)
        image(goback,100,610)
        image(tostart,500,600)
       #song
        if songsel == 0:
            image(xepher1, 490,100)
        else:
            image(xepher, 490,100)
        if songsel == 1:
            image(cd1, 490, 390)
        else:
            image(cd, 490, 390)
       #level
        if levelsel == 0:
            image(level1, 20,200)

        if levelsel ==1:
            image(level2,20, 200)
 

        if songmode == 1 and levelmode ==1:
            player3.pause()
            player4.pause()
            player.pause()
            if screen == 0:
                playerC.play()
                background(0)
                image(cdbg, 0,200)
                
                if topimg == 0:
                    image(top,10,50)
                elif topimg == 1:
                    image(topleft,10,50)
                elif topimg == 2:
                    image(topdown, 10,50)
                elif topimg ==3:
                    image(topup, 10, 50)
                elif topimg == 4:
                    image(topright, 10,50)
                
                x = x+ 1
                y = y + 1
                positioninchart =0
                image(cdbg, 0,200)
                text("SCORE:", 425, 50)
                text(score, 490, 50)
            
                text("FR:", 425, 70)
                text(frameRate, 490, 70)
            
                
                #stepchart ends around >660
                
                current_beat = int(playerC.position() / bpmCE) 
            
                text ("step" + str(current_beat), 200,50) # number of  
                """
                USE THIS TO TEST GAME
                if upon:
                    text("up",700,100)
                
                if downon:
                    text("down",650,100)
                if lefton:
                    text("left",600,100)
            
                if righton:
                    text("right",750,100)
            """   
                if current_beat > 0: 
                    for i in range(8): #FIXME
                        sy=50
                    
                        
                        displaying= stepchartCM[ current_beat:current_beat+8]
                    
                        
                        for arrow in displaying:
                            
                                if arrow[0] == 1:
                                    image(left, 30,sy)
                                    #check if in correct y range -= turn on boolean
                                    if sy>90:
                                        lefton = True
                                    else:
                                        lefton = False 
                                    print sy
                                    
                                    
                                if arrow[1] == 1:
                                    image(down, 177,sy)
                                    if sy >90:
                                        downon = True
                                    else:
                                        downon = False 
                                    
                                if arrow[2] == 1:
                                    image(up, 307, sy)
                                    if sy >90:
                                        upon = True
                                    else:
                                        upon = False 
                                if arrow[3] == 1:
                                    image(right, 427,sy)
                                    if sy > 90:
                                        righton = True
                                    else:
                                        righton = False
                                
                                sy = sy+60
                        if current_beat >330:
                            playerC.pause()
                            screen = 1
                    topimg = 0
        if screen == 1:
            background (6)
            image(congrat,300,100)
            text("SCORE:",300,300)
            text(score,390,300)
            image(goback,100,610)
            songmode = 50
            levelmode = 50
            current_beat = 0
            if score > score3 and score > score2 and score > score1:
                score1 = score
                song1 = "Caramelldacning"
            if score > score3 and score > score2:
                score2 = score
                song2 = "Caramelldacning"
                #name2 = str(input("enter your name"))
            if score > score3:
                score3 = score
                song3 = "Caramelldacning"
                #name3 = str(raw_input("enter your name"))
                image(cd,300,100)
            
        if songmode == 1 and levelmode ==0:
            player3.pause()
            player4.pause()
            player.pause()
            if screen == 0:
                playerC.play()
                background(0)
                image(cdbg, 0,200)
                
                if topimg == 0:
                    image(top,10,50)
                elif topimg == 1:
                    image(topleft,10,50)
                elif topimg == 2:
                    image(topdown, 10,50)
                elif topimg ==3:
                    image(topup, 10, 50)
                elif topimg == 4:
                    image(topright, 10,50)
                
                x = x+ 1
                y = y + 1
                positioninchart =0
                image(cdbg, 0,200)
                text("SCORE:", 425, 50)
                text(score, 490, 50)
            
                text("FR:", 425, 70)
                text(frameRate, 490, 70)
            
                
                #stepchart ends around >660
                
                current_beat = int(playerC.position() / bpmCE) 
            
                text ("step" + str(current_beat), 200,50) # number of  
                """
                USE THIS TO TEST GAME
                if upon:
                    text("up",700,100)
                
                if downon:
                    text("down",650,100)
                if lefton:
                    text("left",600,100)
            
                if righton:
                    text("right",750,100)
            """   
                if current_beat > 0: 
                    for i in range(8): #FIXME
                        sy=50
                    
                        
                        displaying= stepchartCE[ current_beat:current_beat+8]
                    
                        
                        for arrow in displaying:
                            
                                if arrow[0] == 1:
                                    image(left, 30,sy)
                                    #check if in correct y range -= turn on boolean
                                    if sy>90:
                                        lefton = True
                                    else:
                                        lefton = False 
                                    print sy
                                    
                                    
                                if arrow[1] == 1:
                                    image(down, 177,sy)
                                    if sy >90:
                                        downon = True
                                    else:
                                        downon = False 
                                    
                                if arrow[2] == 1:
                                    image(up, 307, sy)
                                    if sy >90:
                                        upon = True
                                    else:
                                        upon = False 
                                if arrow[3] == 1:
                                    image(right, 427,sy)
                                    if sy > 90:
                                        righton = True
                                    else:
                                        righton = False
                                
                                sy = sy+60
                        if current_beat >330:
                            playerC.pause()
                            screen = 1
                    topimg = 0
        if screen == 1:
            background (6)
            image(congrat,300,100)
            text("SCORE:",300,300)
            text(score,390,300)
            image(goback,100,610)
            songmode = 50
            levelmode = 50
            current_beat = 0
            if score > score3 and score > score2 and score > score1:
                score1 = score
                song1 = "Caramelldacning"
            if score > score3 and score > score2:
                score2 = score
                song2 = "Caramelldacning"
                #name2 = str(input("enter your name"))
            if score > score3:
                score3 = score
                song3 = "Caramelldacning"
                #name3 = str(raw_input("enter your name"))
                image(cd,300,100)
            
        if songmode==0 and levelmode ==0:
            player3.pause()
            player4.pause()
            if screen == 0:
                player.play()
                background(0)
            
                if topimg == 0:
                    image(top,10,50)
                elif topimg == 1:
                    image(topleft,10,50)
                elif topimg == 2:
                    image(topdown, 10,50)
                elif topimg ==3:
                    image(topup, 10, 50)
                elif topimg == 4:
                    image(topright, 10,50)
                
                x = x+ 1
                y = y + 1
                positioninchart =0
                image(Xbg, 0,200)
                text("SCORE:", 425, 50)
                text(score, 490, 50)
            
                text("FR:", 425, 70)
                text(frameRate, 490, 70)
            
                
                #stepchart ends around >660
                
                current_beat = int(player.position() / bpmXE) 
            
                text ("step" + str(current_beat), 200,50) # number of  
                """
                USE THIS TO TEST GAME
                if upon:
                    text("up",700,100)
                
                if downon:
                    text("down",650,100)
                if lefton:
                    text("left",600,100)
            
                if righton:
                    text("right",750,100)
            """   
                if current_beat > 0: 
                    for i in range(8): #FIXME
                        sy=50
                    
                        # FIXME
                        displaying= stepchartXE[ current_beat:current_beat+8]
                    
                        
                    
                        #translate(10,-(int(player.position())))
                        #translate(10,-(int(player.position()))) # FIXME
                        for arrow in displaying:
                            
                                if arrow[0] == 1:
                                    image(left, 30,sy)
                                    #check if in correct y range -= turn on boolean
                                    if sy>90:
                                        lefton = True
                                    else:
                                        lefton = False 
                                    print sy
                                    
                                    
                                if arrow[1] == 1:
                                    image(down, 177,sy)
                                    if sy >90:
                                        downon = True
                                    else:
                                        downon = False 
                                    
                                if arrow[2] == 1:
                                    image(up, 307, sy)
                                    if sy >90:
                                        upon = True
                                    else:
                                        upon = False 
                                if arrow[3] == 1:
                                    image(right, 427,sy)
                                    if sy > 90:
                                        righton = True
                                    else:
                                        righton = False
                                
                                sy = sy+60
                        if current_beat >290:
                            player.pause()
                            screen = 1
                    topimg = 0
        if screen == 1:
            background (0)
            image (congrat,300,50)
            text("SCORE:",300,300)
            text(score,390,300)
            image(goback,100,610)
            songmode = 50
            levelmode = 50
            current_beat = 0
            if score > score3 and score > score2 and score > score1:
                score1 = score
                song1 = "Xepher"
            if score > score3 and score > score2:
                score2 = score
                song2 = "Xepher"
                #name2 = str(input("enter your name"))
            if score > score3:
                score3 = score
                song3 = "Xepher"
                #name3 = str(raw_input("enter your name"))
            
        
            
        if songmode==0 and levelmode ==1:
            player3.pause()
            player4.pause()
            if screen == 0:
                player.play()
                background(0)
                
            
                if topimg == 0:
                    image(top,10,50)
                elif topimg == 1:
                    image(topleft,10,50)
                elif topimg == 2:
                    image(topdown, 10,50)
                elif topimg ==3:
                    image(topup, 10, 50)
                elif topimg == 4:
                    image(topright, 10,50)
                
                x = x+ 1
                y = y + 1
                positioninchart =0
                image(Xbg, 0,200)
                text("SCORE:", 425, 50)
                text(score, 490, 50)
            
                text("FR:", 425, 70)
                text(frameRate, 490, 70)
            
                
                #stepchart ends around >660
                current_beat = int(player.position() / mpb) 
            
                if  current_beat > 250 and current_beat < 350:
                    mpb == 270
                if  current_beat > 350 and current_beat < 450:
                    mpb == 210
                if  current_beat > 500:
                    mpb == 170
                text ("step" + str(current_beat), 200,50) # number of  
                """
                USE THIS TO TEST GAME
                if upon:
                    text("up",700,100)
                
                if downon:
                    text("down",650,100)
                if lefton:
                    text("left",600,100)
            
                if righton:
                    text("right",750,100)
            """   
                if current_beat > 0: 
                    for i in range(8): #FIXME
                        sy=50
                    
                        # FIXME
                        displaying= stepchartXH[ current_beat:current_beat+8]
                    
                        
                    
                        #translate(10,-(int(player.position())))
                        #translate(10,-(int(player.position()))) # FIXME
                        for arrow in displaying:
                            
                                if arrow[0] == 1:
                                    image(left, 30,sy)
                                    #check if in correct y range -= turn on boolean
                                    if sy>90:
                                        lefton = True
                                    else:
                                        lefton = False 
                                    print sy
                                    
                                    
                                if arrow[1] == 1:
                                    image(down, 177,sy)
                                    if sy >90:
                                        downon = True
                                    else:
                                        downon = False 
                                    
                                if arrow[2] == 1:
                                    image(up, 307, sy)
                                    if sy >90:
                                        upon = True
                                    else:
                                        upon = False 
                                if arrow[3] == 1:
                                    image(right, 427,sy)
                                    if sy > 90:
                                        righton = True
                                    else:
                                        righton = False
                                
                                sy = sy+60
                        if current_beat >710:
                            player.pause()
                            screen = 1
                    topimg = 0
        if screen == 1:
            background (0)
            image (congrat,300,50)
            text("SCORE:",300,300)
            text(score,390,300)
            if score > score3 and score > score2 and score > score1:
                score1 = score
                song1 = "Xepher"
            if score > score3 and score > score2:
                score2 = score
                song2 = "Xepher"                    
                #name2 = str(input("enter your name"))
            if score > score3:
                score3 = score
                song3 = "Xepher"
                #name3 = str(raw_input("enter your name")
                songmode = 50
                levelmode = 50
                image(goback,100,610)
                current_beat = 0
                
                
            
        
    if mode == 3:#highscores
       
        image(leaderboardscr,-300,0)
        fill(0)
        rect(0,0,200,200)
        rect(0,350,450,100)
        fill(255,255,255)
        image(goback,100,610)
        image(highscore,30,10)
        text(score1, 360, 210)
        text(score2, 360, 310)
        text(score3, 360, 410)
        #text(name1, 100, 210)
        #text(name2, 100, 310)
        #text(name3, 100, 410)
        text(song1, 235, 210)
        text(song2, 235, 310)
        text(song3, 235, 410)
    
        
    if mode == 2:#themesetup
        background(255,255,255)
        image(themewall, 0,0)
        image(themesetup,10,50)
        image(pokemonlogo,5,170)
        image(original,5,350)
        image(themehow, 450,250)
        if themesel == 0:
            fill(255,255,255)
            rect(5,310,350,20)
        if themesel == 1:
            fill(255,255,255)
            rect(5,530,350,20)
            
            
        
    
   
        
            
    
    if mode == 10 and themeoriginal == True:
        player3.pause()
        player4.play()
        if dance >= 1 and dance<=10:
            image(dance1, 450,170)
        elif dance >= 10 and dance<=20:
            image(dance2, 450,170)
        elif dance >= 20and dance<=30:
            image(dance3, 450,170)
        elif dance >= 30and dance<=40:
            image(dance4, 450,170)
        elif dance >= 40and dance<=50:
            image(dance5, 450,170)
        elif dance >= 50and dance<=60:
            image(dance6, 450,170)
        elif dance >= 60:
            image(dance7, 450,170)
        image(logo,50,20)
        image(bg,0,0)
        image(name, 570,570)
        #background(255,255,255)
        if menuselection == 0:
            image(gamestart1, 150, 150)
        if menuselection != 0:
            image(gamestart, 150, 150)
        if menuselection == 1:
            image(instructions1, 150, 250)
        if menuselection != 1:
            image(instructions, 150, 250)
        
        if menuselection == 2:
            image(theme1,150, 350)
        if menuselection != 2:
            image(theme, 150, 350)
        if menuselection == 3:
            image(leaderboard,150, 450)
        if menuselection != 3:
            image(leaderboard1, 150, 450)
        if dance >= 1 and dance<=10:
            image(dance1, 450,170)
        elif dance >= 10 and dance<=20:
            image(dance2, 450,170)
        elif dance >= 20and dance<=30:
            image(dance3, 450,170)
        elif dance >= 30and dance<=40:
            image(dance4, 450,170)
        elif dance >= 40and dance<=50:
            image(dance5, 450,170)
        elif dance >= 50and dance<=60:
            image(dance6, 450,170)
        elif dance >= 60:
            image(dance7, 450,170)
        dance = dance+1
        if dance == 60:
            dance = dance - 59
        image(logo,50,20)
    
    if mode == 10 and themepokemon:
        player4.pause()
        player3.play()

        image(pokemonwall,0,0)
        if jump >= 1 and jump<=10:
            image(pika1, 450,170)
            image(pika1, 600,210)
            image(pika1, 680,280)
        elif jump >= 10 and jump<=20:
            image(pika2, 450,170)
            image(pika2, 600,210)
            image(pika2, 680,280)
        elif jump >= 20 and jump<=30:
            image(pika3, 450,170)
            image(pika3, 600,210)
            image(pika3, 680,280)
        elif jump>= 30 and jump<=40:
            image(pika4, 450,170)
            image(pika4, 600,210)
            image(pika4, 680,280)
        jump = jump+1
        if jump == 40:
            jump = jump-39
        image(logo,50,20)
        image(name, 570,570)
        

        #background(255,255,255)
        if menuselection == 0:
            image(gamestart1, 150, 150)
        if menuselection != 0:
            image(gamestart, 150, 150)
        if menuselection == 1:
            image(instructions1, 150, 250)
        if menuselection != 1:
            image(instructions, 150, 250)
        
        if menuselection == 2:
            image(theme1,150, 350)
        if menuselection != 2:
            image(theme, 150, 350)
        if menuselection == 3:
            image(leaderboard,150, 450)
        if menuselection != 3:
            image(leaderboard1, 150, 450)

            
        
def keyPressed():
    global playerC, cdbg,player, current_beat,screen,great,lefton, downon, righton, upon, score, stepchart, y ,x, bg, displaying,topup, topdown,topleft,topright,leftpr,topimg,themesel,levelsel,levelmode,mode, gamestart, gamestart1,logo, menuselection, instructions, instructions1, theme, theme1,leaderboard, leaderboard1,songsel,songmode,themeoriginal, themepokemon
    print keyCode
    if mode == 10:
        if keyCode == 40: #up
                if menuselection != 3:
                    menuselection =menuselection+ 1
                
                    
        
        elif keyCode == 38:#down
                if menuselection != 0:
                    menuselection =menuselection- 1
        if keyCode == 10: #enter
            mode = menuselection
    if mode == 0:
        if keyCode == 39: #right
                if songsel != 1:
                    songsel =songsel+ 1
                    
        
        elif keyCode == 37:#left
                if songsel != 0:
                    songsel =songsel- 1
        if keyCode == 40: #up
                if levelsel != 1:
                    levelsel =levelsel+ 1
                    
        
        elif keyCode == 38:#down
                if levelsel != 0:
                    levelsel=levelsel- 1
        if keyCode == 71: #enter
            songmode = songsel
            levelmode = levelsel
            print songmode, levelmode
        if songmode==0 and levelmode==0:
            if screen == 0:
                print keyCode   
                if keyCode == 37:
                    topimg = 1
                    if lefton:
                        score = score+1
                        image(great,10,10)
                        lefton = False
                if keyCode ==40:
                    topimg = 2
                    image(topdown,10,50)
                    if downon:
                        score = score+1
                        image(great,10,10)
                        downon = False
                if keyCode ==38:
                    topimg = 3
                    if upon:
                        image(great,10,10)
                        score = score+1
                        upon = False
                if keyCode ==39:
                    topimg = 4
                    if righton:
                        image(great,10,10)
                        score = score+1
                        righton = False
                if keyCode == 66:
                    mode = 10
                    screen = 0
                    player.pause()
                    player.rewind()
                    songmode = 50
                    score = 0
                    
            if screen == 1:
                if keyCode == 66:
                    mode = 10
                    screen = 0
                    player.pause()
                    player.rewind()
                    current_beat = 0
                    score = 0
        if songmode==0 and levelmode ==1:
            if screen == 0:
                print keyCode   
                if keyCode == 37:
                    topimg = 1
                    if lefton:
                        score = score+1
                        image(great,10,10)
                        lefton = False
                if keyCode ==40:
                    topimg = 2
                    image(topdown,10,50)
                    if downon:
                        score = score+1
                        image(great,10,10)
                        downon = False
                if keyCode ==38:
                    topimg = 3
                    if upon:
                        image(great,10,10)
                        score = score+1
                        upon = False
                if keyCode ==39:
                    topimg = 4
                    if righton:
                        image(great,10,10)
                        score = score+1
                        righton = False
                if keyCode == 66:
                    mode = 10
                    screen = 0
                    player.pause()
                    player.rewind()
                    songmode = 50
                    score = 0
                if screen == 1:
                    if keyCode == 66:
                        mode = 10
                        screen = 0
                        player.pause()
                        player.rewind()
                        current_beat = 0
                        score = 0
        if songmode==1 and levelmode ==0:
            if screen == 0:
                    
                print keyCode   
                if keyCode == 37:
                    topimg = 1
                    if lefton:
                        score = score+1
                        image(great,10,10)
                        lefton = False
                if keyCode ==40:
                    topimg = 2
                    image(topdown,10,50)
                    if downon:
                        score = score+1
                        image(great,10,10)
                        downon = False
                if keyCode ==38:
                    topimg = 3
                    if upon:
                        image(great,10,10)
                        score = score+1
                        upon = False
                if keyCode ==39:
                    topimg = 4
                    if righton:
                        image(great,10,10)
                        score = score+1
                        righton = False
                if keyCode == 66:
                    mode = 10
                    screen = 0
                    playerC.pause()
                    playerC.rewind()
                    songmode = 50
                    score = 0
                        
            if screen == 1:
                 if keyCode == 66:
                        mode = 10
                        screen = 0
                        player.pause()
                        player.rewind()
                        current_beat = 0
                        score = 0
        if songmode==1 and levelmode ==0:
                if screen == 0:
                    print keyCode   
                    if keyCode == 37:
                        topimg = 1
                        if lefton:
                            score = score+1
                            image(great,10,10)
                            lefton = False
                    if keyCode ==40:
                        topimg = 2
                        image(topdown,10,50)
                        if downon:
                            score = score+1
                            image(great,10,10)
                            downon = False
                    if keyCode ==38:
                        topimg = 3
                        if upon:
                            image(great,10,10)
                            score = score+1
                            upon = False
                    if keyCode ==39:
                        topimg = 4
                        if righton:
                            image(great,10,10)
                            score = score+1
                            righton = False
                    
                    
                    if keyCode == 66:
                        mode = 10
                        screen = 0
                        playerC.pause()
                        playerC.rewind()
                        songmode = 50
                        score = 0
                        
                if screen == 1:

                    if keyCode == 66:
                        mode = 10
                        screen = 0
                        playerC.pause()
                        playerC.rewind()
                        current_beat = 0
                        score = 0
    if mode == 1:
        if keyCode == 66:
            mode = 10
  
                      
    if mode == 3:
        if keyCode == 66:
            mode = 10
    if mode == 2:
        
        if keyCode == 40: #up
                if themesel != 1:
                    themesel =themesel+ 1
      
            
        
                    
        
        elif keyCode == 38:#down
                if themesel != 0:
                    themesel =themesel- 1
    
           
        
        if keyCode == 66:
            if themesel == 0:
                themepokemon = True
                themeoriginal = False
                mode = 10
                print themepokemon
            if themesel ==1:
                themeoriginal = True
                themepokemon = False
                mode = 10
   
        
            
                
            
                
                
                
        
