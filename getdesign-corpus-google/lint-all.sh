#!/bin/zsh
# Lint every brand file in this directory and produce a compact summary
cd "$(dirname "$0")"
RESULTS_FILE=lint-results.tsv
echo "file\terrors\twarnings\tinfos" > "$RESULTS_FILE"

total=0
fails=0
for f in *.md; do
  # skip non-brand files
  [[ "$f" == "CONVERSION_REPORT.md" ]] && continue
  total=$((total + 1))

  result=$(npx -y @google/design.md lint "$f" 2>&1)
  errs=$(echo "$result" | grep -oE '"errors": *[0-9]+' | grep -oE '[0-9]+' | head -1)
  warns=$(echo "$result" | grep -oE '"warnings": *[0-9]+' | grep -oE '[0-9]+' | head -1)
  infos=$(echo "$result" | grep -oE '"infos": *[0-9]+' | grep -oE '[0-9]+' | head -1)

  errs=${errs:-?}
  warns=${warns:-?}
  infos=${infos:-?}

  echo "$f\t$errs\t$warns\t$infos" >> "$RESULTS_FILE"

  if [[ "$errs" != "0" ]]; then
    fails=$((fails + 1))
    echo "FAIL: $f ($errs errors)"
  fi
done

echo ""
echo "=== Summary ==="
echo "Total files: $total"
echo "Pass (0 errors): $((total - fails))"
echo "Fail (>0 errors): $fails"
echo ""
echo "Results saved to $RESULTS_FILE"
