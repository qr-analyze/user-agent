const userAgent = window.navigator.userAgent.toLowerCase();
if (userAgent.includes("iphone") || userAgent.includes("ipad")) {
    window.location.href = "https://apps.apple.com/sa/app/maheer-customer/id6499317335"; // Replace with your Apple App Store link
} else if (userAgent.includes("android")) {
    window.location.href = "https://play.google.com/store/apps/details?id=com.maheer.customerApp"; // Replace with your Google Play Store link
} else {
    console.log("Unsupported device");
}
