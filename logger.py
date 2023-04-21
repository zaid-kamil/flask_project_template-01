'''
This module is used to log the messages to the terminal/console.
'''
def log(*message):
    print('>>>' * 20)
    for m in message:
        print(f'-->{m}')
    print('<<<' * 20)