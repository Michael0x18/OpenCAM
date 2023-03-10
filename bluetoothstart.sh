#!/bin/bash

rfkill block bluetooth
rfkill unblock bluetooth
bluetoothctl power on
