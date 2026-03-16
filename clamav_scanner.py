import subprocess

def scan_file(file_path):
    try:
        result = subprocess.run(
            ["clamscan", file_path],
            capture_output=True,
            text=True
        )

        if "FOUND" in result.stdout:
            return True, result.stdout
        else:
            return False, result.stdout

    except Exception as e:
        return False, str(e)
