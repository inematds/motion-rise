#!/bin/bash
cd ~/projetos/motion-rise
while IFS='|' read -r nome cena; do
  echo "$nome|$cena"
done < context/cenas.txt | xargs -P 4 -I{} bash -c 'n="${1%%|*}"; c="${1#*|}"; python3 ~/.claude/skills/formato-curso-v6/scripts/gerar-cena.py assets/img/$n.webp "$c" > context/cena-$n.log 2>&1; echo "$n exit $?"' _ {}
