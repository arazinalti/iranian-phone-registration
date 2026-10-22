# 📱 Phone Number Registration

A simple web application built with Python and Flask for registering and validating Iranian mobile phone numbers.

## How It Works

1. The user enters a mobile phone number.
2. The application normalizes Persian and Arabic digits and removes unnecessary spaces and symbols.
3. The phone number is validated against the Iranian mobile number format.
4. Valid numbers are stored in an SQLite database.
5. Duplicate registrations are rejected.

## Technology Stack

- **Python** — application logic
- **Flask** — web framework
- **SQLite** — database
- **HTML & CSS** — user interface

## Current Status

This is an early-stage project. It supports basic phone number validation and registration. Authentication, advanced security, and production deployment have not yet been implemented.

## Run Locally

```bash
python -m pip install flask
python app.py
```

Open `http://127.0.0.1:5000` in your browser.

## Limitations

The application checks the phone number's format, but it does not verify whether the number actually exists or belongs to the user. Additional security and validation are required before production use.

---

*An independent Python web development project.*
