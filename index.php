<?php
$acceptedStrings = [
    'AipgnLUbcCGLxfum4V', 
    '6N0wLHdSy0wha55DrM'
];

$providedString = $_GET['string'] ?? '';

if (in_array($providedString, $acceptedStrings)) {
    if ($providedString === 'YourNormalString') {
        echo 'Ok - Normal authenticate';
    } elseif ($providedString === 'YourAdminString') {
        echo 'Reset - Admin reset';
    }
} else {
    echo 'You do not have access - Contact Mathias Ramlov';
}
?>