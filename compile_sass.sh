#!/bin/bash

cwd=$(pwd)
dir_name=$(basename "$cwd")

if [ "$dir_name" = "squidalytics.ink" ]; then
    base_path="squidalytics/static/"
else
    base_path="static/"
fi

# Path to the SCSS file
input="$base_path/scss/main.scss"

# Path to the output CSS file
output="$base_path/css/main.css"

# Compile the SCSS to CSS
sass $input $output
