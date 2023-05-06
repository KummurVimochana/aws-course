# import tkinter as tk
# import boto3
# import os
# import sys
# from tempfile import gettempdir
# from contextlib import closing

# root = tk.Tk()
# root.geometry("400x400")
# root.title("AMAZON POLLY GUI")

# text_area = tk.Text(root,height=25)
# text_area.pack()

# def getText():
#     aws_mang_con = boto3.session.Session(profile_name='mini_project')
#     client = aws_mang_con.client(service_name = 'polly',region_name = 'us-east-1')
#     result = text_area.get("1.0","end")
#     print(result)
#     response = client.synthesize_speech(VoiceId = 'Joanna',OutputFormat='mp3',Text=result,Engine = 'neural')
#     print(response)
#     if "AudioStream" in response:
#         with closing(response['AudioStream']) as stream:
#             output = os.path.join(gettempdir(),"speech.mp3")
#             try:
#                 with open(output , 'wb')as file:
#                     file.write(stream.read())
#             except IOError as error:
#                 print(error)
#                 sys.exit(-1)
#     else:
#         print('Can not open the audio file')
#         sys.exit(-1)
#     # if sys.platform== 'win32':
#     #     os.system(output)

#     # if sys.platform == 'darwin':
#     #     os.system(output)

#     def open_file(output):
#         if sys.platform == "win32":
#             os.startfile(output)

# buttontoRead = tk.Button(root,height=1,width=10,text="Read",command=getText)
# buttontoRead.pack()

# root.mainloop()


import tkinter as tk
import boto3
import os
import sys
from tempfile import gettempdir
from contextlib import closing

root = tk.Tk()
root.geometry("400x400")
root.title("AMAZON POLLY GUI")

text_area = tk.Text(root, height=25)
text_area.pack()

def getText():
    aws_mang_con = boto3.session.Session(profile_name='mini_project')
    client = aws_mang_con.client(service_name='polly', region_name='us-east-1')
    result = text_area.get("1.0", "end")
    print(result)
    response = client.synthesize_speech(VoiceId='Joanna', OutputFormat='mp3', Text=result, Engine='neural')
    print(response)
    if "AudioStream" in response:
        with closing(response['AudioStream']) as stream:
            output = os.path.join(gettempdir(), "speech.mp3")
            try:
                with open(output, 'wb') as file:
                    file.write(stream.read())
            except IOError as error:
                print(error)
                sys.exit(-1)
    else:
        print('Can not open the audio file')
        sys.exit(-1)

    # Open the output file using the appropriate command
    open_file(output)

def open_file(output):
    if sys.platform == "darwin":
        os.system("open " + output)
    elif sys.platform == "win32":
        os.startfile(output)

buttontoRead = tk.Button(root, height=1, width=10, text="Read", command=getText)
buttontoRead.pack()

root.mainloop()
