"""One-time script to create test users for manual feature review. Delete after use."""
import django
django.setup()

from aplx_ams_django.accounts.models import User  # noqa: E402

# DB role values from accounts/models.py ROLE_CHOICES (model not yet updated by SCR S-17)
# l2l3_support in API spec / frontend, but DB constraint enforces l2_l3_support_engineer
USERS = [
    {"username": "dm_test",      "name": "DM Test",      "role": "delivery_manager",      "email": "dm@test.local",   "client_org": None},
    {"username": "l2l3_test",    "name": "L2L3 Test",    "role": "l2_l3_support_engineer","email": "l2l3@test.local", "client_org": None},
]
PASSWORD = "Test1234!"

for data in USERS:
    user, created = User.objects.get_or_create(
        username=data["username"],
        defaults={
            "name": data["name"],
            "email": data["email"],
            "role": data["role"],
            "is_active": True,
            "failed_attempts": 0,
            "client_org": data["client_org"],
        },
    )
    user.set_password(PASSWORD)
    user.is_active = True
    user.failed_attempts = 0
    user.locked_until = None
    user.save()
    print(f"{'Created' if created else 'Reset'}: {user.username} / {PASSWORD}  (role: {user.role})")
