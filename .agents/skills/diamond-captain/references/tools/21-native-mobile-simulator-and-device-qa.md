# 21. Native mobile, simulator and device QA

Choose when the deliverable runs in a native mobile environment. Simulator/emulator evidence does not prove real-device behavior, and account/device-cloud use may require budget and upload authorization.

| Candidate | When to consider it | Route to check |
| --- | --- | --- |
| [Xcode Simulator](https://developer.apple.com/documentation/xcode/running-your-app-on-simulated-or-physical-devices) | Inspect an iOS app in available simulator environments | L / F |
| [Android Emulator](https://developer.android.com/studio/run/emulator) | Inspect an Android app on configurable virtual devices | L / F |
| [Maestro](https://docs.maestro.dev/) | Describe and run repeatable mobile UI flows | L / F |
| [Appium](https://appium.io/docs/en/latest/) | Cross-platform mobile automation with installed drivers | L / F |
| [Espresso](https://developer.android.com/training/testing/espresso) | Android UI checks in an existing test project | L / F |
| [XCTest](https://developer.apple.com/documentation/xctest) | Apple-platform UI/behavior checks in existing projects | L / F |
| [Firebase Test Lab](https://firebase.google.com/products/test-lab) | Authorized device-lab coverage for supported app builds | B |
| [BrowserStack App Automate](https://www.browserstack.com/app-automate) | Run existing app automation on hosted real devices | B |
| [Sauce Labs mobile testing](https://saucelabs.com/products/mobile-testing) | Existing hosted mobile device/testing program | B |
| [Detox](https://wix.github.io/Detox/) | React Native end-to-end tests in an existing setup | L / F |

Use the [shared routing, capability limits and permissions](../tool-options.md#read-only-what-the-next-decision-needs) before acting.
