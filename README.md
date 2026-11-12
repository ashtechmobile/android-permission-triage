# Android Permission Triage

**Ashique Meethale Purayil** · Simulated mobile security case

## Scenario

A phone repair customer asks for help reviewing a calculator app installed from a browser download. This exercise compares two fictional apps against the permissions expected for their stated functions.

## Findings

| App | Evidence | Review result |
| --- | --- | --- |
| Pocket Calculator | Contacts and Microphone were granted. The download source is unverified. | Review recommended |
| Voice Recorder | Microphone access matches its stated function. The source is verified in this exercise. | Within sample baseline |

## Triage decision

Review the calculator first. Confirm the app's identity and installation source with the device owner. Check whether the granted permissions are needed before recommending changes.

## Run the review

From the repository folder, run `python3 triage.py`. The script prints the review result and the reasons for each flagged app. [Open the Python script](triage.py)
