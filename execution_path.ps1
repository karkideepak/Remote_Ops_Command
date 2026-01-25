Get-ChildItem "$env:APPDATA","$env:TEMP" -Recurse `
-ErrorAction SilentlyContinue |
Where-Object {
    $_.LastWriteTime -gt (Get-Date).AddHours(-12)
} |
Select FullName, LastWriteTime
