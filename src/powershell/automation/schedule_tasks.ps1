# Schedule Tasks Automation Script

# This script automates the scheduling of tasks related to report generation.
# It utilizes Windows Task Scheduler to create, modify, and delete scheduled tasks.

# Define the task name and script path
$taskName = "ProductReportGeneration"
$scriptPath = "C:\path\to\your\script\report_generator.py"

# Define the action to run the Python script
$action = New-ScheduledTaskAction -Execute "python" -Argument $scriptPath

# Define the trigger to run the task daily at a specific time
$trigger = New-ScheduledTaskTrigger -Daily -At "09:00AM"

# Define the principal (user) under which the task will run
$principal = New-ScheduledTaskPrincipal -UserId "SYSTEM" -LogonType ServiceAccount

# Register the scheduled task
Register-ScheduledTask -Action $action -Trigger $trigger -Principal $principal -TaskName $taskName -Description "Daily report generation task"

# Output the status
Write-Host "Scheduled task '$taskName' has been created successfully."