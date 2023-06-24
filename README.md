# flask-pipe-stream

This flask webserver demonstrates how to call a process, pipe its output to another process, then stream the output of the second process to a web browser.

## Run it

Call the main script:
```
python3 main.py
```

Then navigate to http://localhost/

## Design
When a request to http://localhost/ is received, the main script will call a process, `p1.py` which will output the alphabet in lowercase to stdout. This output will be piped to another process, `p2.py`, which will convert its stdin to uppercase and output to stdout. This output is then streamed to the browser.

Both processes p1.py and p2.py will randomly cause an error to show that the main script and correctly process errors and recieve stderr messages.
In the event the user cancels the stream from the browser, the main script will detect this and terminate processes p1.py and p2.py.
