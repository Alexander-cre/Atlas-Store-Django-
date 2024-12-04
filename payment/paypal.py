# paypal.py

import paypalrestsdk

paypalrestsdk.configure({
    "mode": "sandbox",  # or "live" for production
    "client_id": "AWCccjeQoRxKDvxr6tYzC-psFHO1iR9GXz2YKX2CPAhgEJ3Ic1PLW-XaPK9V4kcxKSt46g5sKdiO_oA0",
    "client_secret": "EPJVQNOUelKT05U1Sah6uPWgCGi1S04P9ne1lxAAR5KR5592KPWXKYROihRJqbuo6alnEHsEdsHeDJH8"
})