Write-Host "`n==================== PERSISTENCE: SCHEDULED TASKS ====================" -ForegroundColor Cyan

# Enumerate enabled scheduled tasks
# LOOK FOR:
#   - Random task names
#   - Tasks executing from user-writable paths
Get-ScheduledTask |
Where-Object { $_.State -ne "Disabled" } |
Select TaskName, TaskPath
