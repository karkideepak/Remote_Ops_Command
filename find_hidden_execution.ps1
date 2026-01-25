
Write-Host "`n==================== PROCESS INVESTIGATION ====================" -ForegroundColor Cyan

# Enumerate running processes with full command-line context
# WHY:
#   - SentinelOne storylines often flag suspicious process trees
#   - CommandLine reveals encoded payloads, LOLbins, or script abuse
Get-CimInstance Win32_Process |
Select-Object `
    Name,
    ProcessId,
    ParentProcessId,
    CommandLine |
Sort-Object Name
