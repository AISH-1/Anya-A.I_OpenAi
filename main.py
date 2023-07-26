import speech_recognition as sr
import pyaudio
import win32com.client
import os
import webbrowser
import openai
from config import apikey
import datetime

chatStr = ""

speaker = win32com.client.Dispatch("SAPI.SpVoice")

def chat(query):
    global chatStr
    print(chatStr)
    openai.api_key = apikey
    chatStr += f"User: {query}\n Anya: "
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=chatStr,
        temperature=0.7,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    # todo: a try catch block
    say(response["choices"][0]["text"])
    chatStr += f"{response['choices'][0]['text']}\n"
    return response["choices"][0]["text"]


def ai(prompt):
    openai.api_key = apikey
    text = f"OpenAI response for Prompt: {prompt} \n *************************\n\n"

    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        temperature=0.7,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    # todo: try catch block
    # print(response["choices"][0]["text"])
    text += response["choices"][0]["text"]
    if not os.path.exists("Openai"):
        os.mkdir("Openai")

    # with open(f"Openai/prompt- {random.randint(1, 2343434356)}", "w") as f:
    with open(f"Openai/{''.join(prompt.split('intelligence')[1:]).strip()}.txt", "w") as f:
        f.write(text)


def say(text):
    speaker.Speak(text)


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source)
        try:
            print("Recognizing...")
            query = r.recognize_google(audio, language="en-in")
            print(f"User said: {query}")
            return query
        except Exception as e:
            return "Some Error Occurred. Sorry from Jarvis"


if __name__ == '__main__':
    m = sr.Microphone()
    print(m.list_working_microphones())
    print('Welcome to Anya A.I')
    say("Anya A.I")
    while True:
        print("Listening...")
        query = takeCommand()
        # todo: more sites
        sites = [
            ["youtube", "https://www.youtube.com"],
            ["wikipedia", "https://www.wikipedia.org"],
            ["google", "https://www.google.com"],
            ["facebook", "https://www.facebook.com"],
            ["amazon", "https://www.amazon.com"],
            ["twitter", "https://www.twitter.com"],
            ["instagram", "https://www.instagram.com"],
            ["reddit", "https://www.reddit.com"],
            ["linkedin", "https://www.linkedin.com"],
            ["netflix", "https://www.netflix.com"],
            ["stackoverflow", "https://www.stackoverflow.com"],
            ["yahoo", "https://www.yahoo.com"],
            ["github", "https://www.github.com"],
            ["pinterest", "https://www.pinterest.com"],
            ["wordpress", "https://www.wordpress.org"],
            ["adobe", "https://www.adobe.com"],
            ["cnn", "https://www.cnn.com"],
            ["flipkart", "https://www.flipkart.com"],
            ["hdfcbank", "https://www.hdfcbank.com"],
            ["icicibank", "https://www.icicibank.com"],
            ["snapdeal", "https://www.snapdeal.com"],
            ["bookmyshow", "https://www.bookmyshow.com"],
        ]

        for site in sites:
            if f"Open {site[0]}".lower() in query.lower():
                say(f"Opening {site[0]} sir...")
                webbrowser.open(site[1])

        # todo: play a specific song
        if "play music" in query:
            musicPath = r"C:\Users\aish1\Downloads\Dance_Monkey.mp3"
            os.system(f"start {musicPath}")

        elif "the time" in query:
            hour = datetime.datetime.now().strftime("%H")
            minutes = datetime.datetime.now().strftime("%M")
            say(f"Aish time is {hour} bajke {minutes} minutes")

        elif "open vscode".lower() in query.lower():
            os.system(f"code")
        elif "open word".lower() in query.lower():
            os.system("winword")
        elif "Using artificial intelligence".lower() in query.lower():
            ai(prompt=query)

        elif "Anya Quit".lower() in query.lower():
            exit()

        elif "reset chat".lower() in query.lower():
            chatStr = ""

        else:
            print("Chatting...")
            chat(query)

        # say(query)
