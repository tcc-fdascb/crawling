from selenium import webdriver
from axe_selenium_python import Axe

def test_google():
    driver = webdriver.Firefox()
    driver.get("http://www.google.com")
    axe = Axe(driver)
    # Inject axe-core javascript into page.
    axe.inject()
    # Run axe accessibility checks.
    results = axe.run()
    # Write results to file
    axe.write_results(results, 'a11y.json')
    driver.close()
    # Assert no violations are found
    assert len(results["violations"]) == 0, axe.report(results["violations"])

test_google()
