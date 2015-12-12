import sys

class _Getch:
            """Gets a single character from standard input.  Does not echo to the
            screen."""
            def __init__(self):
                        try:
                                    self.impl = _GetchWindows()
                        except ImportError:
                                    self.impl = _GetchUnix()
                        
            def __call__(self): return self.impl()

class _GetchUnix:
            def __init__(self):
                        import tty, sys
                
            def __call__(self):
                        import sys, tty, termios
                        fd = sys.stdin.fileno()
                        old_settings = termios.tcgetattr(fd)
                        try:
                                    tty.setraw(sys.stdin.fileno())
                                    ch = sys.stdin.read(1)
                        finally:
                                    termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
                        return ch
                
class _GetchWindows:
            def __init__(self):
                        import msvcrt
                
            def __call__(self):
                        import msvcrt
                        return msvcrt.getch()
        
getch = _Getch()
                        
def getpass(prompt='Password: ', stream=None):
        """Prompt for password with echo off, replacing by *"""
        for c in prompt:
                sys.stdout.write(c)
        pw = ""
        while 1:
                c = getch()
                if c == '\r' or c == '\n':
                        break
                if c == '\003':
                        raise KeyboardInterrupt
                if ord(c) == 127:
                        pw = pw[:-1]
                        sys.stdout.write('\b \b')
                        sys.stdout.flush()
                else:
                        pw = pw + c
                        sys.stdout.write('*')
        sys.stdout.write('\b')
        sys.stdout.write('\r')
        sys.stdout.write('\n')
        return pw

def query_yes_no(question, default="yes"):
        """Ask a yes/no question via raw_input() and return their answer.
        
        "question" is a string that is presented to the user.
        "default" is the presumed answer if the user just hits <Enter>.
        It must be "yes" (the default), "no" or None (meaning
        an answer is required of the user).
        
        The "answer" return value is True for "yes" or False for "no".
        """
        valid = {"yes": True, "y": True, "ye": True,
                      "no": False, "n": False}
        if default is None:
                prompt = " [y/n]: "
        elif default == "yes":
                prompt = " [Y/n]: "
        elif default == "no":
                prompt = " [y/N]: "
        else:
                raise ValueError("invalid default answer: '%s'" % default)
    
        while True:
                sys.stdout.write(question + prompt)
                choice = raw_input().lower()
                if default is not None and choice == '':
                        return valid[default]
                elif choice in valid:
                        return valid[choice]
                else:
                    sys.stdout.write("Please respond with 'yes' or 'no' "
                                     "(or 'y' or 'n').\n")

def query_multiple(question, validchoice, default=[], mult=False):

        prompt = '[' + ', '.join(validchoice) + ']'
        if mult is True:
                if default is not None:
                        prompt += "(default:" + ','.join(default) + ") "
                prompt += " separate choice by ',': "
        elif default is not None:
                prompt += "(default:" + default[0] + "): "
        else:
                prompt += ": "
                
        while True:
                sys.stdout.write(question + prompt)
                choice = raw_input()
                if mult is False or ',' in choice:
                        if default is not None and choice == '':
                                return default[0]
                        if choice in validchoice:
                                return choice
                        else:
                                sys.stdout.write("Please respond with " + prompt + ".\n")
                else:
                        res = []
                        if default is not None and choice == "":
                                return default
                        for onechoice in choice.split(","):
                                if onechoice in validchoice:
                                        res.append(choice)
                                else:
                                        sys.stdout.write("Please respond with " + prompt + ".\n")
                                        res = []
                                        break
                        if res is not []:
                                return res

def query(question, password=False, default=None):
            if default is not None:
                        question += "(default:" + default + ")"
            while 42:
                        if password:
                                    choice = getpass(question + ": ")
                        else:
                                    sys.stdout.write(question + ": ")
                                    choice = raw_input()
                        if default is not None and choice == "":
                                    return default
                        if choice != "":
                                    return choice
                        else:
                                    sys.stdout.write("Please enter an " + question + ".\n")
