def get_browser_logs(driver):

    # Retrieve the browser's console log
    logs = driver.get_log("browser")

    # Iterate through the console log entries
    for log_entry in logs:
        print(log_entry)
