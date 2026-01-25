Write-Host "`n==================== SUSPICIOUS POWERSHELL EXECUTION ====================" -ForegroundColor Cyan

# Identify PowerShell executions commonly abused by attackers
# LOOK FOR:
#   - EncodedCommand
#   - ExecutionPolicy Bypass
#   - Hidden windows
Get-CimInstance Win32_Process |
Where-Object {
    $_.CommandLine -match "encodedcommand|bypass|hidden"
} |
Select Name, ProcessId, CommandLine
