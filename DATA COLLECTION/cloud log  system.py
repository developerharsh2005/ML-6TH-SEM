log_path = "/var/log/syslog"   # or /var/log/auth.log

with open(log_path, "r") as f:
    logs = f.readlines()

with open("system_logs.csv", "w") as f:
    for line in logs:
        f.write(line)

print("Logs exported to system_logs.csv")
