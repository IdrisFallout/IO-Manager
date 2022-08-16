# IO-Manager
The project makes use of python library pyFirmata to control arduino pins explicitly. It removes the need of uploading arduino code each time a change is made.

## The following packages have work for the [script][script] to work 
```
pip install pyFirmata
```
```python
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
