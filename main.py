import subprocess
from flask import Flask, stream_with_context, Response


app = Flask(__name__)

@app.route('/')
def stream():
    return Response(stream_with_context(get_stream()), mimetype='text/html; charset=utf-8')


def get_stream():
    p1 = subprocess.Popen(['python3', 'p1.py'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    p2 = subprocess.Popen(['python3', 'p2.py'], stdin=p1.stdout, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    while True:
        try:
            killIfError([p1, p2])
            buf = p2.stdout.read(1)
            if not buf:
                killIfError([p1, p2])
                print("stream complete!")
                return
            yield buf

        # p1 or p2 died, or user aborted
        except (GeneratorExit, Exception) as ex: 
            print('stream aborted')
            p1.terminate()
            p2.terminate()
            return


def killIfError(procs):
    for proc in procs:
        if proc.poll() not in (None, 0):
            for line in proc.stderr:
                print("stderr:" + line.decode(), end='')
            procs[0].terminate()
            procs[1].terminate()
            raise Exception("error occurred")


if __name__ == '__main__':
    app.run(host="localhost", port=80, debug=True)

