#!/usr/bin/env python3

import webview

def process_data(params):
    # Handle data here
    problem = params['problem']
    issues = params['issues']

    print("Problem:", problem)
    print("Issues:", issues)

    # Process and return any result if needed
    return "Data processed"

api_methods = {
    'process_data': process_data
}

window = webview.create_window('Bulletproof Problem Solving', 'index.html', js_api=api_methods)
webview.start()

