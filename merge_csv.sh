printf '%s\0' data/recent_changes/*.csv | xargs -0 cat > recent_changes.csv &&
printf '%s\0' data/allrevisions/*.csv | xargs -0 cat > allrevision.csv