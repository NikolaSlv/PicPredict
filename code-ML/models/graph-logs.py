import subprocess

# Define the TensorBoard command
command = "tensorboard --logdir=logs-best/ --host localhost --port 8088"

# Use subprocess to execute the shell command
process = subprocess.Popen(command, shell=True)
process.wait()
