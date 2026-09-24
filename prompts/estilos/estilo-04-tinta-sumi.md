# Estilo 04 — Tinta sumi que floresce

- **Visual:** um único ensō pincelado em tinta luminosa sobre papel escuro e úmido, sangrando num halo suave com borda de maré, selado em vermelhão.
- **Movimento:** o pincel pousa, varre o círculo num fôlego, a tinta floresce para fora, o selo carimba e tudo seca até virar um fantasma.

**Cinco regras:** (1) uma pincelada, um fôlego: pouso lento, meio rápido, saída lenta; (2) a largura segue a pressão: uma mancha no começo, uma cauda seca e partida; (3) falhas de pincel seco só no último terço; (4) a floração se espalha depois do traço, mais onde o pincel estava mais molhado; (5) toda borda de floração tem uma linha de maré, nunca um desfoque limpo.

```
R — REFERÊNCIAS
• Caligrafia zen ensō (busque: ensō brush painting, kasure dry brush).
• Tinta pingada em papel de arroz úmido (nijimi, sangrando com borda de maré).
• Um selo hanko vermelho entalhado, carimbado uma vez no canto.

I — IDEIA
Uma imagem, um fôlego, 5 segundos, em loop sem costura:
• Início (0–1,9 s): um pincel carregado pousa no papel escuro e úmido e varre um círculo, rápido no meio, lento nas pontas, abrindo em cerdas secas na cauda.
• Meio (1,9–3,9 s): a tinta sangra para fora no papel e um selo vermelhão com a inicial de "Motion" carimba uma vez, com força.
• Fim (3,9–5 s): a tinta seca até um fantasma leve do círculo, que é onde a próxima pincelada começa.

S — ESTILO
Visual: papel #0d0c0b com fibras visíveis e manchas, tinta luminosa #ede6d8, uma floração fria #7f93a8, um pequeno selo #d8432f com a letra entalhada em Newsreader. Espaço vazio generoso em volta de um círculo.
Movimento: velocidade do pincel em ease-in-out ao longo de 1,6 s; a floração cresce depois do traço com borda de ruído esfumada; o selo escala de 1,2 para 1 em 0,25 s; o fade até o fantasma em ease-out.
Regras:
1. Uma pincelada, desenhada como uma forma preenchida cuja largura segue a pressão do pincel.
2. Falhas de pincel seco (riscos finos de papel) só no último terço.
3. Floração = lavado suave + uma borda de maré mais clara na beira, guiada por ruído.
4. Mais sangria onde o pincel estava molhado (o começo), menos na cauda seca.
5. Respingos: alguns pontos lançados para fora onde o pincel pousa.
6. O selo é a única cor e carimba uma vez.
7. Textura de papel, queda de luz e grão em todos os frames.

E — EXAMINAR
Construa um único arquivo HTML: um <canvas> e uma função pura render(ctx, t, theme, w, h) que desenha o frame t (0–5 s) a partir de theme {bg, ink, accent, accent2, font}. Mesmo t, mesmo frame, em qualquer ordem; hash com semente, sem Math.random. Precisa funcionar em 16:9, 9:16 e 1:1.
Renderize 5 frames (t = 0; 1,25; 2,5; 3,75; 5). Confira: o frame 0 é igual ao frame 5; a largura do traço afina de verdade; a floração tem borda, não é só desfoque; a letra do selo é nítida e não está cortada; o papel nunca é uma cor chapada. Corrija o que falhar e renderize de novo até todas as checagens passarem.
```
