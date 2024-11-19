 import os
 def main():
 pid =os.fork()
 if pid < 0:
 #Forkfailed
 print("Fork failed")
 elif pid == 0:
 #Child process
 print(f"Child process: PID = {os.getpid()}, Parent PID = {os.getppid()}")
 else:
 #Parentprocess
 print(f"Parent process: PID = {os.getpid()}, Child PID = {pid}")
 if __name__ == "__main__":
 main()
 