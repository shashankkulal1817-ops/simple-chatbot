# AI STUDY BOT🤓:
import datetime
import time
name =input("welcome💀,enter ur name")
presenthour=datetime.datetime.now().hour
if 5<= presenthour <=11:
    print("good morning",name)
elif 11<=presenthour <=17:
    print("good afternoon",name) 
elif 17 <= presenthour <=20:
    print("good evening",name)
else:
    print("good night",name)           

print("namaste","welcome to rule based CHATBOT😍")
print("you can ask me a basic questions, you can EXIT by typing BYE ✌️")

response={
    "hello":"HI WELCOME TO CHATBOT.HOW CAN I HELP U😎",
    " how are you":" IAM FINE THANKYOU,""WHAT ABOUT YOU ⁇",
    "iam also good": "OK FINE👍",
    "motivate me":"KEEP TRYING HARD U WILL GET WHAT U WANT ONE DAY ❤️",
    " what is function in python":" SORRY !😌,IAM STILL LEARNING ",
    "hello": "HI WELCOME TO CHATBOT. HOW CAN I HELP U 😊",
    "how are you": "I AM FINE THANK YOU. WHAT ABOUT YOU?",
    "i am also good": "OK FINE 👍",
    "motivate me": "KEEP TRYING HARD. U WILL GET WHAT U WANT ONE DAY 💕",
    "what is function in python": "SORRY 😊, I AM STILL LEARNING 💕",
    "what is your name": "MY NAME IS STUDY BOT 🤖",
    "who created you": "I WAS CREATED BY SHASHANK 😎",
    "what can you do": "I CAN ANSWER BASIC QUESTIONS AND CHAT WITH YOU 😊",
    "what is python": "PYTHON IS A SIMPLE AND POWERFUL PROGRAMMING LANGUAGE 🐍",
    "what is ai": "AI MEANS ARTIFICIAL INTELLIGENCE 🤖",
    "what is your purpose": "MY PURPOSE IS TO HELP YOU WITH BASIC QUESTIONS 😊",
    "tell me a joke": "WHY DO PROGRAMMERS LIKE DARK MODE? BECAUSE LIGHT ATTRACTS BUGS 😂",
    "thank you": "YOU ARE MOST WELCOME 😊💕",
    "bye": "BYE 👋 HAVE A GREAT DAY!",
    "good morning": "GOOD MORNING ☀️ HAVE A WONDERFUL DAY!",
    "good night": "GOOD NIGHT 🌙 SWEET DREAMS!",
    "what is your favourite color": "I LIKE ALL COLORS 🌈",
    "are you intelligent": "I AM STILL LEARNING, BUT I WILL TRY MY BEST 🤖",
    "can you help me": "YES OF COURSE! ASK ME ANYTHING 😊",
    "can u play a game":"NO I CANT😌",
    " i just need one help":" YAA TELL ME",
    " what is c": " 💀C IS A POWERFUL PROGRAMMING LANGUAGE USED FOR SYSTEM AND APPLICATION DEVELOPMENT 💻",
    "what is machine learning": " 🥶MACHINE LEARNING IS A PART OF AI THAT HELPS COMPUTERS LEARN FROM DATA 📊",
    "what is a variable": "A VARIABLE IS A NAME USED TO STORE A VALUE IN A PROGRAM 📦",
    "what is a loop": "🫠A LOOP IS USED TO REPEAT A SET OF INSTRUCTIONS 🔄",
    "what is a list": "A LIST IS USED TO STORE MULTIPLE VALUES IN A SINGLE VARIABLE 📋",
    "what is dictionary": "A DICTIONARY STORES DATA IN KEY AND VALUE PAIRS 🗂️",
    "what is an algorithm": "AN ALGORITHM IS A STEP BY STEP PROCEDURE TO SOLVE A PROBLEM 🧠",
    "what is a flowchart": "😐A FLOWCHART IS A DIAGRAM THAT REPRESENTS THE STEPS OF A PROCESS 📈",
    "what is a computer": "A COMPUTER IS AN ELECTRONIC DEVICE THAT PROCESSES DATA 💻",
    "what is hardware": "HARDWARE MEANS THE PHYSICAL PARTS OF A COMPUTER, LIKE KEYBOARD AND CPU 🖥️",
    "what is software": "SOFTWARE IS A SET OF PROGRAMS OR INSTRUCTIONS THAT TELLS A COMPUTER WHAT TO DO 💾",
    "what is cpu": "CPU MEANS CENTRAL PROCESSING UNIT. IT IS CALLED THE BRAIN OF THE COMPUTER 🧠",
    "what is ram": "RAM IS TEMPORARY MEMORY USED BY A COMPUTER WHILE RUNNING PROGRAMS ⚡",
    "what is internet": "THE INTERNET IS A GLOBAL NETWORK THAT CONNECTS COMPUTERS WORLDWIDE 🌐",
    "what is coding": "CODING IS THE PROCESS OF WRITING INSTRUCTIONS FOR A COMPUTER 👨‍💻",
    "what is debugging": "DEBUGGING IS THE PROCESS OF FINDING AND FIXING ERRORS IN A PROGRAM 🐛",
    "what is an error": "AN ERROR IS A PROBLEM IN A PROGRAM THAT PREVENTS IT FROM WORKING CORRECTLY ⚠️",
    "what is html": "HTML IS USED TO CREATE THE STRUCTURE OF WEB PAGES 🌐",
    "what is css": "CSS IS USED TO DESIGN AND STYLE WEB PAGES 🎨",
    "what is database": "A DATABASE IS AN ORGANIZED COLLECTION OF DATA 🗄️",
    "what is cloud computing": "CLOUD COMPUTING PROVIDES STORAGE AND COMPUTING SERVICES THROUGH THE INTERNET ☁️",
    "what is cybersecurity": "CYBERSECURITY IS THE PRACTICE OF PROTECTING COMPUTERS AND DATA FROM ATTACKS 🔒",
    "how can i learn python": "START WITH BASICS, PRACTICE PROGRAMS DAILY AND BUILD SMALL PROJECTS 🐍💻",
    "how can i improve my coding skills": "PRACTICE REGULARLY 👀, SOLVE PROBLEMS AND BUILD PROJECTS 💻🔥",
    "what is programming": "PROGRAMMING IS THE PROCESS OF WRITING INSTRUCTIONS THAT A COMPUTER CAN UNDERSTAND 💻",
    "what is artificial intelligence": "ARTIFICIAL INTELLIGENCE IS A TECHNOLOGY THAT ENABLES MACHINES TO PERFORM INTELLIGENT TASKS 🤖",
    "what is data science": "DATA SCIENCE IS THE STUDY OF DATA TO FIND USEFUL INFORMATION AND INSIGHTS 📊",
    "what is web development": "WEB DEVELOPMENT 😎 IS THE PROCESS OF CREATING AND MAINTAINING WEBSITES 🌐",
    "what is app development": "APP DEVELOPMENT 😊 IS THE PROCESS OF CREATING APPLICATIONS FOR MOBILE OR OTHER DEVICES 📱",
    "what is an operating system": "AN OPERATING SYSTEM MANAGES COMPUTER HARDWARE AND SOFTWARE 🖥️",
    "what is a compiler": "A COMPILER TRANSLATES PROGRAMMING CODE INTO A FORM THAT A COMPUTER CAN EXECUTE ⚙️",
    "what is an interpreter": "AN INTERPRETER EXECUTES PROGRAM CODE LINE BY LINE 🐍",
    "what is source code": "SOURCE CODE IS THE ORIGINAL CODE WRITTEN BY A PROGRAMMER 💻",
    "what is open source": "OPEN SOURCE SOFTWARE ALLOWS ITS SOURCE CODE TO BE VIEWED AND MODIFIED BY PEOPLE 🌐",
    "what is an api": "AN ✌️ API ALLOWS DIFFERENT SOFTWARE APPLICATIONS TO COMMUNICATE WITH EACH OTHER 🔗",
    "what is github": "GITHUB IS A PLATFORM USED TO STORE 🤓, MANAGE AND SHARE CODE 👨‍💻",
    "what is a server": "A SERVER PROVIDES DATA OR SERVICES TO OTHER COMPUTERS THROUGH A NETWORK 🖥️",
    "what is an ip address": "AN IP ADDRESS IS A UNIQUE ADDRESS USED TO IDENTIFY A DEVICE ON A NETWORK 🌐",
    "what is a bug": "A BUG IS AN ERROR OR PROBLEM IN A COMPUTER PROGRAM 🐛",
    "what is a syntax error": " 💕A SYNTAX ERROR HAPPENS WHEN THE RULES OF A PROGRAMMING LANGUAGE ARE NOT FOLLOWED ⚠️",
    "what is a project": "A PROJECT IS A PRACTICAL WORK CREATED TO SOLVE A PROBLEM OR APPLY KNOWLEDGE 🛠️",
    "why is coding important": "CODING IS IMPORTANT BECAUSE IT HELPS CREATE SOFTWARE 🤩, WEBSITES 🫡, APPS AND MANY DIGITAL SOLUTIONS 🚀"
}
def getresponse(userquestion):
    for eachkey in response:
        if eachkey in userquestion:
            return response[eachkey]
    return " iam not able to tell u tht iam still learning"

while True:
    userinput=input("pls👀 ! ,enter ur questions")
    reply=getresponse(userinput)
    print(reply)
    if "bye"in userinput.lower():
        break
