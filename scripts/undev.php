<?php
/**
 * Reset the dev settings to their defaults.
 * See dev.php
 */

define('CLI_SCRIPT', true);
require(dirname(__FILE__).'/config.php');
require_once($CFG->libdir . '/adminlib.php');

function mdk_set_config($name, $value) {
    set_config($name, $value);
    $value = is_bool($value) ? (int) $value : $value;
    mtrace("Setting $name to $value");
}

// Load all the settings.
session_set_user(get_admin());
$adminroot = admin_get_root();


// Debugging settings.
$settingspage = $adminroot->locate('debugging', true);
$settings = $settingspage->settings;

// Set developer level.
$default = $settings->debug->get_defaultsetting();
mdk_set_config('debug', $default);

// Display debug messages.
$default = $settings->debugdisplay->get_defaultsetting();
mdk_set_config('debugdisplay', $default);

// Debug the performance.
$default = $settings->perfdebug->get_defaultsetting();
mdk_set_config('perfdebug', $default);

// Debug the information of the page.
$default = $settings->debugpageinfo->get_defaultsetting();
mdk_set_config('debugpageinfo', $default);


// Site policies settings.
$settingspage = $adminroot->locate('sitepolicies', true);
$settings = $settingspage->settings;

// Any kind of password is allowed.
$default = $settings->passwordpolicy->get_defaultsetting();
mdk_set_config('passwordpolicy', $default);


// Theme settings.
$settingspage = $adminroot->locate('themesettings', true);
$settings = $settingspage->settings;

// Allow themes to be changed from the URL.
$default = $settings->allowthemechangeonurl->get_defaultsetting();
mdk_set_config('allowthemechangeonurl', $default);


// Javascript settings.
$settingspage = $adminroot->locate('ajax', true);
$settings = $settingspage->settings;

// Do not cache JavaScript.
$default = $settings->cachejs->get_defaultsetting();
mdk_set_config('cachejs', $default);

// Do not use YUI combo loading.
$default = $settings->yuicomboloading->get_defaultsetting();
mdk_set_config('yuicomboloading', $default);