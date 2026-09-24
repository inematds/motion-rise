# Estilo 02 — Lousa documental com paquímetro

- **Visual:** explicativo de documentário: uma lousa de carvão borrada, grotesca branca pesada, paquímetro amarelo de medida, um traço laranja cursivo.
- **Movimento:** as barras sobem uma por batida, um paquímetro amarelo mede a mais alta, o número salta, um traço sublinha uma palavra, corte seco.

**Cinco regras:** (1) só dois tamanhos de tipo: rótulo e número 2,6× maior; (2) Title Case, grotesca pesada, branca — nunca caixa-alta, nunca texto colorido; (3) o paquímetro cobre exatamente a altura que mede e aparece antes do número; (4) o número salta 80 ms depois do colchete: 0,85 → 1, sem fade; (5) laranja só como traço: um sublinhado cursivo sob uma palavra do título, uma vez.

```
R — REFERÊNCIAS
• Explicativos de documentário em estilo "lousa": campo de lousa de carvão, tipografia grotesca pesada branca, colchetes de medida amarelos.
• Pranchas de guia de campo: um assunto, um fato medido.
• Pegue a gramática visual, nunca a marca de nenhum canal.

I — IDEIA
Uma imagem com início, meio e fim, 5 segundos, em loop com corte seco:
• Início (0–1,4 s): o título "Design Em Movimento" está numa lousa de carvão borrada; uma linha de base se desenha e três barras sobem, uma por batida.
• Meio (1,4–3,1 s): um paquímetro amarelo mede a barra mais alta, depois o número "3×" salta ao lado; um traço cursivo laranja sublinha uma palavra do título.
• Fim (3,1–5 s): uma pausa parada de pelo menos 1,5 s, depois um corte seco de um frame de volta ao título sozinho.

S — ESTILO
Visual: lousa de carvão #0d0d0d com manchas de giz e poeira, texto #f4f1ea em Plus Jakarta Sans ExtraBold em Title Case, barras com preenchimento translúcido #f4f1ea e contorno de 2 px #f4f1ea, um paquímetro #f5e918, um traço #f0862b.
Movimento: cada construção dura 300–450 ms em quint-out, uma por batida, depois congela. O paquímetro se desenha em 400 ms, o número salta 80 ms depois (0,85 → 1, outBack, sem fade). O traço se desenha em 450 ms. A prancha avança até 1,05 de zoom ao longo da cena.
Regras:
1. Só dois tamanhos de tipo; o número é 2,6× o rótulo.
2. O paquímetro cobre exatamente a altura total da barra, com os ticks voltados para a barra e a aba voltada para o número.
3. Destaques são só traços, abaixo de 0,5% do quadro cada, nunca mais de dois.
4. Nenhum anel, círculo ou elipse em lugar nenhum.
5. A lousa nunca é chapada: a luminância varia um pouco em todo lugar.
6. Pausa parada no fim, depois corte seco (sem crossfade).

E — EXAMINAR
Construa um único arquivo HTML: um <canvas> e uma função pura render(ctx, t, theme, w, h) que desenha o frame t (0–5 s) a partir de theme {bg, ink, accent, accent2, font}. Mesmo t, mesmo frame, em qualquer ordem; hash com semente, sem Math.random. Precisa funcionar em 16:9, 9:16 e 1:1.
Renderize 5 frames (t = 0; 1,25; 2,5; 3,75; 5). Confira: o frame 0 é igual ao frame 5; só dois tamanhos de tipo; o colchete termina exatamente no topo e na base da barra; o número fica no meio da altura da aba; o traço está sob uma palavra só; a lousa não é chapada. Corrija o que falhar e renderize de novo até todas as checagens passarem.
```
