"""Review simulated Android app permissions against a sample baseline."""

apps = [
    {
        "name": "Pocket Calculator",
        "install_source": "Browser download",
        "source_verified": False,
        "expected_permissions": set(),
        "granted_permissions": {"Contacts", "Microphone"},
    },
    {
        "name": "Voice Recorder",
        "install_source": "Approved store",
        "source_verified": True,
        "expected_permissions": {"Microphone"},
        "granted_permissions": {"Microphone"},
    },
]

for app in apps:
    unexpected = sorted(app["granted_permissions"] - app["expected_permissions"])
    needs_review = bool(unexpected) or not app["source_verified"]
    status = "Review recommended" if needs_review else "Within sample baseline"
    print(f"{app['name']} - {status}")
    if unexpected:
        print("  Unexpected grants - " + ", ".join(unexpected))
    if not app["source_verified"]:
        print("  Unverified install source - " + app["install_source"])
