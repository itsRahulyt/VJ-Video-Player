import subprocess

try:
    result = subprocess.run(
        ["ffmpeg", "-version"],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True
    )
    print("FFmpeg found:")
    print(result.stdout.splitlines()[0])
except FileNotFoundError:
    print("FFmpeg NOT found")
