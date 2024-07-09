"""
Made by Sabaru
discord : s4b4ru
"""
print("""                                                                                           
                                            WEEBHOOK SPAMMER 
""")

#imports
from dhooks import Webhook
import time

#prompts
message = input("What do you want to spam?: ")
webhookurl = Webhook(input("Enter webhook: "))
delay = int(input("delay: "))

#webhook spamming time
while True:
    time.sleep(delay)
    webhookurl.send(message)
    print("Done.")
