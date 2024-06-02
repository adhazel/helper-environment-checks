import subprocess  
  
def run_script_in_venv():  
    python_exe = ".\\.venv\\Scripts\\python.exe"  
    script_name = ".\\vscode_python\\python-test.py"  
    subprocess.call([python_exe, script_name])  
  
run_script_in_venv()  