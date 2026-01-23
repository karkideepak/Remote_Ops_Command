# Attempt to retrieve the target process by name.
# -ErrorAction SilentlyContinue prevents noisy errors if the process does not exist.
$process = Get-Process -Name "malware" -ErrorAction SilentlyContinue

# If the process is found, forcefully terminate it.
# This avoids unnecessary failures and makes the action idempotent.
if ($process) {
    Stop-Process -InputObject $process -Force
}
