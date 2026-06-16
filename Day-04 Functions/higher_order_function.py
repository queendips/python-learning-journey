# A Higher-Order Function is a function that Accepts another function as an argument, or returns a function
def pizza():
    print("Preparing Pizza")

def burger():
    print("Preparing Burger")

def prepare_food(food):
    food()

prepare_food(pizza)
prepare_food(burger)

# Sending Email/sent

def send_email():
    print("Email Sent")

def send_sms():
    print("SMS Sent")

def notify(method):
    method()

notify(send_email)
notify(send_sms)