from flask import Flask, request, redirect

app = Flask(__name__)


@app.route("/")
def index():
    user_agent = request.headers.get("User-Agent").lower()
    if "iphone" in user_agent or "ipad" in user_agent:
        return redirect(
            "https://apps.apple.com/sa/app/maheer-customer/id6499317335"
        )  # Replace with your Apple App Store link
    elif "android" in user_agent:
        return redirect(
            "https://play.google.com/store/apps/details?id=com.maheer.customerApp"
        )  # Replace with your Google Play Store link
    else:
        return "Unsupported device"


if __name__ == "__main__":
    app.run(debug=True)
