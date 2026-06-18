servers = ["web-server", "app-server", "db-server"]
backup_servers = servers.copy()
servers.append("kong-server")
print("Original_servers:", servers)
print("Backup:", backup_servers)