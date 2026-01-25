Write-Host "`n==================== PERSISTENCE: REGISTRY RUN KEYS ====================" -ForegroundColor Cyan

# Check common startup persistence locations
# WHY:
#   - Malware frequently registers itself for execution on logon
Get-ItemProperty `
"HKLM:\Software\Microsoft\Windows\CurrentVersion\Run",
"HKCU:\Software\Microsoft\Windows\CurrentVersion\Run" `
-ErrorAction SilentlyContinue
