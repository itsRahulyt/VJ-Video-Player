import subprocess
import os

def mkv_to_mp4(input_path, output_path):
    if os.path.exists(output_path):
        return output_path  # already converted

    cmd = [
        "ffmpeg",
        "-y",
        "-i", input_path,
        "-map", "0",
        "-c:v", "copy",
        "-c:a", "aac",
        "-movflags", "+faststart",
        output_path
    ]

    subprocess.run(cmd, check=True)
    return output_path
