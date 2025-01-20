#!/bin/bash

# Clear .log files
find . -type f -name "*.log" -exec rm -f {} +

# Clear directories
clear_directory() {
    find . -type d -name "$1" -exec rm -rf {} +
}

clear_directory "__pycache__"
clear_directory ".pytest_cache"
clear_directory "build"
clear_directory "dist"
clear_directory "light-oled/build"
clear_directory "light-oled/dist"

echo "Cleanup complete!"
