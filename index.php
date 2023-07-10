<?php
$acceptedStrings = [
    '', 
    ''
];

$blacklistedIPs = [
    '10.0.0.1'
];

$providedString = $_GET['string'] ?? '';
$clientIP = $_SERVER['REMOTE_ADDR'];

if (in_array($clientIP, $blacklistedIPs)) {
    echo 'BLOCKED - IP is blacklisted';
    exit;
}

if (in_array($providedString, $acceptedStrings)) {
    if ($providedString === '') {
        echo 'Ok - Normal authenticate';
    } elseif ($providedString === '') {
        echo 'Ok - Admin authenticate';
    }
} else {
    echo 'Not ok';
}

echo "\nClient IP: " . $clientIP;
?>