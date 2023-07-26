#!/bin/bash

if [ $# -ne 1 ]; then
  echo "Usage: $0 <dot_file_name>"
  exit 1
fi

DOT_FILE="$1"
BASE_NAME=$(basename "$DOT_FILE" .dot)
PNG_FILE="$BASE_NAME.png"

dot -Tpng "$DOT_FILE" -o "$PNG_FILE"

echo "Generated PNG file: $PNG_FILE"
