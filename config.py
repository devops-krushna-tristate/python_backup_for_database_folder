mysql_user = 'root'
mysql_password = "securePassword"

backup_location  = "/home/tristate/Desktop/Learning/pyhton_projects_devops/"

backup_dirs = ["/var/www/html", "/etc"]

mysql_backup = True

clear_backups = False

date_format = "%Y_%m_%H_%M"

backup_name_format = "%date%-%backupNmae%"
