# IO-Manager
The project makes use of python library pyFirmata to control arduino pins explicitly. It removes the need of uploading arduino code each time a change is made.

## The following packages have to be installed for the [script][script] to work 
- To install the libaries into your project. Run the following commands in your terminal window:-
```
pip install pyFirmata
```
```
pip install tk
```
```
pip install pyftpdlib
```
> ### Some of the other libraries come with python
> **Note** 
> I'm using Python 3.9 

## Arduino Setup
- Use the StandardFirmata example provided after installing firmata on Arduino IDE or download from [here][arduinocode]

```python
    # disable upload to the web - remove return to enable this feature
    return
    try:
        session = ftplib.FTP('ftp-server-name', 'username', 'your-password')
        file = open('pins.json', 'rb')  # file to send
        session.storbinary('STOR htdocs/python-pins/pins.json', file)  # send the file
        file.close()  # close file and FTP
        session.quit()
        max_label.config(text="***SUCCESSFULLY UPLOADED***")
        max_label.place(x=(width / 2) - int((len(max_label.cget("text")) * 4)), y=height - 53)
    except:
        max_label.place(x=(width / 2) - int((len(max_label.cget("text")) * 4)), y=height - 53)
```


[script]: pins.py
[arduinocode]: StandardFirmata.ino
