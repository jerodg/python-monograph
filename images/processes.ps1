# Define the drive letter
$driveLetter = "D:"

# Get all processes
$processes = Get-WmiObject Win32_Process | Select-Object Name, CommandLine

# Filter processes running from the specified drive
$processesOnDriveD = $processes | Where-Object { $_.CommandLine -like "$driveLetter*" }

# Display the filtered processes
$processesOnDriveD
