# Get logins from the last 24 hours
$startTime = (Get-Date).AddHours(-24)

# Fetch Security log events (Event ID 4624 = Successful Logon)
$events = Get-WinEvent -FilterHashtable @{
    LogName = 'Security'
    Id      = 4624
    StartTime = $startTime
}

$results = foreach ($event in $events) {

    $xml = [xml]$event.ToXml()
    $eventData = $xml.Event.EventData.Data

    $logonType = ($eventData | Where-Object { $_.Name -eq "LogonType" }).'#text'
    $targetUser = ($eventData | Where-Object { $_.Name -eq "TargetUserName" }).'#text'
    $targetDomain = ($eventData | Where-Object { $_.Name -eq "TargetDomainName" }).'#text'
    $ipAddress = ($eventData | Where-Object { $_.Name -eq "IpAddress" }).'#text'

    # Filter for interactive logins only
    if ($logonType -in 2,7,10 -and 
        $targetUser -notmatch "SYSTEM|LOCAL SERVICE|NETWORK SERVICE|ANONYMOUS LOGON") {

        [PSCustomObject]@{
            TimeCreated = $event.TimeCreated
            User        = "$targetDomain\$targetUser"
            LogonType   = $logonType
