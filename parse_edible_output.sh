#!/bin/bash

# Check if at least the input source (program command or input file) is provided
if [ -z "$1" ]; then
    echo "Usage: $0 <evaluation command | input_file> [output_file]"
    exit 1
fi

INPUT_SOURCE="$1"
OUTPUT_FILE="${2:-avatar_apple_consumption.csv}"

# associative array
declare -A avatar_counts

process_input() {
    # internal field seperator, line by line
    while IFS= read -r line; do
        if [[ $line =~ Avatar\ ([0-9]+)\ consumed\ apple! ]]; then
            avatar_index="${BASH_REMATCH[1]}"
            ((avatar_counts[$avatar_index]++))
        fi
    done
}

# file or a command
if [[ -f "$INPUT_SOURCE" ]]; then
    # from file
    process_input < "$INPUT_SOURCE"
else
  # from STDOUT
  $INPUT_SOURCE | process_input
fi

echo "Avatar,Count" > "$OUTPUT_FILE"
for avatar in "${!avatar_counts[@]}"; do
    echo "$avatar,${avatar_counts[$avatar]}" >> "$OUTPUT_FILE"
done

echo "Results have been written to $OUTPUT_FILE"
