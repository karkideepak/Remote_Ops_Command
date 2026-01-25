Write-Host "`n==================== LOCAL ADMINISTRATORS ====================" -ForegroundColor Cyan

# Enumerate local admin group membership
# LOOK FOR:
#   - Unexpected users or service accounts
Get-LocalGroupMember Administrators
