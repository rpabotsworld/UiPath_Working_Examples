Param
(
[Parameter(Mandatory=$true)] [string]$ProcessCount
)

ps | sort -p ws | select -last $ProcessCount | "Sample.txt"