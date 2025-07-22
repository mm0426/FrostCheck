# SMS Gateway Setup Instructions

## Changes Made
The application has been updated to send SMS messages via email-to-SMS gateway instead of Telegram.

## Required Environment Variables

Update your `.env` file with the following variables:

### Email Configuration
- `EMAIL_ADDRESS`: Your email address (e.g., your Gmail address)
- `EMAIL_PASSWORD`: Your email app password (for Gmail, generate an app-specific password)
- `SMTP_SERVER`: SMTP server (e.g., smtp.gmail.com for Gmail)
- `SMTP_PORT`: SMTP port (587 for most providers)

### SMS Gateway Configuration
- `SMS_EMAIL`: The SMS gateway email for your phone number

## Common SMS Gateway Formats

| Carrier | SMS Gateway Format |
|---------|-------------------|
| AT&T | `1234567890@txt.att.net` |
| Verizon | `1234567890@vtext.com` |
| T-Mobile | `1234567890@tmomail.net` |
| Sprint | `1234567890@messaging.sprintpcs.com` |

Replace `1234567890` with your actual phone number.

## Gmail Setup
1. Enable 2-factor authentication on your Gmail account
2. Generate an app-specific password in your Google Account settings
3. Use this app password (not your regular password) for `EMAIL_PASSWORD`

## Testing
Run the script to test if SMS messages are being sent properly. Check your phone for text messages.
