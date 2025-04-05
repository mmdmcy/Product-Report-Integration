# Stakeholder Alerts Script

# This script sends alerts to stakeholders regarding report availability and updates.

function Send-StakeholderAlert {
    param (
        [string]$stakeholderEmail,
        [string]$reportName,
        [string]$reportLink,
        [string]$message
    )

    $subject = "Report Update: $reportName"
    $body = @"
Hello,

This is to inform you that the report '$reportName' is now available for your review. You can access it using the following link:

$reportLink

$message

Best regards,
Your Reporting Team
"@

    # Send email (assuming Send-MailMessage is configured)
    Send-MailMessage -To $stakeholderEmail -Subject $subject -Body $body -SmtpServer "smtp.yourdomain.com"
}

# Example usage
$stakeholderEmail = "stakeholder@example.com"
$reportName = "Monthly Sales Report"
$reportLink = "http://reports.yourdomain.com/monthly-sales-report"
$message = "Please review the report at your earliest convenience."

Send-StakeholderAlert -stakeholderEmail $stakeholderEmail -reportName $reportName -reportLink $reportLink -message $message