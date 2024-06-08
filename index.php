$userAgent = strtolower($_SERVER['HTTP_USER_AGENT']);
if (strpos($userAgent, 'iphone') !== false || strpos($userAgent, 'ipad') !== false) {
    header('Location: https://apps.apple.com/sa/app/maheer-customer/id6499317335');
    exit; // Stop further execution
} elseif (strpos($userAgent, 'android') !== false) {
    header('Location: https://play.google.com/store/apps/details?id=com.maheer.customerApp');
    exit; 
} else {
    echo "Unsupported device";
}
