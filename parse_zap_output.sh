#!/bin/bash

# Check if at least the input source (program command or input file) is provided
if [ -z "$1" ]; then
    echo "Usage: $0 <evaluation command | input_file> [output_file]"
    exit 1
fi

INPUT_SOURCE="$1"
OUTPUT_FILE="${2:-avatar_zaps.csv}"

# associative arrays
declare -A zaps
declare -A zaps_hits
declare -A zaps_near_edible

process_input() {
    while IFS= read -r line
    do
        if [[ $line =~ avatar:\ ([0-9]+)\ zapped! ]]; then
            avatar_index=${BASH_REMATCH[1]}
            zaps[$avatar_index]=$(( ${zaps[$avatar_index]} + 1 ))
        elif [[ $line =~ avatar:\ ([0-9]+)\ zapped\ and\ hit! ]]; then
            avatar_index=${BASH_REMATCH[1]}
            zaps_hits[$avatar_index]=$(( ${zaps_hits[$avatar_index]} + 1 ))
        elif [[ $line =~ avatar:\ ([0-9]+)\ zapped\ near\ edible! ]]; then
            avatar_index=${BASH_REMATCH[1]}
            zaps_near_edible[$avatar_index]=$(( ${zaps_near_edible[$avatar_index]} + 1 ))
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

# CSV Header, easier than seperate columns for each avatar...
echo "Avatar,Avatar_zaps,Avatar_zaps_hits,Avatar_zaps_near_edible" > "$OUTPUT_FILE"

# need to identify unique keys, clean up by replacing front and end newlines with spaces, sort by unique 
all_keys=$(echo "${!zaps[@]} ${!zaps_hits[@]} ${!zaps_near_edible[@]}" | tr ' ' '\n' | sort -u | tr '\n' ' ')


# Write the counts to the CSV file
for avatar_index in $all_keys
do
    avatar_index=${avatar_index:-0}  # Default to 0 if undefined
    zaps_count=${zaps[$avatar_index]:-0}
    zaps_hits_count=${zaps_hits[$avatar_index]:-0}
    zaps_near_edible_count=${zaps_near_edible[$avatar_index]:-0}
    echo "Avatar_$avatar_index,$zaps_count,$zaps_hits_count,$zaps_near_edible_count" >> "$OUTPUT_FILE"
done

echo "Zap results have been written to $OUTPUT_FILE"
