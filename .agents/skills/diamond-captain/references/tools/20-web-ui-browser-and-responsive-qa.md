# 20. Web UI, browser and responsive QA

Choose when a web deliverable needs observed behavior, layout or regression evidence. Record actual environment, steps, assertions and captured results; a script that exists but was not run is not a pass.

| Candidate | When to consider it | Route to check |
| --- | --- | --- |
| [Playwright](https://playwright.dev/) | Repeatable user flows across supported browser engines | L / F |
| [Cypress](https://www.cypress.io/) | UI/component checks in an existing Cypress project | L / F |
| [Selenium](https://www.selenium.dev/) | Existing WebDriver automation or browser infrastructure | L / F |
| [WebdriverIO](https://webdriver.io/) | Existing web/mobile automation using supported drivers | L / F |
| [Puppeteer](https://pptr.dev/) | Scripted browser inspection or focused automation | L / F |
| [Chrome DevTools](https://developer.chrome.com/docs/devtools/) | Inspect DOM, network, performance and rendered states | B |
| [Safari Web Inspector](https://developer.apple.com/safari/tools/) | Inspect actual Safari or supported Apple-device behavior | B |
| [Firefox DevTools](https://firefox-source-docs.mozilla.org/devtools-user/) | Inspect Firefox-specific layout or behavior issues | B |
| [BrowserStack](https://www.browserstack.com/) | Authorized access to a broader browser/device matrix | B |
| [Sauce Labs](https://saucelabs.com/) | Existing hosted cross-browser test infrastructure | B |

Apply the target site's own QA/telemetry exclusion instructions **before the first document load** when they exist. No query parameter is a universal telemetry opt-out.

Use the [shared routing, capability limits and permissions](../tool-options.md#read-only-what-the-next-decision-needs) before acting.
